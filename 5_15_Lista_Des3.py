def eliminar_duplicados(lista):
    # Mostrar la lista original
    print("Lista original:", lista)
    # Crear una nueva lista sin duplicados usando set
    lista_sin_duplicados = list(set(lista))
    # Mostrar la lista sin duplicados
    print("Lista sin duplicados:", lista_sin_duplicados)

# uso
lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
eliminar_duplicados(lista)
