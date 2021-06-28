import webbrowser
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import csv
import orden_alfabetico

def no_encontrado(var):
    var_s = str(var)
    MessageBox.showinfo("No Found", var_s + ' ' + "No encontrado")

def ingresar_NOMBRE_CONTACT():
    MessageBox.showinfo("No se encuentra un contacto", "Ingrese nombres")

def ingresar_contacto():
    MessageBox.showinfo("Ingrese un contacto", "Ingrese los datos")

def eliminar(NOMBRE_CONTACT):
    var_NOMBRE_CONTACT = str(NOMBRE_CONTACT)
    if var_NOMBRE_CONTACT == '':
        ingresar_NOMBRE_CONTACT()
    else:
        buscar = MessageBox.askquestion("Delete alert","¿Desea eliminar contacto\n" + var_NOMBRE_CONTACT)
        if buscar == "yes":
            return True
        else:
            return False
        
    class App():
        def __init__(self, root):
            self.window = root
        
            inbox_frame = LabelFrame(self.window)
            inbox_frame.grid(row = 0, column = 0)
         
            # ---------------- Ventana del nombre, telefono, dirección-----------------
            inbox_frame = LabelFrame(self.window)
            inbox_frame.grid(row = 1, column = 0)
         
            inbox1_frame = LabelFrame(self.window)
            inbox1_frame.grid(row = 1, column = 1)
       
         # ---------------- Ventana de la agenda-----------------
            three_frame = LabelFrame(self.window)
            three_frame.grid(row = 1, column = 1)
        
            three_button_frame = LabelFrame(self.window)
            three_button_frame.grid(row = 3, column = 0)

            Label(inbox_frame, text = 'INGRESE LOS DATOS DEL\n', font = ("Calibri", "13", "normal")).grid(row = 0, column = 0)
            Label(inbox_frame, text = 'CONTACTO Y SELECCIONE UNA OPCION\n', font = ("Calibri", "13", "normal")).grid(row = 0, column = 1)
                       
            Label(inbox_frame, text = 'NOMBRE_CONTACT', font = ("Calibri", "11", "normal")).grid(row = 2, column = 0)
            inbox_NOMBRE_CONTACT = Entry(inbox_frame, font = ("Calibri", "11", "normal"), width = 30)
            inbox_NOMBRE_CONTACT.grid(row = 2, column = 1)
            inbox_NOMBRE_CONTACT.focus()

            Label(inbox_frame, text = 'TELEFONO', font = ("Calibri", "11", "normal")).grid(row = 4, column = 0)
            inbox_TELEFONO = Entry(inbox_frame, font = ("Calibri", "11", "normal"), width = 30)
            inbox_TELEFONO.grid(row = 4, column = 1)

            Label(inbox_frame, text = 'DIRECCION', font = ("Calibri", "11", "normal")).grid(row = 6, column = 0)
            inbox_DIRECCION = Entry(inbox_frame, font = ("Calibri", "11", "normal"), width = 30)
            inbox_DIRECCION.grid(row = 6, column = 1)
            Label(inbox_frame, text = '\n\n', font = ("Calibri", "11", "normal")).grid(row = 7, column = 0)
            
            Label(inbox_frame, text = 'MENÚ DE LA AGENDA\n', font = ("Calibri", "13", "normal")).grid(row = 9, column = 0)
            # --------------- Boton para añadir un contacto -----------------
            ingresar_button = Button(inbox_frame, command = lambda: agregar(), text = 'Ingrese un contacto', width = 20)
            ingresar_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
            ingresar_button.grid(row = 10, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
            # --------------- Boton para eliminar un contacto -----------------
            _eliminar_button = Button(inbox_frame, command = lambda: _eliminar(), text = 'Eliminar contacto', width = 20)
            _eliminar_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
            _eliminar_button.grid(row = 12, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
            # --------------- Boton para mostrar todos los contacto -----------------
            show_contacto_button = Button(inbox_frame, command = lambda: show_contacto(), text = 'Ver todos los contactos', width = 20)
            show_contacto_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
            show_contacto_button.grid(row = 14, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
            self.tree = ttk.Treeview(three_frame, height = 20, columns = ("DOS","TRES"))
            self.tree.grid(padx = 5, pady = 5, row = 0, column = 0, columnspan = 1)
            self.tree.heading("#0", text = 'NOMBRE_CONTACT', anchor = CENTER)
            self.tree.heading("DOS", text = 'TELEFONO', anchor = CENTER)
            self.tree.heading("TRES", text = 'DIRECCION', anchor = CENTER)
            
            def limpiar_inbox():
                inbox_NOMBRE_CONTACT._eliminar(0, 'end')
                inbox_TELEFONO._eliminar(0, 'end')
                inbox_DIRECCION._eliminar(0, 'end')

            def limpiar_treeview():
                tree_lista = self.tree.get_children()
                for item in tree_lista:
                    self.tree._eliminar(item)

            def visualizar_csv():
                contacto = orden_alfabetico.orden_alfabetico()
                for i, row in enumerate(contacto):
                    NOMBRE_CONTACT = str(row[0])
                    TELEFONO = str(row[1])
                    DIRECCION = str(row[2])
                    self.tree.insert("", 0, text = NOMBRE_CONTACT, values = (TELEFONO, DIRECCION))
        
            def _guardar(NOMBRE_CONTACT, TELEFONO, DIRECCION):
                s_NOMBRE_CONTACT = NOMBRE_CONTACT
                s_TELEFONO = TELEFONO
                s_DIRECCION = DIRECCION
                with open('agenda_tarea2.csv', 'a') as f:
                    writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                writer.writerow( (s_NOMBRE_CONTACT, s_TELEFONO,s_DIRECCION) )

            def _buscar(var_inbox, posicion):
                lista = []
                s_var_inbox = str(var_inbox)
                var_posicion = int(posicion)
                with open('agenda_tarea2.csv', 'r') as f:
                    leer = csv.leer(f)
                for i, row in enumerate(leer):
                    if s_var_inbox == row[var_posicion]:
                        lista = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
                return lista

            def _check(consulta, var_buscar):
                lista_consulta = consulta
                var_buscar = var_buscar
                if lista_consulta == []:
                    no_encontrado(var_buscar)
                else:
                    NOMBRE_CONTACT = str(lista_consulta[0])
                    TELEFONO = str(lista_consulta[1])
                    DIRECCION = str(lista_consulta[2])
                    self.tree.insert("", 0, text = NOMBRE_CONTACT, values = (TELEFONO, DIRECCION))
                    self.tree.insert("", 0, text = "Buscar resultado por nombre", values = ("Buscar resultado por telefono", "Buscar resultado por dirección"))
         

            def _check_1(consulta,var_buscar):
                modificar = consulta
                var = var_buscar
                if modificar == []:
                    no_encontrado(var)
                else:
                    TopLevelModify(self.window, modificar)
