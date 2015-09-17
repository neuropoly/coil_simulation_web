from coil import Coil
<<<<<<< HEAD
from calc_field import calc_field
import numpy as np
PI = np.pi

N=100

arrays_list = []
coils_list = []
nb_elem = input("Input desired number of coils: ")


"""This block receives inputs from the user to define the coils and the axis system."""
=======

N = 100

coils_list = []
nb_elem = input("Input desired number of coils: ")

>>>>>>> 2cdb83d0d9092f0b629f987963e4a72cf6c021dd
for i in range(int(nb_elem)):
    rada = input("Input radius 'a' (meters): ")
    radb = input("Input radius 'b' (meters): ")
    posinix = input("Input initial X-axis position (meters): ")
    posiniy = input("Input initial Y-axis position (meters): ")
    posiniz = input("Input initial Z-axis position (meters): ")
    coil = Coil(posinix, posiniy, posiniz, rada, radb)
    coils_list.append(coil)

error = True

while error ==	True:

    x_axis_min	= int(input("Input minimum X-axis value: "))
    x_axis_max	= int(input("Input maximum X-axis value: "))
    x_axis_prec	= int(input("Input X-axis precision: "))

    y_axis_min	= int(input("Input minimum Y-axis value: "))
    y_axis_max	= int(input("Input maximum Y-axis value: "))
    y_axis_prec	= int(input("Input Y-axis precision: "))

    z_axis_min	= int(input("Input minimum Z-axis value: "))
    z_axis_max	= int(input("Input maximum Z-axis value: "))
    z_axis_prec	= int(input("Input Z-axis precision: "))

    if x_axis_max - x_axis_min != z_axis_max - z_axis_min:
        print("PANIC: XZ PLAN AXISES NOT EQUAL. NEED TO BE EQUAL TO CONTINUE. RESTART...")
        error = True
    else:
        print("SUCCESSFUL AXIS DEFINITION. BRAVO.")
        error = False

<<<<<<< HEAD
		
axis_dict = {'Xmin': x_axis_min, 'Xmax': x_axis_max, 'Xprec': x_axis_prec,
'Ymin': y_axis_min, 'Ymax': y_axis_max, 'Yprec': y_axis_prec,
'Zmin': z_axis_min, 'Zmax': z_axis_max, 'Zprec': z_axis_prec}
		
i=0
for coil in coils_list:
    arrays_list.append(coil.gen_array(N))
    coil.info()
    i += 1

calc_field(arrays_list, axis_dict, (nb_elem-1))

"""This block computes the results"""

=======
for coil in coils_list:
    coil.info()

input("STAHP")
>>>>>>> 2cdb83d0d9092f0b629f987963e4a72cf6c021dd
