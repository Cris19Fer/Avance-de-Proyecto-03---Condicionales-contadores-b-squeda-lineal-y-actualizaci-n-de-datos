# Avance-de-Proyecto-03---Condicionales-contadores-b-squeda-lineal-y-actualizaci-n-de-datos
AVANCE DE PROYECTO 03
# ==================== LISTAS ====================
cursos_lista = ["Mate Discreta","Contabilidad 2","Pre Cálculo", "Algebra Lineal","Algoritmos"]
notas_lista = [78,61,65,82,89]

# Cola de solicitudes de revisión
cola_revisiones = deque()

# Historial de cambios (pila)
historial_cambios = []

# ==================== MENÚ ====================
def mostrar_menu():
    print("""
========= MENÚ =========
1. Registrar nuevo curso
2. Mostrar todos los cursos y notas
3. Calcular promedio general
4. Contar cursos aprobados y reprobados
5. Buscar curso por nombre (búsqueda lineal)
6. Actualizar nota de un curso
7. Eliminar curso
8. Ordenar cursos por nota (ordenamiento burbuja)
9. Ordenar cursos por nombre (ordenamiento burbuja)
10. Buscar curso por nombre (búsqueda binaria)
11. Simular cola de solicitudes de revisión
12. Mostrar historial de cambios (pila)
13. Salir
========================


# ==================== FUNCIONES ====================

# 1 Registrar curso
def registrar_curso_lista():
    try:
        n = int(input("Ingrese la cantidad de cursos a registrar: "))
    except ValueError:
        print("Ingrese un número válido")
        return
 #   
    for i in range(1, n+1):
        while True:
            curso = input(f"Ingrese el nombre del curso {i}: ").strip()
            if not curso:
                print("No puede estar vacío")
                continue
            if curso in cursos_lista:
                print(f"El curso '{curso}' ya está registrado.")
                continue
            break

        while True:
            try:
                nota = float(input(f"Ingrese la nota para {curso}: "))
                if 0 <= nota <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100")
            except ValueError:
                print("Nota inválida, intente de nuevo")

        cursos_lista.append(curso)
        notas_lista.append(nota)

    print("\nCursos y notas registradas:")
    for i in range(len(cursos_lista)):
        print(f"{cursos_lista[i]}: {notas_lista[i]}")
#
# 2 Mostrar cursos
def mostrar_cursos_lista():
    if not cursos_lista:
        print("No hay cursos registrados aún")
        return
    print("\nLista de cursos y notas:")
    for i in range(len(cursos_lista)):
        print(f"{cursos_lista[i]}: {notas_lista[i]}")

# 3 Promedio
def promedio():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    print("\nCursos y notas actuales:")
    for i in range(len(cursos_lista)):
        print(f"{cursos_lista[i]}: {notas_lista[i]}")
    prom = sum(notas_lista)/len(notas_lista)
    print(f"\nEl promedio de las notas es: {prom:.2f}")

# 4 Aprobados y reprobados
def cursos_aprobados_reprobados():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    aprobados, reprobados = [], []
    for i in range(len(cursos_lista)):
        if notas_lista[i] >= 61:
            aprobados.append((cursos_lista[i], notas_lista[i]))
        else:
            reprobados.append((cursos_lista[i], notas_lista[i]))
    print("\nCursos Aprobados:")
    if aprobados:
        for c,n in aprobados:
            print(f"{c}: {n}")
    else:
        print("Ninguno")
    print("\nCursos Reprobados:")
    if reprobados:
        for c,n in reprobados:
            print(f"{c}: {n}")
    else:
        print("Ninguno")

# 5 Buscar curso lineal
def buscar_curso():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    nombre = input("Ingrese el nombre del curso: ").strip()
    if nombre in cursos_lista:
        idx = cursos_lista.index(nombre)
        nota = notas_lista[idx]
        print(f"\nCurso encontrado: {nombre}")
        print(f"Nota: {nota}")
        print("Estado: Aprobado" if nota>=61 else "Estado: Reprobado")
    else:
        print(f"El curso '{nombre}' no está registrado.")

# 6 Actualizar nota
def actualizar_nota():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip()
    if nombre in cursos_lista:
        idx = cursos_lista.index(nombre)
        nota_anterior = notas_lista[idx]
        print(f"Nota actual de {nombre}: {nota_anterior}")
        while True:
            try:
                nueva = float(input("Ingrese nueva nota: "))
                if 0 <= nueva <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido")
        notas_lista[idx] = nueva
        print(f"Nota actualizada: {nombre} - {nueva}")
        # Guardar en historial
        historial_cambios.append(f"Curso: {nombre} | Nota anterior: {nota_anterior} | Nueva nota: {nueva}")
    else:
        print(f"Curso '{nombre}' no registrado.")

# 7 Borrar curso
def borrar_curso_lista():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    print("\nCursos registrados:")
    for i,c in enumerate(cursos_lista):
        print(f"{i+1}. {c} - Nota: {notas_lista[i]}")
    try:
        sel = int(input("Elija número de curso a borrar: "))
        if 1 <= sel <= len(cursos_lista):
            conf = input(f"¿Está seguro de borrar '{cursos_lista[sel-1]}'? (s/n): ").lower()
            if conf=="s":
                eliminado_c = cursos_lista.pop(sel-1)
                eliminado_n = notas_lista.pop(sel-1)
                print(f"Curso '{eliminado_c}' con nota {eliminado_n} eliminado.")
            else:
                print("Operación cancelada")
        else:
            print("Número inválido")
    except ValueError:
        print("Debes ingresar un número válido")

# 8 Ordenar por nota (burbuja)
def ordenar_por_nota_burbuja():
    n = len(notas_lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if notas_lista[j]>notas_lista[j+1]:
                notas_lista[j], notas_lista[j+1] = notas_lista[j+1], notas_lista[j]
                cursos_lista[j], cursos_lista[j+1] = cursos_lista[j+1], cursos_lista[j]
    print("\nCursos ordenados por nota (menor a mayor):")
    for c,n in zip(cursos_lista, notas_lista):
        print(f"{c}: {n}")

# 9 Ordenar por nombre (burbuja)
def ordenar_por_nombre():
    n = len(cursos_lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if cursos_lista[j].lower()>cursos_lista[j+1].lower():
                cursos_lista[j], cursos_lista[j+1] = cursos_lista[j+1], cursos_lista[j]
                notas_lista[j], notas_lista[j+1] = notas_lista[j+1], notas_lista[j]
    print("\nCursos ordenados alfabéticamente:")
    for c,n in zip(cursos_lista, notas_lista):
        print(f"{c}: {n}")

# 10 Búsqueda binaria
def buscar_curso_binario():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    nombre = input("Ingrese el nombre del curso: ").strip().lower()
    ordenar_por_nombre()
    izq, der = 0, len(cursos_lista)-1
    while izq<=der:
        medio = (izq+der)//2
        curso_actual = cursos_lista[medio].lower()
        if curso_actual==nombre:
            nota = notas_lista[medio]
            print(f"\nCurso encontrado: {cursos_lista[medio]}")
            print(f"Nota: {nota}")
            print("Estado: Aprobado" if nota>=61 else "Estado: Reprobado")
            return
        elif nombre<curso_actual:
            der = medio-1
        else:
            izq = medio+1
    print(f"Curso '{nombre}' no registrado.")

# 11 Cola de solicitudes de revisión
def simular_cola_revision():
    if not cursos_lista:
        print("No hay cursos registrados")
        return
    while True:
        print("\n--- Cola de solicitudes de revisión ---")
        print("1. Agregar solicitud")
        print("2. Atender primera solicitud")
        print("3. Mostrar solicitudes")
        print("4. Salir de submenú")
        try:
            opcion = int(input("Elija opción (1-4): "))
        except ValueError:
            print("Ingrese un número válido")
            continue
        if opcion==1:
            nombre = input("Ingrese nombre del curso: ").strip()
            if nombre in cursos_lista:
                cola_revisiones.append(nombre)
                print(f"Solicitud agregada para: {nombre}")
            else:
                print("Curso no registrado")
        elif opcion==2:
            if cola_revisiones:
                curso = cola_revisiones.popleft()
                idx = cursos_lista.index(curso)
                nota_anterior = notas_lista[idx]
                print(f"\nAtendiendo solicitud de: {curso}")
                print(f"Nota anterior: {nota_anterior}")
                while True:
                    try:
                        nueva = float(input(f"Ingrese nueva nota para '{curso}': "))
                        if 0<=nueva<=100:
                            break
                        else:
                            print("Debe estar entre 0 y 100")
                    except ValueError:
                        print("Ingrese número válido")
                notas_lista[idx] = nueva
                historial_cambios.append(f"Curso: {curso} | Nota anterior: {nota_anterior} | Nueva nota: {nueva}")
                print(f"Solicitud atendida. Nota actualizada: {nueva}")
            else:
                print("No hay solicitudes en la cola")
        elif opcion==3:
            if cola_revisiones:
                print("Solicitudes en la cola:")
                for c in cola_revisiones:
                    print(c)
            else:
                print("Cola vacía")
        elif opcion==4:
            break
        else:
            print("Opción inválida")

# 12 Historial de cambios
def mostrar_historial():
    if historial_cambios:
        print("\n--- Historial de cambios ---")
        for registro in reversed(historial_cambios):
            print(registro)
    else:
        print("No hay cambios registrados")

# ==================== EJECUTAR OPCIONES ====================
def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            registrar_curso_lista()
        case 2:
            mostrar_cursos_lista()
        case 3:
            promedio()
        case 4:
            cursos_aprobados_reprobados()
        case 5:
            buscar_curso()
        case 6:
            actualizar_nota()
        case 7:
            borrar_curso_lista()
        case 8:
            ordenar_por_nota_burbuja()
        case 9:
            ordenar_por_nombre()
        case 10:
            buscar_curso_binario()
        case 11:
            simular_cola_revision()
        case 12:
            mostrar_historial()
        case 13:
            print("Saliendo del programa...")
            return False
        case _:
            print("Opción inválida")
    return True

# ==================== BUCLE PRINCIPAL ====================
while True:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opción (1-13): "))
    except ValueError:
        print("Debes ingresar un número válido")
        continue
    if not ejecutar_opcion(opcion):
        break
    resp = input("\n¿Desea realizar otra operación? (s/n): ").lower()
    if resp != "s":
        print("Programa terminado")
        break
