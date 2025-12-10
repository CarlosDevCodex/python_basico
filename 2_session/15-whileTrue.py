# Veremos  como validar  una contraseña utilizando while True
# no validaremos el usuario , solo la contraseña,  se dará 3 intentos
usuario=input('Escribe tu usuario: ') 
intentos=0

while True:
    intentos += 1
    contraseña=input('Ingrese a contraseña: ')
    if contraseña=='123':
        print('Contraseña correcta')
        break
    elif intentos==3:
        print('ha ingresado 3 intentos')
        break
    else:
        print(f"Ha ingresado el intento número {intentos}")
