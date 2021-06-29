from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import orden_alfabetico
import csv

# -------------------------- Funciones globales ------------------------------------------

# -----------  ---------------------------------------
def no_encontrado(var):
    var_s = str(var)
    MessageBox.showinfo("No Found", var_s + ' ' + "no encontrado")

def write_NOMBRE_CONTACT():
    MessageBox.showinfo("No se encuentra un contacto", "Ingrese nombres")

def write_contacto():
    MessageBox.showinfo("Ingrese un contacto", "Ingrese los datos\"Añadir contacto\" option")

def delete_mesageBox(NOMBRE_CONTACT):
    var_NOMBRE_CONTACT = str(NOMBRE_CONTACT)
    if var_NOMBRE_CONTACT == '':
        write_NOMBRE_CONTACT()
    else:
        buscar = MessageBox.askquestion("Delete alert","¿Desea eliminar contacto\n" + var_NOMBRE_CONTACT)
        if buscar == "yes":
            return True
        else:
            return False

# --------------------  -------------------------------
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

        # ---------------  ------------------
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

        # ---------------  -----------------
        
        Label(inbox_frame, text = 'MENÚ DE LA AGENDA\n', font = ("Calibri", "13", "normal")).grid(row = 9, column = 0)
        # --------------- Boton para añadir un contacto -----------------
        ingresar_button = Button(inbox_frame, command = lambda: agregar(), text = 'Ingrese un contacto', width = 20)
        ingresar_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        ingresar_button.grid(row = 10, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
        # --------------- Boton para eliminar un contacto -----------------
        delete_button = Button(inbox_frame, command = lambda: delete(), text = 'Eliminar contacto', width = 20)
        delete_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        delete_button.grid(row = 12, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
        # --------------- Boton para mostrar todos los contacto -----------------
        show_contacts_button = Button(inbox_frame, command = lambda: show_contacto(), text = 'Ver todos los contactos', width = 20)
        show_contacts_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        show_contacts_button.grid(row = 14, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
        
        
         # --------------- Boton para limpiar la pantalla de la agenda -----------------
        guardar_changes_button = Button(inbox_frame, command = lambda: limpiar(), text = 'Limpiar vista', width = 20)
        guardar_changes_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        guardar_changes_button.grid(row = 16, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--

        # -------------- Menu de opciones para busqueda ----------------
        buscar_button = Button(inbox_frame, command = lambda: buscar(), text = 'Buscar contacto por:', width = 20)
        buscar_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        buscar_button.grid(row = 18, column = 0, padx = 3, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
          
        combo = ttk.Combobox(inbox_frame, state = 'readonly', width = 17, justify = 'center', font = ("Calibri", "10", "normal"))
        combo["values"] = ['NOMBRE_CONTACT', 'TELEFONO', 'DIRECCION']
        combo.grid(row = 18, column = 1, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación las opciones de busqueda--
        combo.current(0)

        # ---------------  -----------------
        # Tabla para la base de datos
       
        self.tree = ttk.Treeview(three_frame, height = 20, columns = ("DOS","TRES"))
        self.tree.grid(padx = 5, pady = 5, row = 0, column = 0, columnspan = 1)
        self.tree.heading("#0", text = 'NOMBRE_CONTACT', anchor = CENTER)
        self.tree.heading("DOS", text = 'TELEFONO', anchor = CENTER)
        self.tree.heading("TRES", text = 'DIRECCION', anchor = CENTER)

        scrollVert = Scrollbar(three_frame, command = self.tree.yview)
        self.tree.configure(yscrollcommand = scrollVert.set)
        scrollVert.grid(row = 0, column = 1, sticky = "nsew")

        scroll_x = Scrollbar(three_frame, command = self.tree.xview, orient = HORIZONTAL)
        self.tree.configure(xscrollcommand = scroll_x.set)
        scroll_x.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew")

# --------------------------  -----------------------------

        # --------------- funciones auxiliares ------------------
        def _limpiar_inbox():
            # 
            inbox_NOMBRE_CONTACT.delete(0, 'end')
            inbox_TELEFONO.delete(0, 'end')
            inbox_DIRECCION.delete(0, 'end')

        def _limpiar_treeview():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)

        def _view_csv():
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
            my_list = []
            s_var_inbox = str(var_inbox)
            var_posicion = int(posicion)
            with open('agenda_tarea2.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_posicion]:
                        my_list = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
            return my_list

        def _check(answer, var_buscar):
            list_answer = answer
            var_buscar = var_buscar
            if list_answer == []:
                no_encontrado(var_buscar)
            else:
                NOMBRE_CONTACT = str(list_answer[0])
                TELEFONO = str(list_answer[1])
                DIRECCION = str(list_answer[2])
                self.tree.insert("", 0, text = NOMBRE_CONTACT, values = (TELEFONO, DIRECCION))
                self.tree.insert("", 0, text = "Busqueda de resultado por nombre", values = ("Busqueda de resultado por telefono", "Busqueda de resultado por direccion"))
        

        # ----------------- Funciones de cada boton ------------------
        def agregar():
            NOMBRE_CONTACT = inbox_NOMBRE_CONTACT.get()
            TELEFONO = inbox_TELEFONO.get()
            DIRECCION = inbox_DIRECCION.get()
            contact_check = [NOMBRE_CONTACT, TELEFONO, DIRECCION]
            if contact_check == ['', '', '']:
                write_contacto()
            else:
                if NOMBRE_CONTACT == '':
                    NOMBRE_CONTACT = '<Default>'
                if TELEFONO == '':
                    TELEFONO = '<Default>'
                if DIRECCION == '':
                    DIRECCION = '<Default>'
                _guardar(NOMBRE_CONTACT, TELEFONO,DIRECCION)
                self.tree.insert("", 0, text = str(NOMBRE_CONTACT), values = (str(TELEFONO), str(DIRECCION)))
                self.tree.insert("", 0, text = "Nuevo nombre", values = ("nuevo telefono", "nueva direccion"))
            contact_check = []
            _limpiar_inbox()

        def buscar():
            answer = []
            var_buscar = str(combo.get())
            if var_buscar == 'NOMBRE_CONTACT':
                var_inbox = inbox_NOMBRE_CONTACT.get()
                posicion = 0
                answer = _buscar(var_inbox, posicion)
                _check(answer, var_buscar)
            elif var_buscar == 'TELEFONO':
                var_inbox = inbox_TELEFONO.get()
                posicion = 1
                answer = _buscar(var_inbox, posicion)
                _check(answer, var_buscar)
            else:
                var_inbox = inbox_DIRECCION.get()
                posicion = 2
                answer = _buscar(var_inbox, posicion)
                _check(answer, var_buscar)
            _limpiar_inbox()

            
        def show_contacto():
            _view_csv()



        def delete():
            NOMBRE_CONTACT = str(inbox_NOMBRE_CONTACT.get())
            a = delete_mesageBox(NOMBRE_CONTACT)
            if a == True:
                with open('agenda_tarea2.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('agenda_tarea2.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if NOMBRE_CONTACT != row[0]:
                            writer.writerow(row)
            limpiar()
            show_contacto()

        def limpiar():
            _limpiar_inbox()
            _limpiar_treeview()

# -------------------------  ----------------------------------------------