import webbrowser
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import csv

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
