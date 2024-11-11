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

def actualizar_palabra_oculta(letra: str, palabra: str, palabra_oculta: list)->list:
    for i in range(len(palabra_oculta)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta