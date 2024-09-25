N = int(input("Ingresa un número entero positivo: "))
a, b = 0, 1
secuencia = []
for _ in range(N):
    secuencia.append(a)
    a, b = b, a + b
print(f"Los primeros {N} números de la secuencia de Fibonacci son: {secuencia}")
