print("Gestion eco-Camping 'Bosque Vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True 
while ejecutando:
    print("\n=== MENU DE CONTROL DE REGISTROS")
    print("1.- ver sitios disponibles")
    print("2.- registro denuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida vehiculos(Salida)")
    print("4.- Estado actualde camping")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, porfavor seleccione entre 1 y5")
        continue
    #Despliegue de opciones
    if opcion == 1:
        disponibles= capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitioslibres para recibir vehiculos: {disponibles}")
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print("lo sentimos noquedan espacios en el camping")
        else:
            try:
                ingreso = int(input("¿Cuantos sitios o vehiculos van a ingresar?"))
                if ingreso <= 0:
                    print("Error: la cantidad de ingreso debe ser mayora 0")
                elif ingreso > sitios_libres:
                    print(f"solo puede ingresar un maximo de {sitios_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error:debe ingresar un numero valido")
    else:
        print("Opcion fuera de rango")
    