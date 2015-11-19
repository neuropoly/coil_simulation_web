import sys
from coil import Coil
from phantom import Phantom
from calc_field import calc_field
from msct_parser import Parser
import numpy as np
import matplotlib.pyplot as plt
from image_slice_B1 import image_slice_B1
from plot_planar_array import plot_planar_array
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import math
from mpl_toolkits.mplot3d import Axes3D

PI = np.pi


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
                      mandatory=False,
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
    return parser


# Get parser info
parser = get_parser()
arguments = parser.parse(sys.argv[1:])
rad_a = arguments['-rada']
rad_b = arguments['-radb']
r = arguments['-r']
c = arguments['-c']
o = arguments['-o']
o1 = arguments['-o1']
orientation = arguments['-orientation']
slice_location = arguments['-slice']


coil_definition = 25  # Number of points in each coil

arrays_list = []
coils_list = []
preset_try = input("Do you want to use a preset? (1/0)")
if preset_try == 1:
    d = 0.75*2*rad_a
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
                coils_list.pop()
        else:
            d_x = d * pytha_x
        for j in range(c):
            coil = Coil((d * j + d_x) * 0.01, (d_y * i) * 0.01, 0, rad_a * 0.01, rad_b * 0.01, coil_definition)
            coils_list.append(coil)
else:
    nb_elem = input("Input desired number of coils: ")
    rad_a = input("Input radius 'a' (cm): ") * 0.01
    rad_b = input("Input radius 'b' (cm): ") * 0.01

    """This block receives inputs from the user to define the coils and the axis system."""
    for i in range(int(nb_elem)):
        print "Coil #", i
        pos_ini_x = input("Input initial X-axis position: ") * 0.01
        pos_ini_y = input("Input initial Y-axis position: ") * 0.01
        pos_ini_z = input("Input initial Z-axis position: ") * 0.01
        coil = Coil(pos_ini_x, pos_ini_y, pos_ini_z, rad_a, rad_b, coil_definition)
        coils_list.append(coil)

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

"""This block generates each point of the coil in a 3-D space"""
i = 0
for coil in coils_list:
    arrays_list.append(coil.gen_array(coil_definition))
    coil.info()
    i += 1

"""This block declares the matrix  for B1 and A and fills them with values returned
by calc_field, which calculates with Biot-Savard the value of the magnetic field in
each point of the user-defined 3-D space"""
x_len = int((axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec'])
y_len = int((axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec'])
z_len = int((axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec'])

B1_tmp = np.zeros((x_len, y_len, z_len))
A_tmp = np.zeros((x_len, y_len, z_len))

bB1f = np.zeros((x_len, y_len, z_len))

"""Sum of every contribution by each coil"""
for i in range(nb_elem):
    B1_tmp = np.zeros((x_len, y_len, z_len))
    B1_tmp, A_tmp = calc_field(arrays_list, axis_dict, i)
    bB1f = np.sqrt(np.power(bB1f, 2) + np.power(B1_tmp, 2))

B1f = np.zeros((x_len, z_len))
B1f[:, :] = bB1f[:, 1, :]

"""MatPlotLib calls to display the coils in 3-D"""
plot_planar_array(nb_elem, arrays_list, coil_definition, o1)

image_slice_B1(B1f, axis_dict, o)

plt.show()