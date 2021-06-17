import pandas as pd
import webbrowser
import os

''' agenda = pd.DataFrame({
    "Nombre":["Vania","Camila","Luis"],
    "Teléfono":[133,132,131],
    "Dirección":["Calle falsa 123","Hualpen","San Pedro"]

}
) '''
def agenda():
    contactos = []
    class contact():
        ID              = ""
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
            contacto.ID             = input("Ingrese un identificador al nuevo contacto:  ");
            contacto.NOMBRE_CONTACT = input("Ingrese el nombre al nuevo contacto:         ");
            contacto.TELEFONO       = input("Ingrese el telefono al nuevo contacto:       ");
            contacto.DIRECCION      = input("Ingrese la dirección al nuevo contacto:      ");
            contactos.append(contacto)
        elif seleccion == "2" :
            """ AQUI FAlTA """
''' agenda = pd.read_csv("agenda_tarea2.csv", sep = ';')
print(agenda) '''
agenda() 

