def encontrar_numero(n, arr):
    suma = (n * (n + 1)) // 2   # Sumamos todos los números del 1 al n, y se guarda en la variable suma
    return suma - sum(arr)      # Restamos la suma de los números en el arreglo, y se retorna el resultado, que seria el número que falta


assert encontrar_numero(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print(encontrar_numero(5, [1, 2, 4, 5]))








