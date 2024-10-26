
def media_movil(lista, periodo):
    if periodo <= 0 or periodo > len(lista):
        return "Periodo no válido"
    medias_moviles = [
        sum(lista[i:i+periodo]) / periodo for i in range(len(lista) - periodo + 1)
    ]
    return medias_moviles

precios = [10, 12, 13, 15, 16, 18, 19, 20, 22]
print(media_movil(precios, 3))
