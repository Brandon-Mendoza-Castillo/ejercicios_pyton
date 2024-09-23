numeros = input("Ingresa números separados por comas: ").split(',')
numeros = [float(num) for num in numeros]
mayor = max(numeros)
menor = min(numeros)
print(f"El número mayor es {mayor} y el menor es {menor}.")
