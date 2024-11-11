from Paquete_Funciones.funciones_generales import *
import random


def procesar_letra(letra: str, palabra: str, letras_acertadas: list, letras_incorrectas: list, diccionario_juego: dict) -> bool:
    """
    Procesa la letra ingresada por el usuario y actualiza las listas de letras acertadas e incorrect

    Args:
        letra (str): Letra ingresada por el usuario.
        palabra (str): Palabra que se esta adivinando.
        letras_acertadas (list): Lista con las letras acertadas.
        letras_incorrectas (list): Lista con las letras incorrectas.
        diccionario_juego (dict): Diccionario que contiene el numero de intentos restantes bajo la clave "intentos".

    Returns:
        bool: True si la letra ingresada esta en la palabra, False en caso contrario.
    """    
    if verificar_letra_ya_ingresada(letra, letras_acertadas, letras_incorrectas):
        if verificar_letra_en_palabra(letra, palabra):
            letras_acertadas.append(letra)
            validacion = True
        else:
            letras_incorrectas.append(letra)
            diccionario_juego["intentos"] -= 1
            print(f"Te quedan {diccionario_juego['intentos']} intentos")
            validacion = False
            
    else:
        print("Ya ingresaste esa letra")
        validacion = False
    return validacion


def verificar_letra_ya_ingresada(letra: str, letras_acertadas: list, letras_incorrectas: list) -> bool:
    """
    Verifica si la letra ingresada ya fue ingresada anteriormente.

    Args:
        letra (str): Letra ingresada por el usuario.
        letras_acertadas (list): Lista con las letras acertadas.
        letras_incorrectas (list): Lista con las letras incorrectas.

    Returns:
        bool: True si la letra no fue ingresada anteriormente, False en caso contrario.
    """    
    return letra not in letras_acertadas and letra not in letras_incorrectas

def generar_palabra_oculta(palabra:str)->list:
    """
    Genera una lista con guiones bajos que representan la palabra oculta.

    Args:
        palabra (str): La palabra que se desea ocultar.

    Returns:
        list: Una lista con guiones bajos que representan la palabra oculta.
    """    
    palabra_oculta = []
    for i in range(len(palabra)):
        palabra_oculta.append("_")
    return palabra_oculta



