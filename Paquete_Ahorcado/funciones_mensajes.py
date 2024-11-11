from Paquete_Funciones.funciones_generales import mostrar_lista
def mostrar_estado_juego(letras_acertadas: list, letras_incorrectas: list, palabra_oculta:list) -> None:
    """
    Muestra el estado del juego, incluyendo las letras acertadas, las letras incorrectas y la palabra oculta.

    Args:
        letras_acertadas (list): Lista con las letras acertadas.
        letras_incorrectas (list): Lista con las letras incorrectas.
        palabra_oculta (list): Lista con la palabra oculta.
    """    
    print(f"\nLetras acertadas: ")
    mostrar_lista(letras_acertadas)
    print(f"Letras incorrectas: ")
    mostrar_lista(letras_incorrectas)
    mostrar_lista(palabra_oculta)