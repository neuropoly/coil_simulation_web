from coil import Coil

N = 100

coils_list = []
nb_elem = input("Input desired number of coils: ")

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

for coil in coils_list:
    coil.info()

input("STAHP")