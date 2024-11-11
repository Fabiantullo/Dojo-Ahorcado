def calcular_puntuacion_final(diccionario_juego:dict)->int:
    puntuacion_final = 0
    for i in range(len(diccionario_juego["puntuacion"])):
        puntuacion_final += diccionario_juego["puntuacion"][i]
    return puntuacion_final

def calcular_puntuacion_parcial(letras_acertadas: list, letras_incorrectas: list , diccionario_juego: dict) -> int:
    puntuacion = len(letras_acertadas) * 3 - len(letras_incorrectas)
    diccionario_juego["puntuacion"].append(puntuacion)
    return puntuacion

def manejar_ganancia(diccionario_juego: dict, letras_acertadas: list, letras_incorrectas: list) -> None:
    puntuacion_ganada = calcular_puntuacion_parcial(letras_acertadas, letras_incorrectas, diccionario_juego)
    diccionario_juego["intentos"] = 7
    print(f"¡Ganaste! Ganaste {puntuacion_ganada} puntos")
    letras_acertadas.clear()
    letras_incorrectas.clear()