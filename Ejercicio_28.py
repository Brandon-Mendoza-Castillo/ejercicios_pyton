N = int(input("Ingresa un número entero positivo: "))
impares = [i for i in range(1, N + 1) if i % 2 != 0]
print(f"Los números impares hasta {N} son: {impares}")
