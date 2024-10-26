
import random
from collections import Counter

def simular_dados(lanzamientos=1000):
    resultados = [random.randint(1, 6) + random.randint(1, 6) for _ in range(lanzamientos)]
    frecuencia = Counter(resultados)
    return frecuencia

print(simular_dados())
