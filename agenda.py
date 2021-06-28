from tkinter import * #--- importamos la libreria tkinter para la interfaz de la agenda --- 
import index #--- importamos index donde está el código completo de la agenda ---

def main():
    root = Tk()
    root.title('Agenda') #--- Titulo que se da a la ventana principal ---
    root.configure 
    root.geometry("+250+80")
    root.resizable(0,0)
    index.App(root) 
    root.mainloop()

if __name__ == "__main__":
    main()
    

if __name__ == "__main__":
    main()
    