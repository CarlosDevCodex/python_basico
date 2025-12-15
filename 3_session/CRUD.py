# creamos un CRUD, que es la parte  mínima  de un sistema
# infrmático.
# por ejemplo, el sistema que usan  la farmaciade compramos
# es un POS(Point if sale; punto de venta), por cada entidad que maneja
# (clientes, productos, ventas, etc.) se debe crear un CRUD , es el acrónimo de:
# Create (agregar, un nuenvo registro),Read (Leer o buscar un registro),
# Update (Modificar un registro) Delete (Eliminar un registro)
# Haremos un CRUD la entidad del producto
import  os
import time
import  mysql.connector

# Paso 1. creamos  el módulo que conectará python  con la BD de Mysql
mybd=mysql.connector.connect(
   host='localhost',#c cualquier comnputadora a conectar
   user='root',
   password='',#sin conmtraseña
   database='farmaciaperu'

)
# Paso 2, creamos un cursor,(un objeto para ejecutar comandos de sql server en la base de datos)
mycursor = mybd.cursor()
# paso 3, creamos  un interfaz de usuario que verá  el usuario() (nuestro front-end)
while True:#Este  ciclo asegura que al menos 1 vez el susuario verá  el menú
    print(
        "===MENU DE LA FARMACIA==="
        "\n1. Insertar un producto"
        "\n2. Eliminar un producto"
        "\n3. Buscar un producto"
        "\n4. Modificar un producto"
        "\n5. Mostrar el catalogos de productos"
        "\n6. Salir dle sistema"
    )
    opcion= int(input('Elige una opción  del menú: '))
    # si el susuario  elige la opción 1
    if opcion==1:#el usuarioquiere guardar un producto (create)
        clave=input('clave del producto: ')
        nombre=input('nombre del producto: ')
        precio=input('precio del producto: ')
        # creamos la instrucción del SQL para insertar
        sql = 'INSERT INTO PRODUCTOS (CLAVE,NOMBRE, PRECIO) VALUES (%s,%s,%s)'
        # CREAMOS LA TUPLA (DATOS QUE SE VAN A GUARDAR EN LA TABLA PRODUCTOS)
        val=(clave, nombre, precio) 
        # preparamos apra insertar
        mycursor.execute(sql,val)
        # insertamos
        mybd.commit()#ahora lo insertó
        # aisamos al usuario
        print('Producto agregado al sistema.....')
        time.sleep(2)
        os.system('cls')
    elif opcion==2: #Eliminar un producto (delete)
        clave=input('clave  del ,producto a eliminar: ')
        # creamos la instrucción sql para eliminar
        sql='DELETE FROM PRODUCTOS WHERE clave=%s'
        # Creamos la tupa
        val=(clave,)
        # preparamos para eliminar
        mycursor.execute(sql, val)
        # eliminamos
        mybd.commit()
        print(f'El producto con clave {clave} fue elimado del sistema')
        time.sleep(3)
        os.system('cls')#es clear
    elif opcion==3:#conuslta del producto
        clave=input('Escribe la clave del producto a buscar: ')
        # creamos la consulta en este  caso de selección
        sql='select   *   from productos where clave=%s'
        #creamos la tupla
        val=(clave,)
        # preparamos la instrucción
        mycursor.execute(sql, val)
        # verificarmos si existe el producto
        myresult = mycursor.fetchall()#guardamos el resultado de la busquda
        if myresult: #si myresult hay dato?
            print(f'El producto con clave {clave} si existe en el sistema')
        else:#si no hay datos en el resultado
            print(f"El producto con clave {clave} no existe en el sistema")
        time.sleep(3)
        os.system('cls')    
