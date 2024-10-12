celsius = list(map(float, input("Ingresa las temperaturas en Celsius separadas por comas: ").split(',')))
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f"Temperaturas en Fahrenheit: {fahrenheit}")
