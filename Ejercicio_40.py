N = int(input("Ingresa un número entero positivo: "))
suma_cuadrados = sum(i**2 for i in range(1, N + 1))
print(f"La suma de los cuadrados de los primeros {N} números es {suma_cuadrados}.")
