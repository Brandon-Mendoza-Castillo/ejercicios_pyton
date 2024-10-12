frase = input("Ingresa una frase: ")
palabras = frase.split()
print(f"Número de palabras: {len(palabras)}")
for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {len(palabra)} caracteres.")
