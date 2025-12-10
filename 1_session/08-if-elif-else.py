# El programa debe clasificar la nota:
# Si la calificación está entre 18 y 20: mensaje de felicitaciones (excelente).
# Si la calificación está entre 11 y menos de 18: mensaje de felicitaciones (aprobaste).
# Cualquier otro caso: mensaje de desaprobado.

nota = float(input('Ingresa tu nota: '))

if 18 <= nota <= 20:
    print(f'Felicitaciones, tienes una nota de {nota} y es excelente.')
elif 11<=nota<=17.99:
    print(f'Felicitaciones, tienes una nota de {nota} aprobastes.')
else:
    print(f"Lo sentimos, tienes una nota de {nota} y desaprobaste.")

print('fin de la tarea.')

