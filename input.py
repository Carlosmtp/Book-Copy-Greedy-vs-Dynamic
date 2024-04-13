def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        lines = file.readlines()
        n, m = map(int, lines[0].split())
        libros = ['name'] * m
        paginas = [0] * m
        for i in range(m):
            libros[i], paginas[i] = lines[i+1].split()[0], int(lines[i+1].split()[1])
    return n, m, libros, paginas