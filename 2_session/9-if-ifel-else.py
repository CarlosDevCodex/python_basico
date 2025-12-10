# crearemos un programa que con base en el peso de una persona, emita un
# dictámen, si el peso es mayor que 120 "Tienes sobrepeso":
# si está entre 120 y 90 "Eres corpulento"
# si el peso está entre 89.9999 y 70 "Eres fornido"
# si el peso está entre 69.9999 y 50 "Estás en forma"
# si el peso está entre 49.9999 y 40 "Eres delgado"
# si el peso está entre 39.9999 y hasta 20 "cuida tu salud"
# en cualquier otro caso, avisar, ese peso no es válido para personas
# normales

peso= float(input('Ingrese su peso: ')) 

if peso>=120:
    print("Tienes sobrepeso")
elif 70 <= peso <= 89.9999:
    print("Eres fornido")
elif 50 <= peso <= 69.9999:
    print("Estás en forma")
elif 40 <= peso <= 49.9999:
    print("Eres delgado")
elif 20 <= peso <= 39.9999:
    print("cuida tu salud")
else:
    print("ese peso no es válido para personas")
