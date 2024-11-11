def normalizar_lista_en_diccionario(lista: list) -> dict:
    diccionario = {}
    for elemento in lista:
        key = elemento[0]
        if key not in diccionario:
            diccionario[key] = elemento[1:]
        else:
            diccionario[key].append(elemento[1])
    return diccionario

