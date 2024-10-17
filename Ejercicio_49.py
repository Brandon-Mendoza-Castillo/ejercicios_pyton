import random
N = int(input("Ingresa el número de elementos de la lista: "))
lista_aleatoria = [random.randint(1, 100) for _ in range(N)]
print(f"Lista de números aleatorios: {lista_aleatoria}")
