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
         

print ("\nConectado\n")

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
    print("Presione '8' Si desea eliminar por nombre");
    print("Presione '9' Si desea eliminar por telefono");
    print("Presione '10' Si desea eliminar por direccion");
    
agendaContact     = []
nombre_contact    = []
telefono_contact  = []
direccion_contact = []

opciones       = 0
opcionBusqueda = 0
opcionEliminar = 0
agenda()

while opciones != 4:
    opciones =  str(input("Ingrese la opcion: "))
    socket_cliente.send(opciones.encode("utf-8"))
    if opciones == 1:
        print("Ingrese el nombre del contacto");
        nombre_contact      = input()
        
        print("Ingrese el numero de teléfono del contacto");
        telefono_contact    = input()
      
        print("Ingrese la direccion del contacto");
        direccion_contact   = input() 
        with open('Tarea2-Redes-de-Computadores/agenda.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r')
    recibido = socket_cliente.recv(1024).decode('utf-8')
    print ("Servidor >> " + recibido)
        
        
            
    """ elif opciones == 2:
        busqueda()
        opcionBusqueda = int(input("¿Por qué opción desea buscar?\n"));
        if opcionBusqueda == 5: 
            print("Nombre del contacto: ")
            nombre_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if nombre_contact == row[0]:
                        print(','.join(row))
        
        elif opcionBusqueda == 6:
            print("Número del contacto: ")
            telefono_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if telefono_contact == row[1]:
                        print(','.join(row))
                
        elif opcionBusqueda == 7:
            print("Dirección del contacto: ")
            direccion_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if direccion_contact == row[2]:
                        print(','.join(row))
                        
    elif opciones == 3:
        eliminar()
        opcionEliminar = int(input("¿Por qué opción desea eliminar?\n"));
        if opcionEliminar == 8: 
            print("Nombre del contacto: ")
            nombre_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if nombre_contact != row[0]:
                        writer.writerow(row)
            print("contacto eliminado")
            
        elif opcionEliminar == 9: 
            print("Telefono del contacto: ")
            telefono_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if telefono_contact != row[1]:
                        writer.writerow(row)
            print("contacto eliminado")
            
        elif opcionEliminar == 10: 
            print("Dirección del contacto: ")
            direccion_contact = input()
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('Tarea2-Redes-de-Computadores/agenda.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if direccion_contact != row[2]:
                        writer.writerow(row)
            print("contacto eliminado")
        
    elif opciones == 4:
        break
            
try:
    while True:
        mensaje = str(input("Yo >> "))
        socket_cliente.send(mensaje.encode("utf-8"))
        if mensaje == "finalizar()":
            break
        recibido = socket_cliente.recv(1024).decode('utf-8')
        print ("Servidor >> " + recibido) """

""" except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrumpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.") """