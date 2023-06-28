import os
import msvcrt
import time
import numpy

guarderia = numpy.zeros((2,5),int)

lista_nombre = []
lista_rut = []
lista_nombre_masc = []
lista_estadia = []
lista_habitacion = []
lista_fila = []
lista_columna = []

def menu_guarderia():
    os.system("cls")
    while True:
        print("""MENÚ "MASCOTA SEGURA"
        1. Grabar
        2. Buscar
        3. Retirarse
        4. Salir""")
        return

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opción (1 AL 4): "))
            if opc in (1,2,3,4):
                return opc
            else:
                print("ERROR! DEBE INGRESAR UNA DE LAS OPCIONES DEL 1 AL 4")
        except:
            print("ERROR! LA OPCION DEBE SER UN NÚMERO ENTERO!!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre mascota: ")
        if len(nombre) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_cantidad_dia():
    while True:
        try:
            cant_dia = int(input("Ingrese días de estadia: "))
            if cant_dia >= 1:
                return cant_dia
            else:
                print("ERROR! DEBE REGISTRAR AL MENOS 1 DÍA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_habitación(p_habit):
    while True:
        try:
            habitacion = int(input("Ingrese número de habitación: "))
            if habitacion in(p_habit):
                return habitacion
            else:
                print("ERROR! NÚMERO DE HABITACIÓN NO DISPONIBLE!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def ver_guarderia():
    os.system("cls")
    while True:
        print("\t GUARDERIA \n")
        contador = 1
        for x in range(2):
            print(f"Piso {x+1}", end=" ")
            for y in range(5):
                print(f"Habitación {contador}: {guarderia[x][y]}",end=" ")
                contador+=1
                print("\n")
            time.sleep(3)
            return

def habitacion_disponible():
    contador = 1
    lista_habitacion = []
    for x in range (2):
        for y in range (5):
            if guarderia[x][y] == 0:
                lista_habitacion.append(contador)

def guardar_datos():
    os.system("cls")
    while True:
        nombre = validar_nombre()
        rut = validar_rut()
        nombre_mascota = validar_nombre_mascota()
        cantidad_dia = validar_cantidad_dia()
        ver_guarderia()
        habitacion = validar_habitación()

        lista_nombre.append(nombre)
        lista_rut.append(rut)
        lista_nombre_masc.append(nombre_mascota)
        lista_estadia.append(cantidad_dia)
        lista_habitacion.append(habitacion)
        
        print("Precione enter para continuar...")
        msvcrt.getch()
        return

def buscar():
    os.system("cls")
    while True:
        rut = validar_rut()
        lista_rut.index(rut)

