import input
import argparse
from time import time
paginas = []
libros = []

def solucion_recursiva(n, m, paginas):
    if m == 0:
        return 0
    elif n == 1:
        return sum(paginas)
    else:
        min_tiempo = float('inf')
        for i in range(1, m + 1):
            tiempo_actual = max(sum(paginas[:i]), solucion_recursiva(n - 1, m - i, paginas[i:]))
            min_tiempo = min(min_tiempo, tiempo_actual)
        return min_tiempo
    
def main(inputfile):
    inicio = time()
    n, m, libros, paginas = input.leer_archivo(inputfile + '.txt')
    print(solucion_recursiva(n, m, paginas))
    fin = time()
    print('Tiempo de ejecucion: ', fin - inicio, 'segundos')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)