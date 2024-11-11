import random
def seleccionar_categoria(lista) -> str:
    return random.choice(lista)

def seleccionar_palabra(lista, categoria) -> str:
    return random.choice(lista[categoria])

def seleccionar_categoria_y_palabra(diccionario_palabras: dict) -> tuple:
    lista_categorias = ["Programación", "Videojuegos", "Historia", "Deportes"]
    categoria = seleccionar_categoria(lista_categorias)
    palabra = seleccionar_palabra(diccionario_palabras, categoria).lower()
    return palabra
