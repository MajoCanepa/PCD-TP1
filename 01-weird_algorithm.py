def weird_algorithm(num):  # Función que recibe un número
    def es_par(num):       # Función para saber si un número es par
        return num % 2 == 0   # Si el residuo de la división de num entre 2 es 0, entonces es par

    resultado = [num]      # Guardamos los resultados en una lista

    while num !=1:
        if es_par(num):
            num = num // 2  # Si es par, se divide por 2
        else:
            num = (3 * num) + 1   # Si no es par, se multiplica por 3 y se le suma 1
        resultado.append(num)  # Agregamos a la lista el resultado
        
    return resultado       # Acá tenemos la lista con los reultados 

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print(weird_algorithm(3))



