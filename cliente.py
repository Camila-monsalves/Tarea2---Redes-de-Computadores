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
         

print ("\nConectado, escriba finalizar() para terminar la conexión.\n")

def agenda():
    print("AGENDA");
    print("Presione '1' Si desea Agregar un nuevo contacto");
    print("Presione '2' Si desea Buscar un contacto");
    print("Presione '3' Si desea Eliminar un contacto");
    print("Presione '4' Si desea Salir");
        
agendaContact     = []
nombre_contact    = []
telefono_contact  = []
direccion_contact = []

opciones       = 0
opcionBusqueda = 0
opcionEliminar = 0
agenda()
    
try:
    while True:
        opciones =  str(input("Ingrese la opcion: "))
        
        socket_cliente.send(opciones.encode("utf-8"))
        
        if opciones == str(1):
            print("Ingrese el nombre del contacto");
            nombre_contact      = input()
            
            print("Ingrese el numero de teléfono del contacto");
            telefono_contact    = input()
        
            print("Ingrese la direccion del contacto");
            direccion_contact   = input()
            
            lista_datos = [nombre_contact, telefono_contact, direccion_contact]
            socket_cliente.send(str(lista_datos).encode("utf-8"))
            recibido = socket_cliente.recv(1024).decode('utf-8')
            print ("Servidor >> " + recibido)      
            
        elif opciones == str(2):
            print("Nombre del contacto: ")
            nombre_contact = input()
            socket_cliente.send(nombre_contact.encode("utf-8"))
            datos = socket_cliente.recv(1024).decode('utf-8')
            print(datos)
                
                            
        elif opciones == str(3):
            print("Nombre del contacto: ")
            nombre_contact = input()
            socket_cliente.send(nombre_contact.encode("utf-8"))
            datos = socket_cliente.recv(1024).decode('utf-8')
            print(datos)

            
        elif opciones == str(4):
            break
        
except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrumpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")