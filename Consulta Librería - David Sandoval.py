# Con NumPy puedes crear, transformar, calcular y resolver casi todo lo que tenga que ver con vectores y matrices.
# 
# En la universidad se efectuó la elección del representante de los estudiantes ante el Consejo Superior. 
# Se presentaron 30 candidatos y cada uno se identificó con un número del 1 al 30. 
# Asumiendo que los 5000 estudiantes de la universidad votaron, 
# elabore un programa donde imprima un listado de mayor a menor, 
# según el número de votos obtenidos por cada candidato
# 
# #
import numpy as np

print("Parte número 1: ")

candidatos = 30
num_votos = 5000

votos = np.random.randint(1, candidatos + 1, size=num_votos)

# Genera num_votos (5000) números aleatorios entre 1 y candidatos (30) (incluyendo ambos (esto gracias al +1 en parte del candidatos + 1)). 
# Simula q cada estudiante de su voto y se guarda mas o menos asi en el array = [23, 12, 22, 21, 6 .....] hasta 500 votos q hubo

conteo = np.bincount(votos, minlength=candidatos + 1)[1:]

# np.bincount(votos) → cuenta cuántas veces aparece cada número en el array votos.
# minlength=candidatos+1 → garantiza que tengamos posiciones para los 30 candidatos.
# como un asegúrate de que el resultado tenga al menos candidatos + 1 posiciones”.

# [1:] → descartamos la posición 0 (porque no hay candidato con número 0). Como un desde 1 en adelante

# Basicamente hace la cuenta de la cantidad de veces q aparece un número que representa el candidato;

orden = np.argsort(conteo)[::-1]

# np.argsort(conteo) devuelve los índices ordenados de menor a mayor según los votos.
#devuelve los índices que ordenarían el array conteo.

# [::-1] invierte ese orden → de mayor a menor.

# Entonces orden no guarda votos, guarda los índices de los candidatos en el orden correcto.

for i in orden:
    print(f"Candidato {i+1}: {conteo[i]} votos")

# i es el índice de cada candidato en el orden correcto.
# i+1 → porque los candidatos están numerados desde 1, no desde 0.
# conteo[i] → muestra los votos de ese candidato.

print(" ")
print("Parte número 2: ")
## Suponga que en la UIS hay 6500 estudiantes. 
# Por cada uno de ellos tenemos un registro con el código, nombre y promedio acumulado

# Definimos el tipo de dato (como una tabla en memoria)
estudiante = np.dtype([
    ("codigo", "i4"),           #entero de 4 bits
    ("nombre", "U20"),          #Unicode string de 20 caracteres máx.
    ("carrera", "U10"),         #Unicode string de 10 caracteres máx.
    ("promedio", "f8"),         #Float de 8 bits 
    #IMPORTANTE si usamos f4 float de 4 bits; el promedio aunq usemos round(...,2) nos mostrara un monton
    
    ("año_ingreso", "i4"),
    ("condicional", "bool")     #True/False
])

num_estudiantes = 6500

#podriamos usar 
# codigos = np.arange(10000, 10000 + num_estudiantes)
# para generar los Codigos únicos (10000 al 16500)

#pero es mejor
codigos = np.random.choice(
    np.arange(10000, 99999),  # rango de posibles códigos
    size=num_estudiantes,
    replace=False             # sin repetición
)

# Nombres ficticios (Est_1, Est_2, ...)
nombres = np.array([f"Est_{i}" for i in range(1, num_estudiantes + 1)])

# Carreras posibles
carreras_posibles = np.array(["SIS", "IND", "CIV", "ELE", "MEC"])
carreras = np.random.choice(carreras_posibles, size=num_estudiantes) #aqui no se coloca replace pq si s epueden repetir carreras

# Promedios (entre 0 y 5.0)
promedios = np.round(np.random.uniform(0.0, 5.0, size=num_estudiantes), 2) 

# np.random.uniform(0.0, 5.0, ...) → genera valores flotantes aleatorios entre 0 y 5.
# round(..., 2) → deja los decimales con dos cifras (ej: 3.47, 1.25, 4.89).

# Año de ingreso (entre 1980 y 2025)
años = np.random.randint(1980, 2025, size=num_estudiantes)

# Condicional (20% probabilidad de ser True)
condicionales = np.random.choice([True, False], size=num_estudiantes, p=[0.2, 0.8])

#Ahora si creamos el array bien estructurado
estudiantes = np.zeros(num_estudiantes, dtype=estudiante)

estudiantes["codigo"] = codigos
estudiantes["nombre"] = nombres
estudiantes["carrera"] = carreras
estudiantes["promedio"] = promedios
estudiantes["año_ingreso"] = años
estudiantes["condicional"] = condicionales

## SubPunto 1 del punto 2
# Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar)
# que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.

print("Carreras disponibles:") # Queremos llegar a algo similar a ["SIS", "IND", "CIV", "ELE", "MEC"]

for idx, carrera in enumerate(carreras_posibles, start=1): 
# Enumerate(...) sirve para recorrer una lista y tener al mismo tiempo el índice y el valor
# Con el start = 1 le decimos como "Oye, empieza a contar desde 1 en vez de 0".

# idx → va tomando 1, 2, 3, 4, 5…
# carrera → va tomando "SIS", "IND", "CIV", "ELE", "MEC".

# (1, "SIS")
# (2, "IND")
# (3, "CIV")
# (4, "ELE")
# (5, "MEC")

    print(f"{idx}. {carrera}")

# Pedir opción al usuario
opcion = int(input("Ingrese el número de la carrera que desea listar: "))

# Verificar que la opción sea válida
if 1 <= opcion <= len(carreras_posibles):
    carrera_seleccionada = carreras_posibles[opcion - 1] 
    #indice -1 pq comienza desde 0 el index del array y en el de mostrar lo mostramos desde 1
    
    print(f"\nSeleccionaste la carrera: {carrera_seleccionada}\n")

    # Filtrar estudiantes de esa carrera con promedio >= 4
    filtro = (estudiantes["carrera"] == carrera_seleccionada) & (estudiantes["promedio"] >= 4)
    seleccionados = estudiantes[filtro]
    
    #EJEMPLO DE ESTO
    # x = np.array([10, 20, 30, 40, 50])
    # filtro = x > 25   # → [False, False, True, True, True]
    # y = x[filtro]     # → [30, 40, 50]
    
    for est in seleccionados: 
        #est funciona como un i q va yendo de est a est en el array
        
        print(f"Código: {est['codigo']} | Nombre: {est['nombre']} | Promedio: {est['promedio']}")

    print(f"\nTotal: {len(seleccionados)} estudiantes con promedio >= 4 en {carrera_seleccionada}")
    
else:
    print("Opción inválida.")
      
## SubPunto 2 del punto 2 
# Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 y están condicionales.

print("\nParte número 2 - Subpunto 2:\n")

# Filtro: año < 1990 Y condicional == True
filtro2 = (estudiantes["año_ingreso"] < 1990) & (estudiantes["condicional"] == True)

seleccionados2 = estudiantes[filtro2]

# Mostrar resultados
for est in seleccionados2:
    #est funciona como un i q va yendo de est a est en el array
    
    print(f"Código: {est['codigo']} | Nombre: {est['nombre']} | Año ingreso: {est['año_ingreso']} | Condicional: {est['condicional']}")

print(f"\nTotal: {len(seleccionados2)} estudiantes condicionales que ingresaron antes de 1990")
