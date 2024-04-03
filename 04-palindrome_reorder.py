def palindrome_reorder(palabra):
    # Acá contamos las veces que aparece cada letra en la palabra
    contar_letras = {}    # variable que guarda las letras
    for letra in palabra:    # bucle que recorre la palabra para contar las letras
        contar_letras[letra] = contar_letras.get(letra, 0) + 1  # contamos las letras de la palabra y las guarda en la variable contar_letras 

    # Verificamos si se puede formar un palíndromo
    # Si hay más de una letra impar, no se puede formar un palíndromo
    # Si hay una letra impar, la guardamos para usarla en el centro del palíndromo
    # Si todas las letras son pares, no necesitamos una letra impar

    letra_impar = None  
    for letra, conteo in contar_letras.items():      
        if conteo % 2 == 1:     
            if letra_impar:  
                return "NO SOLUTION"
            letra_impar = letra

    # Se arma la primera mitad del palíndromo alfabéticamente
    primera_mitad_palindromo = ''
    for letra, conteo in contar_letras.items(): 
        primera_mitad_palindromo += letra * (conteo // 2) 

    # Se construye la segunda mitad del palíndromo en orden inverso a la primera mitad
    segunda_mitad_palindromo = ''
    for letra in reversed(primera_mitad_palindromo):
        segunda_mitad_palindromo += letra

    # Se forma el palíndromo completo con la letra impar en el centro si existe 
    palindromo = primera_mitad_palindromo + (letra_impar if letra_impar else '') + segunda_mitad_palindromo

    return palindromo

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print(palindrome_reorder("aabbc"))
