import random
import re
from os import system as sys

def obtener_lista_palabras() -> list:
    lista = []

    with open("palabras.csv", "r", encoding="utf-8") as archivo:
        primera_linea = archivo.readline().split(",")
        for linea in archivo:
            
            lectura = re.split(",|\n", linea)
        
            lista.append(lectura)
    return lista
 
def normalizar_lista_en_diccionario(lista: list) -> dict:
    diccionario = {}
    for elemento in lista:
        key = elemento[0]
        if key not in diccionario:
            diccionario[key] = elemento[1:]
        else:
            diccionario[key].append(elemento[1])
    return diccionario

def jugar_ahorcado() -> None:
    # Arranca el juego
    lista_palabras = obtener_lista_palabras()
    diccionario_palabras = normalizar_lista_en_diccionario(lista_palabras)
    
    # Selecciona la categoría y la palabra
    palabra = seleccionar_categoria_y_palabra(diccionario_palabras)
    palabra_oculta = generar_palabra_oculta(palabra)

    diccionario_juego = {"intentos": 7, "puntuacion": []}
    letras_acertadas = []
    letras_incorrectas = []
    
    while verificar_estado_juego(diccionario_juego):
        mostrar_estado_juego(letras_acertadas, letras_incorrectas, palabra_oculta)
        letra = ingresar_letra("Ingrese una letra: ", "Ingrese una letra valida")
        
        if procesar_letra(letra, palabra, letras_acertadas, letras_incorrectas, diccionario_juego):
            palabra_oculta = actualizar_palabra_oculta(letra, palabra, palabra_oculta)
        
        if verificar_estado_ronda(palabra_oculta):
            manejar_ganancia(diccionario_juego, letras_acertadas, letras_incorrectas)
            palabra = seleccionar_categoria_y_palabra(diccionario_palabras)
            palabra_oculta = generar_palabra_oculta(palabra)
            if desea_continuar("¿Desea continuar? (si/no): ", "Ingrese una respuesta valida"):
                continue
            else:
                break
        sys("pause")
        sys("cls")
    finalizar_juego(diccionario_juego)
    print("\nGracias por jugar\n")
    input("Presione enter para salir")

def mostrar_estado_juego(letras_acertadas: list, letras_incorrectas: list, palabra_oculta: list) -> None:
    print(f"\nLetras acertadas: ")
    mostrar_lista(letras_acertadas)
    print(f"Letras incorrectas: ")
    mostrar_lista(letras_incorrectas)
    mostrar_palabra_oculta(palabra_oculta)

def mostrar_lista(lista: list) -> None:
    for elemento in lista:
        print(elemento, end=" ")
    print("\n")
def desea_continuar(mensaje, mensaje_error) -> bool:
    while True:
        respuesta = input(f"{mensaje}").lower()
        if respuesta == "si" or respuesta == "s":
            validacion = True
            break
        elif respuesta == "no" or respuesta == "n":
            validacion = False
            break
        else:
            print(f"{mensaje_error}")
    return validacion


def procesar_letra(letra: str, palabra: str, letras_acertadas: list, letras_incorrectas: list, diccionario_juego: dict) -> bool:
    if verificar_letra_ya_ingresada(letra, letras_acertadas, letras_incorrectas):
        if verificar_letra_en_palabra(letra, palabra):
            letras_acertadas.append(letra)
            return True
        else:
            letras_incorrectas.append(letra)
            diccionario_juego["intentos"] -= 1
            print(f"Te quedan {diccionario_juego['intentos']} intentos")
    else:
        print("Ya ingresaste esa letra")
    return False

def manejar_ganancia(diccionario_juego: dict, letras_acertadas: list, letras_incorrectas: list) -> None:
    puntuacion_ganada = calcular_puntuacion_parcial(letras_acertadas, letras_incorrectas, diccionario_juego)
    diccionario_juego["intentos"] = 7
    print(f"¡Ganaste! Ganaste {puntuacion_ganada} puntos")
    letras_acertadas.clear()
    letras_incorrectas.clear()

def seleccionar_categoria_y_palabra(diccionario_palabras: dict) -> tuple:
    lista_categorias = ["Programación", "Videojuegos", "Historia", "Deportes"]
    categoria = seleccionar_categoria(lista_categorias)
    palabra = seleccionar_palabra(diccionario_palabras, categoria).lower()
    return palabra

def finalizar_juego(diccionario_juego) -> None:
    puntuacion = calcular_puntuacion_final(diccionario_juego)
    guardar_puntuacion(puntuacion, ingresar_nombre_usuario("Ingrese su nombre: ", "Ingrese un nombre valido", 2, 10))

def ingresar_letra(mensaje: str, mensaje_error: str) -> str:
    while True:
        letra = input(f"\n{mensaje}").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print(f"\n{mensaje_error}")

def verificar_letra_en_palabra(letra: str, palabra: str) -> bool:
    return letra in palabra

def verificar_letra_ya_ingresada(letra: str, letras_acertadas: list, letras_incorrectas: list) -> bool:
    return letra not in letras_acertadas and letra not in letras_incorrectas

def calcular_puntuacion_parcial(letras_acertadas: list, letras_incorrectas: list , diccionario_juego: dict) -> int:
    puntuacion = len(letras_acertadas) * 3 - len(letras_incorrectas)
    diccionario_juego["puntuacion"].append(puntuacion)
    return puntuacion

def seleccionar_categoria(lista) -> str:
    return random.choice(lista)

def seleccionar_palabra(lista, categoria) -> str:
    return random.choice(lista[categoria])

def guardar_puntuacion(puntuacion, nombre) -> bool:
    from datetime import datetime
    fecha = datetime.now().strftime("%d/%m/%Y")
    with open("puntuaciones.csv", "a") as archivo:
        if archivo.tell() == 0:
            archivo.write("Nombre,Puntuacion,Fecha\n")
        archivo.write(f"{nombre},{puntuacion},{fecha}\n")

def ingresar_nombre_usuario(mensaje: str, mensaje_error: str, minimo_len: int, maximo_len: int) -> str:
    while True: 
        nombre = input(mensaje)
        if len(nombre) <= minimo_len or len(nombre) >= maximo_len:
            print(mensaje_error)
        else:
            return nombre
        

def verificar_estado_ronda(palabra_oculta: list)->bool:
    if "_" in palabra_oculta:
        valalidacion = False
    else:
        valalidacion = True
    return valalidacion

def verificar_estado_juego(diccionario_juego:dict)->bool:
    if diccionario_juego["intentos"] == 0:
        validacion = False
    else:
        validacion = True
    return validacion

def generar_palabra_oculta(palabra:str)->list:
    palabra_oculta = []
    for i in range(len(palabra)):
        palabra_oculta.append("_")
    return palabra_oculta

def mostrar_palabra_oculta(palabra_oculta: list):
    for i in range(len(palabra_oculta)):
        print(palabra_oculta[i], end=" ")

def actualizar_palabra_oculta(letra: str, palabra: str, palabra_oculta: list)->list:
    for i in range(len(palabra_oculta)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta

def calcular_puntuacion_final(diccionario_juego:dict)->int:
    puntuacion_final = 0
    for i in range(len(diccionario_juego["puntuacion"])):
        puntuacion_final += diccionario_juego["puntuacion"][i]
    return puntuacion_final


#! No encuentro para que se utiliza
def obtener_elemento_aleatorio(lista_elementos:list)->any:
    pass

jugar_ahorcado()