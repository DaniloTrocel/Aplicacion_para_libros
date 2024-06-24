import os
from tabulate import tabulate
from conexion import *
from libro import * 

con = conectar()

def iniciar():
    os.system('cls')
    while True:
        print('Seleccione una de las opciones')
        print('\t1. Añadir un libro')
        print('\t2. Ver todos los libros')
        print('\t3. Buscar un libro')
        print('\t4. Modificar un libro')
        print('\t5. Eliminar un libro')
        print('\t6. Salir de la aplicacion')
        opcion = input('Escoja una opcion: ')
        if opcion == '1':
            nuevo_libro()
        elif opcion == '2':
            ver_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':
            modificar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
             break
        else:
            print('Escoja una opción correcta') 

def nuevo_libro():
    titulo = input('Ingrese título del libro: ')
    autor = input('Ingrese el nombre del autor: ')
    estado = 'Disponible'
    respuesta = registrar(titulo, autor, estado)
    print(respuesta) 

def ver_libros():
    datos = mostrar()
    heater = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, heater, tablefmt='fancy_grid')
    print(tabla)

def buscar_libro():
    id = input('Ingrese el id del libro: ')
    datos = buscar(id)
    heater = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, heater, tablefmt='fancy_grid')
    print(tabla)

def modificar_libro():
    id = input('ingres el id del libro a modificar: ')
    nuevo_valor = ''
    respuesta = ''
    campo = input('Opciones de los campos que desea modificar\n1. Título\n2. Autor\n3. Estado\n' 'Seleccione el campo que desea modificar: ')
    if campo == '1':
        nuevo_valor = input('Ingrese el nuevo título del libro: ')
    elif campo == '2':
        nuevo_valor = input('Ingrese el nuevo autor del libro: ')
    elif campo == '3':
        nuevo_valor = input('Ingrese el nuevo estado del libro: ')
    respuesta = modificar(id, campo, nuevo_valor)
    print(respuesta)

def eliminar_libro():
    id = input('ingrese el id del libro que desea eliminar: ')
    respuesta = eliminar(id)
    print(respuesta)

iniciar()      