import funciones as fn

while True:
    fn.menu_guarderia()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.guardar_datos()
    elif opcion == 2:
        fn.buscar()
    elif opcion == 3:
        pass
    else:
        print("Gracias por su preferencia")
        break