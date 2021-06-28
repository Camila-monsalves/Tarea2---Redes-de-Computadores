import tkinter
import pandas as pd 
principal = tkinter.Tk()
principal.title('Agenda')

etiqueta1 = tkinter.Label(principal, text="INGRESE LOS DAROS DE REGISTRO")
marco1 = tkinter.Frame(principal, bd=8, relief="groove")

etiqueta2 = tkinter.Label(marco1, text="NOMBRE_CONTAC:")
marco2 = tkinter.Entry(marco1, width=18)

etiqueta3 = tkinter.Label(marco1, text="TELEFONO:")
marco3 = tkinter.Entry(marco1, width=18)

etiqueta4 = tkinter.Label(marco1, text="DIRECCIÓN:")
marco4 = tkinter.Entry(marco1, width=18)

enviar=tkinter.Button(marco1, text="AÑADIR")
borrar=tkinter.Button(marco1, text="ELIMINAR")
salir=tkinter.Button(marco1, text="SALIR")
etiqueta1.grid(row=0, column=1, pady=10)
marco1.grid(padx=10, pady=10, row=1, column=1)
etiqueta2.grid(row=0, column=0)
marco2.grid(row=0, column=1, padx=10)
etiqueta3.grid(row=1, column=0)
marco3.grid(row=1, column=1, padx=10 )
etiqueta4.grid(row=2, column=0)
marco4.grid(row=2, column=1, padx=10)


enviar.grid(row=7,column=2)
salir.grid(row=7, column=3)
borrar.grid(row=7,column=4)
principal.mainloop() 

