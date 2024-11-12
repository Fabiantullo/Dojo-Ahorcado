import random
def seleccionar_categoria(lista: list) -> str:
    """
    Selecciona una categoria al azar de una lista de categorias.

    Args:
        lista (list): Lista de categorias.

    Returns:
        str: La categoria
    """    
    return random.choice(lista) 

def seleccionar_palabra(lista: list|dict, categoria: str) -> str:
    """
    Selecciona una palabra al azar de una lista de palabras.

    Args:
        lista (list): Lista de palabras.
        categoria (str): La categoria de la palabra.

    Returns:
        str: La palabra
    """    
    salida = random.choice(lista[categoria])
    if lista[categoria] == []:
        lista.pop(categoria)
    else:
        lista[categoria].remove(salida)
    return salida

def seleccionar_categoria_y_palabra(diccionario_palabras: dict) -> str:
    """
    Selecciona una categoria y una palabra al azar de un diccionario de palabras.

    Args:
        diccionario_palabras (dict): Un diccionario que contiene las palabras agrupadas por categorias.

    Returns:
        str: La palabra
    """    
    lista_categorias = ["Programación", "Videojuegos", "Historia", "Deportes"]
    categoria = seleccionar_categoria(lista_categorias)
    palabra = (seleccionar_palabra(diccionario_palabras, categoria)).lower()
    return palabra
