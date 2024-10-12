numeros = list(map(int, input("Ingresa una lista de números separados por comas: ").split(',')))
unico = list(set(numeros))
unico.sort()
if len(unico) > 1:
    print(f"El segundo número más grande es {unico[-2]}")
else:
    print("No hay suficiente diversidad de números para encontrar el segundo más grande.")
