def mostrar_lista(lista: list) -> None:
    """
    Imprime los elementos de una lista en una sola línea, separados por un espacio.

    Args:
        lista (list): La lista de elementos a imprimir.

    Returns:
        None
    """
    for elemento in lista:
        print(elemento, end=" ")
    print("\n")
    
def limpiar_diccionario(diccionario: dict) -> None:
    """
    Elimina los elementos vacíos de un diccionario.

    Args:
        diccionario (dict): El diccionario a limpiar.
    """    
    for clave in diccionario:
        for item in diccionario[clave]:
            if item == "":
                diccionario[clave].remove(item)
                
def desea_continuar(mensaje, mensaje_error) -> bool:
    """
    Solicita al usuario una respuesta de si o no y valida la entrada.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario solicitando una respuesta.
        mensaje_error (str): El mensaje que se mostrara al usuario en caso de una entrada invalida.

    Returns:
        bool: True si la respuesta es "si" o "s", False si la respuesta es "no" o "n".
    """
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

def ingresar_letra(mensaje: str, mensaje_error: str) -> str:
    """
    Solicita al usuario que ingrese una letra y valida la entrada.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario solicitando la letra.
        mensaje_error (str): El mensaje de error que se mostrara si la entrada no es valida.

    Returns:
        str: Una letra valida ingresada por el usuario.
    """
    while True:
        letra = input(f"\n{mensaje}").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print(f"\n{mensaje_error}")
            
def verificar_letra_en_palabra(letra: str, palabra: str) -> bool:
    """
    Verifica si una letra se encuentra en una palabra.

    Args:
        letra (str): La letra que se desea verificar.
        palabra (str): La palabra en la que se desea verificar la letra.

    Returns:
        bool: True si la letra se encuentra en la palabra, False en caso contrario.
    """    
    return letra in palabra

def ingresar_nombre_usuario(mensaje: str, mensaje_error: str, minimo_len: int, maximo_len: int) -> str:
    """
    Solicita al usuario que ingrese su nombre y valida la entrada.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario solicitando el nombre.
        mensaje_error (str): El mensaje de error que se mostrara si la entrada no es valida.
        minimo_len (int): La longitud minima permitida para el nombre.
        maximo_len (int): La longitud maxima permitida para el nombre.

    Returns:
        str: Un nombre valido ingresado por el usuario.
    """    
    while True: 
        nombre = input(mensaje)
        if len(nombre) <= minimo_len or len(nombre) >= maximo_len:
            print(mensaje_error)
        else:
            return nombre