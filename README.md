# Copia de Libros

Este repositorio contiene implementaciones de algoritmos voraz y dinámico para optimizar la copia de libros entre múltiples escritores. Este proyecto forma parte del curso de Fundamentos de Análisis y Diseño de Algoritmos.

## Descripción del Problema

Antes de la invención de las fotocopiadoras, hacer copias de libros era un trabajo manual que podía llevar meses. En este contexto, se presenta un escenario donde un profesor de teatro necesita hacer copias de una obra famosa dividida en varios libros, cada uno con un número diferente de páginas, y desea hacerlo lo más rápido posible contratando a varios escritores.
[Enunciado Completo](Enunciado.pdf)

## Soluciones Propuestas

1. **Algoritmo Voraz:** Se propone una solución que sigue una estrategia de selección voraz, asignando a cada escritor una secuencia continua de libros, con el objetivo de minimizar el tiempo total de copia.
2. **Algoritmo Dinámico:** Se propone una solución que utiliza programación dinámica para encontrar la distribución óptima de libros entre los escritores, considerando diferentes combinaciones posibles y minimizando el tiempo total de copia.

## Formato de Entrada y Salida

### Entrada

El algoritmo recibe un archivo de texto en el siguiente formato:
```
n
m
nombre_libro_1 paginas_1
...
nombre_libro_m paginas_m
```
Donde:
- `n` es el número de escritores.
- `m` es el número de libros.
- Las siguientes `m` líneas contienen información sobre cada libro, incluyendo su nombre y el número de páginas que contiene.

### Salida

Se espera que el programa genere un archivo de texto donde la primera línea sea el tiempo en días que tarda en copiar todos los libros, seguido de la distribución de libros elegida para cada escritor.

## Análisis de Eficiencia

La complejidad de cada alternativa de solución debe ser calculada y comparada con las mediciones de tiempo de ejecución tomadas para diferentes entradas y tamaños de datos. [Informe](Proyecto_FADA_1741699.pdf)

Este proyecto tiene como objetivo proporcionar una implementación eficiente para resolver el problema de copia de libros, permitiendo una distribución óptima de la tarea entre múltiples escritores.
