# Realiza  un programa que imprima  la cuenta regresiva  del 1000 al 1
# sin llegar a números negativos

import   time 
contador=1000

limite=int(input('Ingrese el número del límite: '))

while contador > limite:
    print(contador)
    time.sleep(.010)
    contador-=1
