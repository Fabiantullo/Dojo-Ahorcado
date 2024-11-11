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

def ingresar_letra(mensaje: str, mensaje_error: str) -> str:
    while True:
        letra = input(f"\n{mensaje}").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print(f"\n{mensaje_error}")
            
def verificar_letra_en_palabra(letra: str, palabra: str) -> bool:
    return letra in palabra

def ingresar_nombre_usuario(mensaje: str, mensaje_error: str, minimo_len: int, maximo_len: int) -> str:
    while True: 
        nombre = input(mensaje)
        if len(nombre) <= minimo_len or len(nombre) >= maximo_len:
            print(mensaje_error)
        else:
            return nombre