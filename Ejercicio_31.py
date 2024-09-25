palabra = input("Ingresa una palabra: ").lower()
if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
