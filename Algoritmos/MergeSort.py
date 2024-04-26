#Funcion para llevar a cabo el algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) > 1: #se asegura de tener mas de un elemento
        mid = len(lista) // 2  #Aqui divide a la mitad mi lista
        I = lista[:mid] #sublista izquierda
        D = lista[mid:] #sublista derecha
        merge_sort(I) #aplica de manera recursiva mi funcion
        merge_sort(D)
        i = j = k = 0
        while i < len(I) and j < len(D): #Combina las sublistas ordenadas I y D
            if I[i] < D[j]:
                lista[k] = I[i]
                i += 1
            else:
                lista[k] = D[j]
                j += 1
            k += 1

        while i < len(I):
            lista[k] = I[i]
            i += 1
            k += 1

        while j < len(D):
            lista[k] = D[j]
            j += 1
            k += 1


lista = [12, 11, 13, 5, 6, 7] #Ejemplo de una lista desordenada
print("Lista original:\n", lista)
merge_sort(lista)  #Llama a la función para ordenar la lista
print("Lista ordenada:\n", lista)  #Imprime la lista ya ordenada