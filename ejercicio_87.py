
def clasificar_estudiantes(estudiantes, nota_corte=60):
    clasificacion = {'Aprobado': [], 'Reprobado': []}
    for nombre, nota in estudiantes.items():
        if nota >= nota_corte:
            clasificacion['Aprobado'].append(nombre)
        else:
            clasificacion['Reprobado'].append(nombre)
    return clasificacion

estudiantes = {'Ana': 85, 'Juan': 58, 'Pedro': 90, 'María': 70, 'Luis': 40}
print(clasificar_estudiantes(estudiantes))
