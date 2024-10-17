cadena1 = input("Ingresa la primera cadena: ").replace(" ", "").lower()
cadena2 = input("Ingresa la segunda cadena: ").replace(" ", "").lower()

if sorted(cadena1) == sorted(cadena2):
    print("Las cadenas son anagramas.")
else:
    print("Las cadenas no son anagramas.")
