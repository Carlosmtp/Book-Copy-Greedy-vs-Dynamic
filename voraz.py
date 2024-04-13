from time import time
import matplotlib.pyplot as plt
import numpy as np
import input

def solucion_voraz(n, m, paginas):
    if n == 0:
        return float('inf'), [m-1]
    if m == 0:
        return 0, [0]
    total_paginas = 0
    for i in range(m):
        total_paginas += paginas[i]
    limite_estimado = total_paginas / n
    indices = []
    tiempo = paginas[0]
    tiempo_total = 0
    for j in range(1, m):
        if tiempo + paginas[j] < limite_estimado:
            tiempo += paginas[j]
        elif limite_estimado - tiempo <= tiempo + paginas[j] - limite_estimado:
            if tiempo_total < tiempo:
                tiempo_total = tiempo
            tiempo = paginas[j]
            indices.append(j-1)
        else:
            tiempo += paginas[j]
            if tiempo_total < tiempo:
                tiempo_total = tiempo
            tiempo = 0
            indices.append(j)
    return tiempo_total, indices

def escribir_solucion(n, m, solucion, libros, filename):
    out_filename = filename.split('.')[0] + '_out.txt'
    with open(out_filename, 'w') as file:
        file.write('Tiempo total: {}\n'.format(solucion[0]))
        if n == 0:
            file.write('No hay escritores!!!')
        if m == 0:
            file.write('No hay libros!!!')
        if n >= m:
            for i in range(m):
                file.write('Escritor {}:'.format(i+1))
                file.write(' '.join(libros[i:i+1]) + '\n')
        else:
            for i in range(n):
                file.write('Escritor {}:'.format(i+1))
                if i == 0:
                    file.write(' '.join(libros[0:solucion[1][0]+1]) + '\n')
                elif i == n-1:
                    file.write(' '.join(libros[solucion[1][i-1]+1:]) + '\n')
                else:
                    file.write(' '.join(libros[solucion[1][i-1]+1:solucion[1][i]+1]) + '\n')
                
def main(inputfile):
    n, m, libros, paginas = input.leer_archivo(inputfile)
    sol = solucion_voraz(n, m, paginas)
    escribir_solucion(n, m, sol, libros, inputfile)

def graficar_tiempos_ejecucion():
    archivos = ['10.txt', '20.txt', '30.txt', '40.txt', '50.txt',
                '100.txt', '200.txt', '300.txt', '400.txt', '500.txt',
                '1000.txt', '2000.txt', '3000.txt', '4000.txt', '5000.txt',
                '10000.txt', '20000.txt', '30000.txt', '40000.txt', '50000.txt',
                '60000.txt', '70000.txt', '80000.txt', '90000.txt', '100000.txt'
                ]
    tiempos = []
    
    for archivo in archivos:
        inicio = time()
        main(archivo)
        fin = time()
        tiempo_ejecucion = fin - inicio
        tiempos.append(tiempo_ejecucion)
        print('Tiempo de ejecucion para {}: {} segundos'.format(archivo, tiempo_ejecucion))
    plt.plot(archivos, tiempos)
    plt.xlabel('Archivo')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempos de ejecución')
    plt.xticks(rotation=90)
    plt.show()

graficar_tiempos_ejecucion()