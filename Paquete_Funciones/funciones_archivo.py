import re

def obtener_lista_palabras() -> list:
    lista = []

    with open("palabras.csv", "r", encoding="utf-8") as archivo:
        archivo.readline().split(",")
        for linea in archivo:
            
            lectura = re.split(",|\n", linea)
        
            lista.append(lectura)
    return lista
 
def guardar_puntuacion(puntuacion, nombre) -> bool:
    from datetime import datetime
    fecha = datetime.now().strftime("%d/%m/%Y")
    with open("puntuaciones.csv", "a") as archivo:
        if archivo.tell() == 0:
            archivo.write("Nombre,Puntuacion,Fecha\n")
        archivo.write(f"{nombre},{puntuacion},{fecha}\n")