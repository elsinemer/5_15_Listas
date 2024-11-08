def sumar_listas(lista1, lista2):
    # Encontrar la longitud máxima entre ambas listas
    longitud_max = max(len(lista1), len(lista2))
    
    # Extender ambas listas con ceros para igualar su longitud
    lista1.extend([0] * (longitud_max - len(lista1)))
    lista2.extend([0] * (longitud_max - len(lista2)))
    
    # Sumar los elementos en posiciones correspondientes
    resultado = [lista1[i] + lista2[i] for i in range(longitud_max)]
    
    return resultado

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5]
resultado = sumar_listas(lista1, lista2)
print(resultado)
