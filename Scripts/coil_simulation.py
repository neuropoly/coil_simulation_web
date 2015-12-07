import sys
from coil import Coil
from calc_R import calc_R
from calc_SNR import calc_SNR
from phantom import Phantom
from calc_field import calc_field
from msct_parser import Parser
import numpy as np
import matplotlib.pyplot as plt
from image_slice_B1 import image_slice_B1
from plot_planar_array import plot_planar_array
from create_wrapped_elem import create_wrapped_elem
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import math
from mpl_toolkits.mplot3d import Axes3D

PI = np.pi

"""Main function"""

def get_parser():
    # Initialize parser
    parser = Parser(__file__)

    # TODO Ensure parser can properly receive arguments from a web request
    parser.usage.set_description("This program takes a preset coil configuration as input"
                                 "that is either cylindrical or planar, and computes the "
                                 "corresponding magnetic field by calling calc_field.py."
                                 " This magnetic field is then showed to the user as a "
                                 "slice with field intensity. The user can also display"
                                 " the coils.")

    parser.add_option(name="-rada",
                      type_value="float",
                      description="Determine radius a",
                      mandatory=True,
                      example="1",
                      default_value="3")

    parser.add_option(name="-radb",
                      type_value="float",
                      description="Determine radius b",
                      mandatory=True,
                      example="1",
                      default_value="3")

    parser.add_option(name="-radc",
                      type_value="float",
                      description="Determine radius c of cylinder (for circular_array)",
                      mandatory=False,
                      example="1",
                      default_value="3")

    parser.add_option(name="-r",
                      type_value="int",
                      description="Determine number of rows",
                      mandatory=True,
                      example="1",
                      default_value="1")

    parser.add_option(name="-c",
                      type_value="int",
                      description="Determine number of columns",
                      mandatory=True,
                      example="1",
                      default_value="1")

    parser.add_option(name="-o",
                      type_value="file_output",
                      description="Magnetic field file",
                      mandatory=True,
                      example="b1_field.png",
                      default_value='')

    parser.add_option(name="-o1",
                      type_value="file_output",
                      description="Coils array file",
                      mandatory=True,
                      example="coils.png",
                      default_value='')

    parser.add_option(name="-definition",
                      type_value="int",
                      description="Coil definition (number of points)",
                      mandatory=True,
                      example="100",
                      default_value='100')

    parser.add_option(name="-orientation",
                      type_value="int",
                      description="Determine which plane the slice will be taken in (1 for XZ, 2 for XY)",
                      mandatory=True,
                      example="1",
                      default_value='1')

    parser.add_option(name="-slice",
                      type_value="int",
                      description="Determines the location of the slice in the corresponding plane",
                      mandatory=True,
                      example="5",
                      default_value='0')

    parser.add_option(name="-radius",
                      type_value="int",
                      description="Determine if array is cylindrical by giving it a radius (in cm)",
                      mandatory=False,
                      example="3",
                      default_value="0")

    parser.add_option(name="-m",
                      type_value="material",
                      description="Material to be analyzed (phantom)",
                      mandatory=False,
                      example="water",
                      default_value="water")

    parser.add_option(name="-type",
                      type_value="int",
                      description="Determine wanted simulation (1 = Planar, 2 = Circular)",
                      mandatory=True,
                      example="1",
                      default_value="1")

    parser.add_option(name="-preset",
                      type_value="int",
                      description="Determine wanted simulation preset (0 = No preset, 1 = Preset)",
                      mandatory=True,
                      example="1",
                      default_value="0")
    return parser


""" Get parser info """
parser = get_parser()
arguments = parser.parse(sys.argv[1:])
rad_a = arguments['-rada']
rad_b = arguments['-radb']
rad_c = arguments['-radc']
r = arguments['-r']
c = arguments['-c']
o = arguments['-o']
o1 = arguments['-o1']
orientation = arguments['-orientation']
slice_location = arguments['-slice']
coil_definition = arguments['-definition']
type = arguments['-type']
preset = arguments['-preset']

arrays_list = []
coils_list = []

"""Preset, number of coil according to lines and columns"""
if preset == 1:
    rad_a = rad_a * 0.01
    rad_b = rad_b * 0.01
    rad_c = rad_c * 0.01
    d = 0.75 * 2 * rad_a
    """60 deg = 1.0472 rad"""
    pytha_x = np.cos(1.0472)
    pytha_y = np.sin(1.0472)
    d_x = d * pytha_x
    d_y = d * pytha_y
    nb_elem = int((c * r) - round(r / 2))

    for i in range(r):
        if i % 2 == 0:
            d_x = 0
            if i != 0:
                """Minus one coil according to theory"""
                coils_list.pop()
        else:
            d_x = d * pytha_x
        for j in range(c):
            coil = Coil((d * j + d_x), (d_y * i), 0, rad_a, rad_b, coil_definition)
            coils_list.append(coil)

    """If preset on a cylinder"""
    if type == 2:
        for j in range(int(nb_elem)):
            coils_list[j].posinix = create_wrapped_elem(rad_c, int(nb_elem))[j]

        for coil in coils_list:
            coil.rotation(rad_c)

        for coil in coils_list:
            coil_translated = coil.translation(rad_c)
            coil.coil_array = coil_translated

    """Coils on plan"""
elif type == 1:
    nb_elem = input("Input desired number of coils: ")
    rad_a = rad_a * 0.01
    rad_b = rad_b * 0.01

    """This block receives inputs from the user to define the coils and the axis system."""
    for i in range(int(nb_elem)):
        print "Coil #", i
        pos_ini_x = input("Input initial X-axis position: ") * 0.01
        pos_ini_y = input("Input initial Y-axis position: ") * 0.01
        pos_ini_z = input("Input initial Z-axis position: ") * 0.01
        coil = Coil(pos_ini_x, pos_ini_y, pos_ini_z, rad_a, rad_b, coil_definition)
        coils_list.append(coil)

    """Coils on a cylinder"""
else:
    nb_elem = input("Input desired number of coils: ")
    rad_a *= 0.01
    rad_b *= 0.01
    rad_c *= 0.01

    """This block receives inputs from the user to define the coils and the axis system."""
    for i in range(int(nb_elem)):
        print "Coil #", i
        pos_ini_x = input("Input initial X-axis position: ") * 0.01
        pos_ini_y = input("Input initial Y-axis position: ") * 0.01
        pos_ini_z = input("Input initial Z-axis position: ") * 0.01
        coil = Coil(pos_ini_x, pos_ini_y, pos_ini_z, rad_a, rad_b, coil_definition)
        coils_list.append(coil)

    for j in range(int(nb_elem)):
         coils_list[j].posinix = create_wrapped_elem(rad_c, int(nb_elem))[j]

    for coil in coils_list:
        coil.rotation(rad_c)

    for coil in coils_list:
        coil_translated = coil.translation(rad_c)
        coil.coil_array = coil_translated

for coil in coils_list:
    arrays_list.append(coil.coil_array)
    coil.info()


"""Loop that naively ensures that the inputted axis are equal. To be modified later
   with the web interface"""
error = True

while error:
    print "AXIS DEFINITION: "
    x_axis_min = input("Input minimum X-axis value: ") * 0.01
    x_axis_max = input("Input maximum X-axis value: ") * 0.01
    x_axis_prec = input("Input X-axis precision: ") * 0.01

    y_axis_min = input("Input minimum Y-axis value: ") * 0.01
    y_axis_max = input("Input maximum Y-axis value: ") * 0.01
    y_axis_prec = input("Input Y-axis precision: ") * 0.01

    z_axis_min = input("Input minimum Z-axis value: ") * 0.01
    z_axis_max = input("Input maximum Z-axis value: ") * 0.01
    z_axis_prec = input("Input Z-axis precision: ") * 0.01

    if x_axis_max - x_axis_min != z_axis_max - z_axis_min:
        print("PANIC: XZ PLAN AXISES NOT EQUAL. NEED TO BE EQUAL TO CONTINUE. RESTART...")
        error = True
    else:
        print("SUCCESSFUL AXIS DEFINITION. BRAVO.")
        error = False

"""Structure simplifying the passing of axis dimensions as arguments to other functions"""
axis_dict = {'Xmin': x_axis_min, 'Xmax': x_axis_max, 'Xprec': x_axis_prec,
             'Ymin': y_axis_min, 'Ymax': y_axis_max, 'Yprec': y_axis_prec,
             'Zmin': z_axis_min, 'Zmax': z_axis_max, 'Zprec': z_axis_prec}

print "COIL ARRAY SHAPE :", coils_list[0].coil_array.shape

"""This block declares the matrix  for B1 and A and fills them with values returned
by calc_field, which calculates with Biot-Savard the value of the magnetic field in
each point of the user-defined 3-D space"""
x_len = int((axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec'])
y_len = int((axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec'])
z_len = int((axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec'])

B1_tmp = np.zeros((x_len, y_len, z_len))
A_tmp = np.zeros((x_len, y_len, z_len))

bB1f = np.zeros((x_len, y_len, z_len))
B1_tmp = np.zeros((x_len, y_len, z_len))


"""Sum of every contribution by each coil"""
for i in range(nb_elem):
    B1_tmp, A_tmp = calc_field(arrays_list, axis_dict, i, coil_definition)
    bB1f = np.sqrt(np.power(bB1f, 2) + np.power(B1_tmp, 2))

if orientation == 1:
    B1f = np.zeros((x_len, z_len))
    B1f[:, :] = bB1f[:, slice_location, :]

if orientation == 2:
    B1f = np.zeros((x_len, y_len))
    B1f[:, :] = bB1f[:, :, slice_location]

"""Compute signal noise"""
R = calc_R(A_tmp, nb_elem, rad_c, axis_dict)

# SNR = calc_SNR(B1_tmp, nb_elem, R, axis_dict)

"""MatPlotLib calls to display the coils in 3-D"""
plot_planar_array(nb_elem, arrays_list, coil_definition, o1)

image_slice_B1(B1f, axis_dict, o)

plt.show()