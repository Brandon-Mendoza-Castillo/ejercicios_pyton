base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1
for _ in range(abs(exponente)):
    resultado *= base
if exponente < 0:
    resultado = 1 / resultado
print(f"{base}^{exponente} es {resultado}.")
