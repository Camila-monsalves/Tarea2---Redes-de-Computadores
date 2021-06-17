print("Bienvenido");
import pandas as pd

''' agenda = pd.DataFrame({
    "Nombre":["Vania","Camila","Luis"],
    "Teléfono":[133,132,131],
    "Dirección":["Calle falsa 123","Hualpen","San Pedro"]

}
) '''

agenda = pd.read_csv("agenda_tarea2.csv", sep = ';')
print(agenda)