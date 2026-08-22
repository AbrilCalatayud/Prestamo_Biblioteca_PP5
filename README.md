# Tarea de Paradigmas de Programación 5: Préstamo de biblioteca

## Consigna: [Link](https://paradigmas-v-fie.github.io/reuniones-2026/ejercicios/reuniones/clase-1.html)

## ¿Qué regla quedó dentro de Prestamo y qué problema habría si la calculara quien usa el objeto?
### Respuesta: 
Las reglas que quedaron dentro son el cálculo de si está vencido o no el préstamo, los días de retraso (son 0 si no está vencido) y el armado del resumen con la información importante. 
El problema que habría si el vencimiento o los días de retraso los calculara otra clase es que se estarían leyendo atributos de Prestamo directamente desde afuera, no se cumpliría el principio de encapsulación.

## Requerimientos previos antes de clonar el repositorio
* Python 3.13 en adelante
* Pytest 9.1.1

## Cómo clonar el repositorio
* Apretá el botón que dice "<> Code"
* Copiá la URL. Es esta: https://github.com/AbrilCalatayud/Prestamo_Biblioteca_PP5.git
* Abrí tu terminal
* Navegá hasta la carpeta donde querés clonar el repositorio con `cd ruta/de/carpeta`
* Escribí `git clone`, pegá la URL que copiaste y presioná Enter
