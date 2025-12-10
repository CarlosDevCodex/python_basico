# haremos  un progrma que sume  números  hasta  que el usuario ingrese el cero
# al final del programa debe ingresar la suma de números introducidos
# la cantidad de  números  que se sumaron

suma=0
while True:
    numero=float(input('Ingrese le número: '))
    suma += numero
    if numero==0:
        break
print(f"La suma es: ", suma)
