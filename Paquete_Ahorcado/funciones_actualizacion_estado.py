from Paquete_Ahorcado.funciones_calculo_puntaje import *
from Paquete_Funciones.funciones_archivo import *
from Paquete_Funciones.funciones_generales import *

def verificar_estado_ronda(palabra_oculta: list)->bool:
    """Verifica el estado de la ronda basado en la palabra oculta.

    Args:
        palabra_oculta (list): La palabra oculta que se está adivinando.

    Returns:
        bool: True si la palabra oculta no contiene guiones bajos, False en caso contrario.
    """    
    if "_" in palabra_oculta:
        valalidacion = False
    else:
        valalidacion = True
    return valalidacion

def verificar_estado_juego(diccionario_juego:dict, palabra: str, diccionario_palabras: dict)->bool:
    """
    Verifica el estado del juego basado en el número de intentos restantes.

    Args:
        diccionario_juego (dict): Un diccionario que contiene el estado actual del juego, 
                                  incluyendo el número de intentos restantes bajo la clave "intentos".

    Returns:
        bool: True si hay intentos restantes, False en caso contrario.
    """
    if diccionario_juego["intentos"] == 0:
        print("Te quedaste sin intentos")
        print(f"La palabra era: {palabra}")	
        validacion = False
    else:
        validacion = True
    if not diccionario_palabras:
        print("No hay mas palabras")
        validacion = False
    return validacion

def actualizar_palabra_oculta(letra: str, palabra: str, palabra_oculta: list)->list:
    """
    Actualiza la palabra oculta con la letra proporcionada.

    Args:
        letra (str): La letra que se ha adivinado.
        palabra (str): La palabra completa que se está adivinando.
        palabra_oculta (list): La representación actual de la palabra oculta, con letras adivinadas y guiones bajos.

    Returns:
        list: La palabra oculta actualizada con la letra adivinada en las posiciones correctas.
    """
    for i in range(len(palabra_oculta)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta

def finalizar_juego(diccionario_juego: dict) -> None:
    """
    Finaliza el juego guardando la puntuación final y el nombre del usuario.

    Args:
        diccionario_juego (dict): Un diccionario que contiene la puntuación final del juego bajo la clave "puntuacion".
    """    
    puntuacion = calcular_puntuacion_final(diccionario_juego)
    guardar_puntuacion(puntuacion, ingresar_nombre_usuario("Ingrese su nombre: ", "Ingrese un nombre valido", 2, 10))



