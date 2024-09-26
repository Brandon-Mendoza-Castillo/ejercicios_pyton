N = int(input("Ingresa un número entero positivo: "))
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
