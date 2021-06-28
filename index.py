import pandas as pd
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