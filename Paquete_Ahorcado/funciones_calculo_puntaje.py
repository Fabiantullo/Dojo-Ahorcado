def calcular_puntuacion_final(diccionario_juego:dict)->int:
    """
    Calcula la puntuacion a traves de la suma de las puntuaciones parciales.

    Args:
        diccionario_juego (dict): Un diccionario que contiene la puntuacion de cada ronda bajo la clave "puntuacion".

    Returns:
        int: La puntuacion final del juego.
    """    
    puntuacion_final = 0
    for i in range(len(diccionario_juego["puntuacion"])):
        puntuacion_final += diccionario_juego["puntuacion"][i]
    return puntuacion_final

def calcular_puntuacion_parcial(letras_acertadas: list, letras_incorrectas: list , diccionario_juego: dict) -> int:
    """
    Calcula la puntuacion de la ronda actual.

    Args:
        letras_acertadas (list): Lista que contiene las letras acertadas.
        letras_incorrectas (list): Lista que contiene las letras incorrectas.
        diccionario_juego (dict): Un diccionario que contiene la puntuacion de cada ronda bajo la clave "puntuacion".

    Returns:
        int: La puntuacion de la ronda actual.
    """    
    puntuacion = len(letras_acertadas) * 3 - len(letras_incorrectas)
    diccionario_juego["puntuacion"].append(puntuacion)
    return puntuacion

def manejar_ganancia(diccionario_juego: dict, letras_acertadas: list, letras_incorrectas: list) -> None:
    """
    Maneja la ganancia del jugador, mostrando la puntuacion ganada y reiniciando las listas de letras acertadas e incorrectas.

    Args:
        diccionario_juego (dict): Un diccionario que contiene los intentos de cada ronda bajo la clave "intentos".
        letras_acertadas (list): Lista que contiene las letras acertadas.
        letras_incorrectas (list): Lista que contiene las letras incorrectas.
    """    
    puntuacion_ganada = calcular_puntuacion_parcial(letras_acertadas, letras_incorrectas, diccionario_juego)
    diccionario_juego["intentos"] = 7
    print(f"¡Ganaste! Ganaste {puntuacion_ganada} puntos")
    letras_acertadas.clear()
    letras_incorrectas.clear()