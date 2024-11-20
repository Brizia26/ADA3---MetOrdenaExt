
def mezcla_directa(lista):
    n = len(lista)
    tamaño = 1  
  
    while tamaño < n:
        izquierda = 0  
        while izquierda < n:
            mitad = izquierda + tamaño
            derecha = min(izquierda + 2 * tamaño, n)
            if mitad < derecha:
                lista[izquierda:derecha] = merge(
                    lista[izquierda:mitad], lista[mitad:derecha]
                )
            izquierda += 2 * tamaño  
        tamaño *= 2  
    return lista

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

lista_desordenada = [28, 47, 93, 3, 2, 85, 12]
print("Lista original:", lista_desordenada)

lista_ordenada = mezcla_directa(lista_desordenada)
print("Lista ordenada:", lista_ordenada)