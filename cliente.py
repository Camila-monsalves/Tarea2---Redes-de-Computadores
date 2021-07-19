import socket
import sys

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('0.0.0.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio desarrollado.")
    sys.exit(0)

IP = get_ip()  
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, "en el servidor ", IP, "\n")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(2)

print ("Servicio configurado en puerto ", PUERTO, "en el servidor ", IP, "\n")

<<<<<<< HEAD

        
            
try:
    while True:
        while opciones != 4:
            opciones =  int(input("Ingrese la opcion: "))
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
                        writer.writerow( (nombre_contact, telefono_contact, direccion_contact) )
                opciones = socket_cliente.recv(1024).decode('utf-8')
                print("Servidor >>" + opciones)
                
        
            
            elif opciones == 2:
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print("Servidor >>" + recibido)
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
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print("Servidor >>" + recibido)
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
        
                

=======
try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)
>>>>>>> parent of 7bfa410 (act)

        while True:
            try:
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >> ", recibido)
                if recibido == "finalizar()":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                socket_cliente.send(respuesta_servidor.encode("utf-8"))
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")
