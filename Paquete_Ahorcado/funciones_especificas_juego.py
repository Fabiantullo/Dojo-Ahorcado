from Paquete_Funciones.funciones_generales import *
import random


def procesar_letra(letra: str, palabra: str, letras_acertadas: list, letras_incorrectas: list, diccionario_juego: dict) -> bool:
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
    return letra not in letras_acertadas and letra not in letras_incorrectas

def generar_palabra_oculta(palabra:str)->list:
    palabra_oculta = []
    for i in range(len(palabra)):
        palabra_oculta.append("_")
    return palabra_oculta



