def number_spiral(fila, columna):
   max_valor = max(fila, columna)  # máximo valor de la fila y columna
   min_valor = min(fila, columna)  # mínimo valor de la fila y columna
   area = (max_valor - 1) ** 2     # área cuadrada del espiral
   if max_valor % 2 == fila % 2:    
       incremento = min_valor    # si el max_valor es par, el incremento es el min_valor.
   else:
       incremento = max_valor * 2 - min_valor  # si el max_valor es impar, el incremento es el max_valor por 2, menos el min_valor
   return area + incremento                    # se retorna el área más el incremento

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
print(number_spiral(2, 2))





