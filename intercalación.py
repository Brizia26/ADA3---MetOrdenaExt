
def merge_sort(lista):
    if len(lista) <= 1:  
        return lista

   
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)


    return merge(izquierda, derecha)


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

lista_desordenada = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista_desordenada)

lista_ordenada = merge_sort(lista_desordenada)
print("Lista ordenada:", lista_ordenada)



