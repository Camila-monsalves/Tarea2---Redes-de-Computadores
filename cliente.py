#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa Cliente

import socket
import sys
import pandas as pd
import csv

        
if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

print ("\nConectandose al servidor ", IP, " en el puerto ", PUERTO, " ...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.", IP, " en el puerto ", PUERTO)
    sys.exit(0)


def agenda():
    print("AGENDA");
    print("Presione '1' Si desea Agregar un nuevo contacto");
    print("Presione '2' Si desea Buscar un contacto");
    print("Presione '3' Si desea Eliminar un contacto");
    print("Presione '4' Si desea Salir");
    
def busqueda():
    print("Presione '5' Si desea realizar una busqueda por nombre");
    print("Presione '6' Si desea realizar una busqueda por telefono");
    print("Presione '7' Si desea realizar una busqueda por direccion");
    
def eliminar():
    print("'Presione 8' Si desea Eliminar por nombre");
    print("'Presione 9' Si desea Eliminar por número");

agendaContact     = []
nombre_contact    = []
telefono_contact  = []
direccion_contact = []

opciones       = 0
opcionBusqueda = 0
agenda()

while opciones != 4:
    opciones =  int(input("Ingrese la opcion"))
    if opciones == 1:
        print("Ingrese el nombre del contacto");
        nombre_contact      = input()
        print("Ingrese el numero de teléfono del contacto");
        telefono_contact    = input()
        print("Ingrese la direccion del contacto");
        direccion_contact   = input()
        agendaContact.append([nombre_contact, telefono_contact, direccion_contact])
        print(agenda);
    elif opciones == 2:
        busqueda()
        opcionBusqueda = input("¿Por qué opción desea buscar?\n");
        if opcionBusqueda == 5: 
            nombre_contact = input("Nombre contacto buscado:")
            if nombre_contact in telefono_contact: 
                print("Telefono:", telefono_contact[nombre_contact]);
            else:
                print("La busqueda no arroja nada");
                          
        elif opcionBusqueda == 6:
            telefono_contact = input("Telefono contacto buscado:")
            if telefono_contact in nombre_contact:
                print("Nombre:", nombre_contact[telefono_contact]);
            else:
                print("La busqueda no arroja nada");
        
        elif opcionBusqueda == 7:
            direccion_contact = input("Direccion del contacto buscado:")
            if direccion_contact in nombre_contact:
                print("Nombre:", direccion_contact[nombre_contact]);
            else:
                print("La busqueda no arroja nada");
    elif opciones == 3:
        eliminar()
        opcionEliminar = input("")
        if opcionEliminar == 8:
            nombre_contact = input("Nombre: ")
            if nombre_contact not in agenda[0:100]:
                print('Contacto eliminado con exito');
            else:
                print("No existe el nombre a eliminar");
                
        elif opcionEliminar == 9:
            telefono_contact = input("Número: ")
            if telefono_contact not in agenda[0:100]:
                print('Contacto eliminado con exito');
            else:
                print("No existe el nombre a eliminar");
            
            
            

print ("\nConectado, escriba finalizar() para terminar la conección.\n")
try:
    while True:
        mensaje = str(input("Yo >> "))
        socket_cliente.send(mensaje.encode("utf-8"))
        if mensaje == "finalizar()":
            break
        recibido = socket_cliente.recv(1024).decode('utf-8')
        print ("Servidor >> " + recibido)

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")
