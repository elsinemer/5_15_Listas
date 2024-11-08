# Pedir al usuario que ingrese tres números
numeros = []
for i in range(3):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Determinar el mayor o si todos son iguales
if numeros[0] == numeros[1] == numeros[2]:
    print("Todos los números son iguales.")
else:
    mayor = max(numeros)
    print(f"El número mayor es: {mayor}")
