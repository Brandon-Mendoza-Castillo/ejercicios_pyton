numeros = []
while True:
    numero = float(input("Ingresa un número (negativo para terminar): "))
    if numero < 0:
        break
    numeros.append(numero)
if numeros:
    promedio = sum(numeros) / len(numeros)
    print(f"El promedio de los números ingresados es {promedio}.")
else:
    print("No se ingresaron números.")
