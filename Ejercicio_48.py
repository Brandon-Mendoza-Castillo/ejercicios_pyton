peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / estatura**2
print(f"Tu índice de masa corporal es {imc:.2f}.")
