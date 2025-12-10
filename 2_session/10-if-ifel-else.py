# el programa pedirá en formato 24  horas y dará el saludo correspondiente

hora = int(input('Ingrese la hora'))

# usaremos  el if  anidados, es decir  un if dentro de otro if

if   0<=hora<=24:
    if hora<7:
        print('es de madrugrada')
    elif hora<12:
        print("buenos días")
    elif hora<19:
        print("buenos tardes")
    elif hora <24:
        print("buenos noches")
