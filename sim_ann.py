import random as r
import math as m

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
            total += ( (f_size[p1] / 2 + middle_distance + f_size[p2] / 2) * (f_weight[p1][p2]) )
            middle_distance += f_size[p2]

    return total

def solucionInicial(n):
    """
    Función para obtener la solución inicial aleatorizada.
    n: Número de instalaciones.
    return: Arreglo con el orden de las instalaciones aleatorizadas.
    """
    arreglo = []
    for i in range(0,n):
        arreglo.append(i)
    solucion = r.sample(arreglo, n)
    return solucion

def swap(mod_arr):
    """
    Función para realizar cambiar los valores de dos posiciones en un arreglo.
    mod_arr: Arreglo con el orden de las instalaciones.
    """
    # Utilizando sample, se seleccionan aleatoriamente dos posiciones al azar del arreglo
    j1,j2 = r.sample(mod_arr, 2)

    # Utilizando una variable auxiliar, se intercambian ambas posiciones en el arreglo
    aux = mod_arr[j1]
    mod_arr[j1] = mod_arr[j2]
    mod_arr[j2] = aux

def simulated_annealing(n, f_size, f_weight, sol):
    """
    Función para realizar el Simulated Annealing.
    n: Número de instalaciones.
    f_size: Tamaños de las instalaciones.
    f_weight: Matriz de pesos.
    sol: Arreglo con el orden de las instalaciones.
    return: Retorna la mejor solución encontrada en forma de arreglo con el orden de los puestos según los criterios de aceptación.
    """
    # Se calcula la distancia de la solución inicial
    dist_ori = total_distance(n, f_size, f_weight, sol)
    # Se copia en otro arreglo la solución inicial
    mod_arr = sol.copy()

    # Párametros
    t_i = 1000 # Temperatura actual
    t_m = 0.1 # Temperatura mínima
    alpha = 0.98 # Párametro alfa
    # Mientras la temperatura actual no sea menor a la temperatura mínima, se realizaran iteraciones
    while(t_i > t_m):
        # Se utiliza el operador SWAP para modificar el orden de los puestos
        swap(mod_arr)
        # Se calcula la distancia de la nueva solución
        pos_dist = total_distance(n, f_size, f_weight, mod_arr)
        # Se calcula la diferencia de las distancias
        dif_dist = pos_dist - dist_ori

        # Si la distancia es menor, significa que la solución nueva es mejor que la actual
        if dif_dist < 0:
            # Se copia el valor en el arreglo que se entregara al final, en conjunto de la distancia calculada.
            sol = mod_arr.copy()
            dist_ori = pos_dist
            print(f"Solución Criterio A: {dist_ori}") 
        # Si la distancia es mayor, se evalua utilizando el criterio de metropolis si se cambia o no, para explorar más en el espacio de búsqueda
        elif m.exp(-(dif_dist)/(t_i)) > r.random():
            # Se copia el valor en el arreglo que se entregara al final, en conjunto de la distancia calculada.
            sol = mod_arr.copy()
            dist_ori = pos_dist
            print(f"Solución Criterio B: {dist_ori}") 
        # Se disminuye la temperatura actual utilizando el parámetro alfa
        t_i *= alpha
    return sol
    
## FUNCIÓN PRINCIPAL
# Seleccionar archivo
file_name = "sko56.txt"
# Lectura del archivo
n, f_size, f_weight = read_srflp(file_name)
# Mostrar por pantalla los valores de la instancia
print_instance(n, f_size, f_weight)
print("\n===========================\n")
# Solución generada de forma aleatoria uniforme
solucion = solucionInicial(n)  
# Se llama a la función para realizar el Simulated Annealing
solucion = simulated_annealing(n, f_size, f_weight, solucion) 
# Se muestra la mejor solución encontrada
print(f"\nSolucion final: ", solucion)
# Se muestra el resultado de la función objetivo
print(f"Distancia total final:", total_distance(n, f_size, f_weight, solucion))
