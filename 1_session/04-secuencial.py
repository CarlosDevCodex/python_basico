# calcular el promedio  de 3 calificaciones
# usuraremos un librería  llamada time para controlar
# el tiempo de ejecución

import time

mat=float(input('Calf. de matemáticas: '))
fis = float(input("Calf. de fisicas: "))
qui=float(input('Calificaciónd e química: '))

prom=(mat+fis+qui)/3

print('Procesando...')
time.sleep(5)
print(f'El promedio es: {round(prom,2)}')

