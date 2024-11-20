
def mezcla_equilibrada(lista):
    import math

    bloques = [[x] for x in lista]  

    while len(bloques) > 1:
        nuevos_bloques = []
        for i in range(0, len(bloques), 2):
            if i + 1 < len(bloques):
                nuevo_bloque = merge(bloques[i], bloques[i + 1])
            else:
                nuevo_bloque = bloques[i]
            nuevos_bloques.append(nuevo_bloque)
        bloques = nuevos_bloques  
    return bloques[0] if bloques else []

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

lista_desordenada = [28, 17, 43, 6, 2, 35, 66]
print("Lista original:", lista_desordenada)

lista_ordenada = mezcla_equilibrada(lista_desordenada)
print("Lista ordenada:", lista_ordenada)


