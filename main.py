#region Importaciones
from Paquete_Funciones.funciones_normalizacion import *
from Paquete_Ahorcado.funciones_especificas_juego import *
from Paquete_Ahorcado.funciones_inicio_ronda import *
from Paquete_Ahorcado.funciones_mensajes import *
from Paquete_Ahorcado.funciones_actualizacion_estado import *
from Paquete_Ahorcado.funciones_calculo_puntaje import *
from os import system as sys
#endregion

def jugar_ahorcado() -> None:
    # Arranca el juego
    lista_palabras = obtener_lista_palabras()
    diccionario_palabras = normalizar_lista_en_diccionario(lista_palabras)
    limpiar_diccionario(diccionario_palabras)
    
    # Selecciona la categoría y la palabra
    palabra = seleccionar_categoria_y_palabra(diccionario_palabras)
    palabra_oculta = generar_palabra_oculta(palabra)

    diccionario_juego = {"intentos": 7, "puntuacion": []}
    letras_acertadas = []
    letras_incorrectas = []
    
    while verificar_estado_juego(diccionario_juego, palabra, diccionario_palabras):
        mostrar_estado_juego(letras_acertadas, letras_incorrectas, palabra_oculta)
        letra = ingresar_letra("Ingrese una letra: ", "Ingrese una letra valida")
        sys("cls")
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
        
        
        mostrar_estado_juego(letras_acertadas, letras_incorrectas, palabra_oculta)
            
        sys("pause")
        sys("cls")
    finalizar_juego(diccionario_juego)
    print("\nGracias por jugar\n")
    input("Presione enter para salir")

#! No encuentro para que se utiliza
# def obtener_elemento_aleatorio(lista_elementos:list)->any:
#     pass

jugar_ahorcado()