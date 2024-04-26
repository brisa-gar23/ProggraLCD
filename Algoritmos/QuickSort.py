def quicksort(lista):  #si la lista tiene longitud 0 o 1, ya está ordenada.
    if len(lista) <= 1:
        return lista
    else:
        piv = lista[0] #Elegimos el primer elemento de la lista como pivote.
#Dividimos la lista en dos partes: menores o iguales al pivote (less) y mayores que el pivote (great).
        less = []
        great = []
        for x in lista[1:]:
            if x <= piv:
                less.append(x)
            else:
                great.append(x)
        sorted_less = quicksort(less) #Se ordenan recursivamente las sublistas
        sorted_great = quicksort(great)
        return sorted_less + [piv] + sorted_great #Se combinan las sublistas ordenadas y el pivote

# Ejemplo de uso:
lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista original: \n\t", lista)
sorted_lista = quicksort(lista)
print("\nLista ordenada: \n\t", sorted_lista)