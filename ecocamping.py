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
    elif opcion == 3:
        print(f"\n-- Registrar salida (vehiculos o sitios ocupados: {sitios_ocupados})")
        if sitios_ocupados == 0:
            print(" No hay vehiculos registrados en el camping actualmente")
        else:
            try:
                salida = int(input("¿cuantos vehiculos se retiran?"))
                if salida <= 0:
                   print("Error: la cantidad debe ser mayor a 0")
                elif salida > sitios_ocupados:
                   print(f"Error: no se puede retirar mas de {sitios_ocupados} vehiculos")
                else:
                    sitios_ocupados -=salida
                    print(f"salida registrada,sehan liberado {salida} sitios")
            except ValueError:
                print("Error:debe ingresar un numero entero valido")               
    elif opcion == 4:
        porcentaje_ocupacion = (sitios_ocupados / capacidad_maxima) * 100
        print(f"\n[ESTADO] Ocupacion actual: {sitios_ocupados}/{capacidad_maxima} sitios")
        print(f"[ESTADO] El camping esta al {porcentaje_ocupacion:.1f}% de su capacidad")
    elif opcion == 5:
        print("Cerrando el sistema")
        ejecutando = False
    else:
        print("Opcion fuera de rango")
    