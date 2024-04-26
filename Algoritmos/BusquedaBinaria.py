def busqueda_binaria(lista, num):
    izq = 0 #Inicializamos los índices izquierdo y derecho del segmento de la lista
    der = len(lista) - 1
    while izq <= der: #Mientras que sea menor o igual,continuamos con la búsqueda.
        mid = (izq + der) // 2 #Calculamos el índice medio
        if lista[mid] == num:  #Comparamos el elemento medio con el objetivo
            return mid 
        elif lista[mid] < num: #Si el elemento medio es menor que el objetivo, ajustamos el índice izquierdo.
            izq = mid + 1 
        else:  #De lo contrario, ajustamos el índice derecho.
            der = mid - 1
# Si llegamos aquí, el objetivo no está presente en la lista.
    return -1

# Ejemplo
lista = [x for x in range(150,420, 10)]
num = 160
res = busqueda_binaria(lista, num)
if res != -1: #bandera para saber si está o no
    print("El numero deseado", num, "está en la posición", res)
else:
    print("El numero", num, "no se encuentra en la lista")