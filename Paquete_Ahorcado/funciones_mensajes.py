from Paquete_Funciones.funciones_generales import mostrar_lista
def mostrar_estado_juego(letras_acertadas: list, letras_incorrectas: list, palabra_oculta: list) -> None:
    print(f"\nLetras acertadas: ")
    mostrar_lista(letras_acertadas)
    print(f"Letras incorrectas: ")
    mostrar_lista(letras_incorrectas)
    mostrar_lista(palabra_oculta)