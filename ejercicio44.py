usuarios = []

def ingresar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        nota = float(input("Ingrese la nota (0 a 5): "))

        if nota >= 0 and nota <= 5:
            break
        else:
            print("Error: la nota debe estar entre 0 y 5")

    if nota >= 3.0:
        resultado = "GANO"
    else:
        resultado = "PERDIO"

    usuarios.append({
        "nombre": nombre,
        "nota": nota,
        "resultado": resultado
    })

    print("Estudiante agregado correctamente")


def mostrar_estudiantes():
    if len(usuarios) == 0:
        print("No hay estudiantes registrados")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")

        for estudiante in usuarios:
            print("Nombre:", estudiante["nombre"])
            print("Nota:", estudiante["nota"])
            print("Resultado:", estudiante["resultado"])
            print("----------------------")


def estadistica():
    if len(usuarios) == 0:
        print("No hay notas registradas")
    else:
        suma = 0

        for estudiante in usuarios:
            suma += estudiante["nota"]

        promedio = suma / len(usuarios)

        print("\n--- ESTADISTICA DE ESTUDIANTES ---")
        print("Cantidad de estudiantes:", len(usuarios))
        print("Promedio de todas las notas:", round(promedio, 2))

        if promedio >= 3.0:
            print("El promedio general es: GANADO")
        else:
            print("El promedio general es: PERDIDO")


while True:
    print("\n--- MENU ---")
    print("1. Ingresar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Estadistica estudiantes")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        ingresar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        estadistica()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion incorrecta")s
