#Funcion para la creacion de un algoritmo bubblesort
def bubble_sort(list):
    x = len(lista) #len es para ver el tamaño de mi lista
    for i in range(x):
        for j in range(0, x-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

#Ejemplo de lista
lista = [i for i in range(1000, 0, -1)]
print("Lista original:\n", lista)
bubble_sort(lista)
print("\nLista ordenada:")
print(lista)