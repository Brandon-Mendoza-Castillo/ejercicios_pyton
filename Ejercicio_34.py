def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
mcd = calcular_mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es {mcd}.")
