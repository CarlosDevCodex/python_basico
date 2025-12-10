#veremos el uso  de la estructura  repetitiva while True
#el programa pedirá  la palabra salir  para terminar la ejecución
#mientras esto  no ocurra, seguirá pidiendo dicha palabra

while True:
    texto=input('Escribe salir para terminar el ciclo: ') 
    if texto.lower()=='salir':
        break
print('Progrma terminado....')

