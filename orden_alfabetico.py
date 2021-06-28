import csv

# ----------------- Funcion que lee la base de datos en csv -----------------

def orden_alfabetico(): #-- definimos la funcion de orden alfabetico ---
    my_order = []
    my_row = []
    with open('agenda_tarea2.csv', 'r') as f: #--- abrimos la base de datos ---
        reader = csv.reader(f)  #--- leemos la base de datos ---
        for i, row in enumerate(reader): #---   se recorren los datos de la base de datos para hacer el orden --- 
            NOMBRE_CONTACT = str(row[0]) #--- la prioridad de el orden es alfabetico por lo tanto dejamos que ordene por nombres primero---
            TELEFONO = str(row[1]) #--- si hay dos nombres iguales entonces verifica el orden del numero de telefono ---
            DIRECCION = str(row[2]) #--- en algun caso hipotetico de tener mismo nombre y numero se ingresa la direccion por oden alfabetico ---
            my_row = [NOMBRE_CONTACT, TELEFONO, DIRECCION] #--- la fila de datos se imprime en este orden ---
            my_order.append(my_row)
    lista_ordenada = ordenamiento_por_mezcla(my_order)
    return lista_ordenada


def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[ : medio]
        derecha = lista[medio : ]
 
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        i = 0
        j = 0

        k = 0
 
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = derecha[j]
                j += 1
            else:
                lista[k] = izquierda[i]
                i += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha [j]
            j += 1
            k += 1

    return lista