import input
import argparse
from time import time
paginas = []
libros = []
dp = [[float(-1) for i in range(100000)] for j in range(100000)]

def solucion_dinamica(n, m, paginas):
    if dp[n][m] != -1:
        return dp[n][m]
    if m == 0:
        return 0
    elif n == 1:
        return sum(paginas)
    else:
        min_tiempo = float('inf')
        for i in range(1, m + 1):
            tiempo_actual = max(sum(paginas[:i]), solucion_dinamica(n - 1, m - i, paginas[i:]))
            min_tiempo = min(min_tiempo, tiempo_actual)
            dp[n][m] = min_tiempo
        return min_tiempo

def main(inputfile):
    global libros, paginas, dp
    inicio = time()
    n, m, libros, paginas = input.leer_archivo(inputfile + '.txt')
    print(solucion_dinamica(n, m, paginas))
    fin = time()
    print('Tiempo de ejecucion: ', fin - inicio, 'segundos')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)