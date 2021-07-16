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

print ("\nConectado, escriba finalizar() para terminar la conección.\n")

def agenda():
    contactos = []
    class contact():
        NOMBRE_CONTACT  = ""
        TELEFONO        = ""
        DIRECCION       = ""
    while True:
        print("Bienvenido a la Agenda");
        print("Presione '1' Si desea agregar un nuevo contacto");
        print("Presione '2' Si desea visualizar un contacto");
        print("Presione '3' Si desea eliminar un contacto");
        seleccion = input("Seleccione una opción de las indicadas: ");

        if seleccion == "1" :
            print("Bienvenido a la seccion 'Agregar Contacto'");
            contacto                = contact()
            contacto.NOMBRE_CONTACT = input("Ingrese el nombre al nuevo contacto:         ");
            contacto.TELEFONO       = input("Ingrese el telefono al nuevo contacto:       ");
            contacto.DIRECCION      = input("Ingrese la dirección al nuevo contacto:      ");
            contactos.append(contacto)
        elif seleccion == "2" :
            print("Bienvenido a la seccion 'Visualizar Contacto'");
            with open('agenda_tarea2.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['NOMBRE_CONTACT'], row['TELEFONO'], row['DIRECCION'])
        elif seleccion == "3" :
            print("Bienvenido a la seccion 'Eliminar Contacto'");
            
''' agenda = pd.read_csv("agenda_tarea2.csv", sep = ';')
print(agenda) '''
''' agenda()  '''
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
