def normalizar_lista_en_diccionario(lista: list) -> dict:
    """
    Normaliza una lista en un diccionario.

    Args:
        lista (list): Lista de elementos.

    Returns:
        dict: Un diccionario con los elementos de la lista.
    """    
    diccionario = {}
    for elemento in lista:
        key = elemento[0]
        if key not in diccionario:
            diccionario[key] = elemento[1:]
        else:
            diccionario[key].append(elemento[1])
    return diccionario

