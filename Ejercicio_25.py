frase = input("Ingresa una frase: ").lower()
letra = input("Ingresa una letra para contar: ").lower()
ocurrencias = frase.count(letra)
print(f"La letra '{letra}' aparece {ocurrencias} veces en la frase.")
