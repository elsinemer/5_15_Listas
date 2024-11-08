# Lista de códigos de productos en el inventario
inventario = ["A123", "B456", "C789", "D012", "E345"]

# Solicitar al usuario que introduzca un código de producto
codigo_producto = input("Introduce el código del producto: ")

# Buscar el código en la lista de inventario
if codigo_producto in inventario:
    posicion = inventario.index(codigo_producto)
    print(f"El código '{codigo_producto}' se encuentra en la posición {posicion}.")
else:
    print(f"El código '{codigo_producto}' no se ha encontrado en el inventario.")
