
def contar_palabras_unicas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read().lower()
        palabras = set(texto.split())
        return len(palabras)

print(contar_palabras_unicas('mi_archivo.txt'))
