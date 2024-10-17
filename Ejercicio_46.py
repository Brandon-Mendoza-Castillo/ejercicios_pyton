lista1 = list(map(int, input("Ingresa la primera lista de números separados por comas: ").split(',')))
lista2 = list(map(int, input("Ingresa la segunda lista de números separados por comas: ").split(',')))

if len(lista1) == len(lista2):
    lista_suma = [a + b for a, b in zip(lista1, lista2)]
    print(f"La lista resultante es: {lista_suma}")
else:
    print("Las listas deben tener el mismo tamaño.")
