from coil import Coil
from phantom import Phantom
from calc_field import calc_field
import numpy as np
import matplotlib.pyplot as plt
from image_slice_B1 import image_slice_B1
from plot_planar_array import plot_planar_array
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import math
from mpl_toolkits.mplot3d import Axes3D
PI = np.pi

coil_definition = 100 #Number of points in each coil

arrays_list = []
coils_list = []

nb_elem = input("Input desired number of coils: ")
rada = input("Input radius 'a' (cm): ") * 0.01
radb = input("Input radius 'b' (cm): ") * 0.01

"""This block receives inputs from the user to define the coils and the axis system."""
for i in range(int(nb_elem)):
    print "Coil #", i
    posinix = input("Input initial X-axis position: ") * 0.01
    posiniy = input("Input initial Y-axis position: ") * 0.01
    posiniz = input("Input initial Z-axis position: ") * 0.01
    coil = Coil(posinix, posiniy, posiniz, rada, radb, coil_definition)
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
i=0
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

for i in range(nb_elem):
    B1_tmp = np.zeros((x_len, y_len, z_len))
    B1_tmp, A_tmp = calc_field(arrays_list, axis_dict, i)
    bB1f = np.sqrt(np.power(bB1f, 2) + np.power(B1_tmp, 2))

B1f = np.zeros((x_len, z_len))
B1f[:, :] = bB1f[:, 1, :]

"""MatPlotLib calls to display the coils in 3-D"""
plot_planar_array(nb_elem, arrays_list, coil_definition)

image_slice_B1(B1f, axis_dict)

plt.show()