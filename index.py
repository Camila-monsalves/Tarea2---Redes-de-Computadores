from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import orden_alfabetico
import csv

# -------------------------- Funciones globales ------------------------------------------

# -----------  ---------------------------------------
def no_found(var):
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
        search = MessageBox.askquestion("Delete alert","¿Desea eliminar contacto\n" + var_NOMBRE_CONTACT)
        if search == "yes":
            return True
        else:
            return False

def modify_mesageBox(contacto):
    var_NOMBRE_CONTACT = str(contacto[0])
    var_TELEFONO = str(contacto[1])
    var_DIRECCION = str(contacto[2])
    search = MessageBox.askquestion("Modify Alert","¿Desea modificar los datos?\n" + " NOMBRE:" + var_NOMBRE_CONTACT )
    if search == "yes":
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
        
        
        # ---------------- Ventana del menu-----------------
       
        
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
        ingresar_button = Button(inbox_frame, command = lambda: add(), text = 'Ingrese un contacto', width = 20)
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
        save_changes_button = Button(inbox_frame, command = lambda: clean(), text = 'Limpiar vista', width = 20)
        save_changes_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        save_changes_button.grid(row = 16, column = 0, padx = 2, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--

        # -------------- Menu de opciones para busqueda ----------------
        search_button = Button(inbox_frame, command = lambda: search(), text = 'Buscar contacto por:', width = 20)
        search_button.configure(cursor = 'hand2', font = ("Calibri", "10", "normal"))
        search_button.grid(row = 18, column = 0, padx = 3, pady = 3, sticky = W + E) #-- da las coordenadas de ubicación del boton--
          
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

        #Scroll
        scrollVert = Scrollbar(three_frame, command = self.tree.yview)
        self.tree.configure(yscrollcommand = scrollVert.set)
        scrollVert.grid(row = 0, column = 1, sticky = "nsew")

        scroll_x = Scrollbar(three_frame, command = self.tree.xview, orient = HORIZONTAL)
        self.tree.configure(xscrollcommand = scroll_x.set)
        scroll_x.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew")

# --------------------------  -----------------------------

        # --------------- funciones auxiliares ------------------
        def _clean_inbox():
            # 
            inbox_NOMBRE_CONTACT.delete(0, 'end')
            inbox_TELEFONO.delete(0, 'end')
            inbox_DIRECCION.delete(0, 'end')

        def _clean_treeview():
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

        def _save(NOMBRE_CONTACT, TELEFONO, DIRECCION):
            s_NOMBRE_CONTACT = NOMBRE_CONTACT
            s_TELEFONO = TELEFONO
            s_DIRECCION = DIRECCION
            with open('agenda_tarea2.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                writer.writerow( (s_NOMBRE_CONTACT, s_TELEFONO,s_DIRECCION) )

        def _search(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('agenda_tarea2.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if list_answer == []:
                no_found(var_search)
            else:
                NOMBRE_CONTACT = str(list_answer[0])
                TELEFONO = str(list_answer[1])
                DIRECCION = str(list_answer[2])
                self.tree.insert("", 0, text = NOMBRE_CONTACT, values = (TELEFONO, DIRECCION))
                self.tree.insert("", 0, text = "Search result of name", values = ("Search result of phone", "Search result of email"))
         

        def _check_1(answer,var_search):
            val_modify = answer
            var = var_search
            if val_modify == []:
                no_found(var)
            else:
                TopLevelModify(self.window, val_modify)

        # ----------------- Funciones de cada boton ------------------
        def add():
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
                _save(NOMBRE_CONTACT, TELEFONO,DIRECCION)
                self.tree.insert("", 0, text = str(NOMBRE_CONTACT), values = (str(TELEFONO), str(DIRECCION)))
                self.tree.insert("", 0, text = "Nuevo nombre", values = ("nuevo telefono", "nueva direccion"))
            contact_check = []
            _clean_inbox()

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'NOMBRE_CONTACT':
                var_inbox = inbox_NOMBRE_CONTACT.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            elif var_search == 'TELEFONO':
                var_inbox = inbox_TELEFONO.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            else:
                var_inbox = inbox_DIRECCION.get()
                possition = 2
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            _clean_inbox()

            
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
            clean()
            show_contacto()

        def clean():
            _clean_inbox()
            _clean_treeview()

# -------------------------  ----------------------------------------------

class TopLevelModify():
    def __init__(self, root, val_modify):
        self.root_window = root
        self.val_modify = val_modify
        self.NOMBRE_CONTACT = str(self.val_modify[0])
        self.TELEFONO = str(self.val_modify[1])
        self.DIRECCION = str(self.val_modify[2])

        window_modify = Toplevel(self.root_window)
        window_modify.title("Modify Contact")
        window_modify.configure(bg = "#53CDB8")
        window_modify.geometry("+1000+100")
        window_modify.resizable(0,0)

        # ---------------- -----------------
        text_frame = LabelFrame(window_modify)
        text_frame.grid(row = 0, column = 0)

        inbox_frame = LabelFrame(window_modify)
        inbox_frame.grid(row = 2, column = 0)

         # ---------------  -----------------
        Label(text_frame, text = self.NOMBRE_CONTACT, font = ("Calibri", "11", "bold")).grid(row = 1, column = 0)
        Label(text_frame, text = self.TELEFONO, font = ("Calibri", "11", "bold")).grid(row = 1, column = 1)
        Label(text_frame, text = self.DIRECCION, font = ("Calibri", "11", "bold")).grid(row = 1, column = 2)
        
        # ---------------  ------------------
        Label(text_frame, text = 'Write a new Name', font = ("Calibri", "11", "normal")).grid(row = 2, column = 0)
        n_inbox_NOMBRE_CONTACT = Entry(text_frame, font = ("Calibri", "11", "normal"), width = 28)
        n_inbox_NOMBRE_CONTACT.grid(row = 3, column = 0)
        n_inbox_NOMBRE_CONTACT.focus()

        Label(text_frame, text = 'Write a new Phone', font = ("Calibri", "11", "normal")).grid(row = 2, column = 1)
        n_inbox_TELEFONO = Entry(text_frame, font = ("Calibri", "11", "normal"), width = 20)
        n_inbox_TELEFONO.grid(row = 3, column = 1)

        Label(text_frame, text = 'Write a new Email', font = ("Calibri", "11", "normal")).grid(row = 2, column = 2)
        n_inbox_DIRECCION = Entry(text_frame, font = ("Calibri", "11", "normal"), width = 30)
        n_inbox_DIRECCION.grid(row = 3, column = 2)

        # ---------------  -----------------
        yes_button = Button(inbox_frame, command = lambda: yes(), text = 'Yes', width = 20)
        yes_button.configure(bg = "#F26262", cursor = 'hand2', font = ("Calibri", "10", "normal"))
        yes_button.grid(row = 1, column = 0, padx = 2, pady = 3, sticky = W + E)

        no_button = Button(inbox_frame, command = window_modify.destroy, text = 'No', width = 20, bg = "yellow", cursor = 'hand2')
        no_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Calibri", "10", "normal"))
        no_button.grid(row = 1, column = 1, padx = 2, pady = 3, sticky = W + E)

        cancel_button = Button(inbox_frame, command = window_modify.destroy, text = 'Cancel', width = 20, bg = "green", cursor = 'hand2')
        cancel_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Calibri", "10", "normal"))
        cancel_button.grid(row = 1, column = 2, padx = 2, pady = 3, sticky = W + E)

        # -----------------  ------------------
        def yes():
            contacto = self.val_modify
            new_NOMBRE_CONTACT = n_inbox_NOMBRE_CONTACT.get()
            new_TELEFONO = n_inbox_TELEFONO.get()
            new_DIRECCION = n_inbox_DIRECCION.get()
            a = modify_mesageBox(contacto)
            if a == True:
                _del_old(contacto[0])
                _add_new(new_NOMBRE_CONTACT, new_TELEFONO, new_DIRECCION)
            window_modify.destroy()

        def _add_new(NOMBRE_CONTACT, TELEFONO, DIRECCION):
            s_NOMBRE_CONTACT = NOMBRE_CONTACT
            s_TELEFONO = TELEFONO
            s_DIRECCION = DIRECCION
            with open('agenda_tarea2.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                writer.writerow( (s_NOMBRE_CONTACT, s_TELEFONO, s_DIRECCION) )

        def _del_old(old_NOMBRE_CONTACT):
            NOMBRE_CONTACT = old_NOMBRE_CONTACT
            with open('agenda_tarea2.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('agenda_tarea2.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if NOMBRE_CONTACT != row[0]:
                        writer.writerow(row)