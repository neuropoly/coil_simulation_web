from coil import Coil
from calc_field import calc_field
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import math
from mpl_toolkits.mplot3d import Axes3D
PI = np.pi

N=100 #Number of points in each coil

arrays_list = []
coils_list = []

nb_elem = input("Input desired number of coils: ")

"""This block receives inputs from the user to define the coils and the axis system."""
for i in range(int(nb_elem)):
    rada = input("Input radius 'a' (cm): ") * 0.01
    radb = input("Input radius 'b' (cm): ") * 0.01
    posinix = input("Input initial X-axis position: ") * 0.01
    posiniy = input("Input initial Y-axis position: ") * 0.01
    posiniz = input("Input initial Z-axis position: ") * 0.01
    coil = Coil(posinix, posiniy, posiniz, rada, radb)
    coils_list.append(coil)

"""Loop that naively ensures that the inputted axis are equal. To be modified later
 with the web interface"""
error = True

while error:

    x_axis_min = int(input("Input minimum X-axis value: "))
    x_axis_max = int(input("Input maximum X-axis value: "))
    x_axis_prec = int(input("Input X-axis precision: "))

    y_axis_min = int(input("Input minimum Y-axis value: "))
    y_axis_max = int(input("Input maximum Y-axis value: "))
    y_axis_prec = int(input("Input Y-axis precision: "))

    z_axis_min = int(input("Input minimum Z-axis value: "))
    z_axis_max = int(input("Input maximum Z-axis value: "))
    z_axis_prec = int(input("Input Z-axis precision: "))

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
    arrays_list.append(coil.gen_array(N))
    coil.info()
    i += 1

"""This block declares the matrix  for B1 and A and fills them with values returned
by calc_field, which calculates with Biot-Savard the value of the magnetic field in
each point of the user-defined 3-D space"""
x_len = axis_dict['Xmax'] - axis_dict['Xmin']
y_len = axis_dict['Ymax'] - axis_dict['Ymin']
z_len = axis_dict['Zmax'] - axis_dict['Zmin']

B1_tmp = np.zeros((x_len, y_len, z_len))
A_tmp = np.zeros((x_len, y_len, z_len))

bB1f = np.zeros((x_len, y_len, z_len))

for i in range(nb_elem):
    B1_tmp, A_tmp = calc_field(arrays_list, axis_dict, i)
    bB1f = np.sqrt(np.power(bB1f, 2) + np.power(B1_tmp, 2))

B1f = np.zeros((x_len, z_len))
B1f[:, :] = bB1f[:, 1, :]

"""MatPlotLib calls to display the coils in 3-D"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 0
for n in range(nb_elem):
    for i in range(N):
        xs = arrays_list[n][i][0]
        ys = arrays_list[n][i][1]
        zs = arrays_list[n][i][2]
        ax.scatter(xs, ys, zs)
    # ax.plot(arrays_list[n][:][0], arrays_list[n][:][1], arrays_list[n][:][2])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# plt.show()

fig, (ax1) = plt.subplots(nrows=1, figsize=(6,10))

img = ax1.imshow(B1f, extent=[x_axis_min,x_axis_max,z_axis_min,z_axis_max], aspect=1)
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)
ax1.set_title('B1 Sensitivity Profile')
ax1.set_xlabel('X Axis [cm]', fontsize=16, labelpad=20)
ax1.set_ylabel('Z Axis [cm]', fontsize=16, labelpad=20)
plt.tight_layout()
cbar = fig.colorbar(img, cax=cax)
cbar.ax.set_ylabel('verbosity coefficient', labelpad=20)
plt.show()