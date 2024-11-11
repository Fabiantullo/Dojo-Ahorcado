import re

def obtener_lista_palabras(path: str = "palabras.csv") -> list:
    """
    Obtiene una lista de palabras de un archivo csv.

    Args:
        path (str, optional): Path hacia el archivo csv. Defaults to "palabras.csv".

    Returns:
        list: Lista de palabras.
    """    
    lista = []

    with open(path, "r", encoding="utf-8") as archivo:
        archivo.readline().split(",")
        for linea in archivo:
            
            lectura = re.split(",|\n", linea)
        
            lista.append(lectura)
    return lista
 
def guardar_puntuacion(puntuacion: int, nombre: str) -> bool:
    """
    Guarda la puntuacion en un archivo csv.

    Args:
        puntuacion (int): Puntuacion final del jugador.
        nombre (str): Nombre del jugador.

    Returns:
        bool: True si la puntuacion se guardo correctamente, False en caso contrario.
    """    
    validacion = False
    from datetime import datetime
    fecha = datetime.now().strftime("%d/%m/%Y")
    with open("puntuaciones.csv", "a") as archivo:
        if archivo.tell() == 0:
            archivo.write("Nombre,Puntuacion,Fecha\n")
        archivo.write(f"{nombre},{puntuacion},{fecha}\n")
        validacion = True
    return validacion