import os
import random

def read_srflp(file_name):
    """
    Función para el análisis y lectura de las instancias del problema.
    file_name: Nombre del archivo de la instancia.
    return: Número de instalaciones, tamaños de las instalaciones y matriz de pesos.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()

        n = int(lines[0].strip())
        f_size = list(map(int, lines[1].strip().split(',')))
        f_weight = [list(map(int, line.strip().split(','))) for line in lines[2:]]

    return n, f_size, f_weight

def print_instance(n, f_size, f_weight):
    """
    Función para imprimir la información de la instancia SRFLP.
    n: Número de instalaciones.
    f_size: Tamaños de las instalaciones.
    f_weight: Matriz de pesos.
    """
    print("Numero de instalaciones:", n)
    print("Tamaños:", " ".join(map(str, f_size)))
    print("Pesos:")
    for row in f_weight:
        print(" ".join(map(str, row)))

def get_weight(f_weight, i, j):
    """
    Función para obtener el flujo entre dos instalaciones i y j.
    f_weight: Matriz de pesos.
    i: Índice de la instalación i.
    j: Índice de la instalación j.
    return: Valor del flujo entre las instalaciones i y j.
    """
    return f_weight[i][j]

def get_facility_size(f_size, i):
    """
    Función para obtener el tamaño de una instalación.
    f_size: Tamaños de las instalaciones.
    i: Índice de la instalación i.
    return: Tamaño de la instalación i.
    """
    return f_size[i]

def total_distance(n, f_size, f_weight, sol):
    """
    Función para calcular la distancia total recorrida por los clientes en base a la solución sol.
    n: Número de instalaciones.
    f_size: Tamaños de las instalaciones.
    f_weight: Matriz de pesos.
    sol: Arreglo con el orden de las instalaciones.
    return: Distancia total recorrida por los clientes.
    """
    total = 0.0
    middle_distance = 0.0

    for i in range(n - 1):
        p1 = sol[i]
        middle_distance = 0.0
        for j in range(i + 1, n):
            p2 = sol[j]
            total += ( (f_size[p1] / 2 + middle_distance + f_size[p2] / 2) * (f_weight[i][j]) )
            middle_distance += f_size[p2]

    return total

def solucionInicial(n):
    arreglo = []
    for i in range(0,n):
        arreglo.append(i)
    solucion = random.sample(arreglo, n)
    return solucion

def swap(n, f_size, f_weight, sol):
    dist1 = total_distance(n, f_size, f_weight, sol)
    sol_aux = sol[:]
    print(sol)
    print("Base:", dist1)

    for i in range(0,10):
        j1,j2 = random.sample(sol_aux, 2)

        aux = sol_aux[j1]
        sol_aux[j1] = sol_aux[j2]
        sol_aux[j2] = aux

        pos_dist = total_distance(n, f_size, f_weight, sol_aux)
    
        if dist1 > pos_dist:
            print(i,":", pos_dist)
            sol = sol_aux
            dist1 = pos_dist
        elif i == 4:
            print("Caso especial:", pos_dist)
            sol = sol_aux
            dist1 = pos_dist
    return sol
    

#Ejemplo de uso:
file_name = "S8.txt"
n, f_size, f_weight = read_srflp(file_name)
#print_instance(n, f_size, f_weight)
dist_final = 0
solucion = solucionInicial(n)  # Ejemplo de solución
solucion = swap(n, f_size, f_weight, solucion)
# 56 
#solucion = [40, 14, 20, 24, 53, 0, 15, 3, 45, 1, 7, 36, 47, 33, 38, 25, 26, 16, 44, 5, 19, 11, 42, 30, 46, 52, 49, 27, 23, 54, 13, 6, 35, 9, 10, 28, 50, 4, 43, 55, 12, 17, 51, 8, 39, 22, 29, 41, 48, 32, 18, 21, 31, 2, 37, 34]
# 100
#solucion = [48, 41, 38, 78, 70, 24, 31, 92, 96, 17, 4, 93, 51, 67, 7, 97, 82, 8, 15, 87, 21, 32, 42, 20, 26, 74, 79, 23, 59, 66, 85, 27, 30, 73, 18, 88, 53, 14, 0, 55, 95, 64, 3, 90, 84, 54, 12, 10, 77, 62, 56, 61, 36, 76, 58, 80, 60, 49, 91, 47, 89, 99, 37, 45, 25, 81, 68, 52, 34, 71, 65, 69, 35, 50, 9, 39, 19, 29, 46, 72, 13, 40, 86, 33, 63, 94, 43, 28, 22, 11, 16, 98, 1, 75, 57, 44, 83, 5, 2, 6]

print(f"\nSolucion final: ", solucion)
print(f"Distancia total final:", total_distance(n, f_size, f_weight, solucion))
