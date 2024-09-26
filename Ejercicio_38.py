numeros = input("Ingresa números separados por comas: ").split(',')
numeros = [int(num) for num in numeros]
numeros_unicos = list(set(numeros))
print(f"Lista sin duplicados: {numeros_unicos}")
