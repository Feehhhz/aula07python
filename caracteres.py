def transformar_maiusculo(texto):
    return texto.upper()

def transformar_minusculo(texto):
    return texto.lower()

def contar_consoantes(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "bcdfghjklmnpqrstvxywz":
            contador += 1
    return contador