# creamos un programa con interface gráfica
# importamos  las librerías tkinder

import  tkinter  as tk
# importamos la clase messagebox
from tkinter import messagebox
# creamos  un método  que manejará cuadros de dialogos y etiquetas
def etiquetas_y_texto(): #definimos el método
    # creamos la ventana
    ventana=tk.Tk()#de tkinter  tomamos el objeto tk (una ventana)
    # pondremos el título
    ventana.title('Etiquetas y Cuadros de textos')
    # ajustamos el tamaño de la ventana
    ventana.geometry('300x300')
    # crearemos un etiqueta personalizada, gracias al objeto label
    etiqueta = tk.Label(ventana, text='Ingresa tu nombre: ', font=('Arial',12,'bold'),fg='blue')
    # ahora hay que empaquetar dentro de la ventana
    etiqueta.pack(pady=5)
    # ahora crearemos un cuadro de texto personalizados(es como un input para meter datos)
    entrada=tk.Entry(ventana,font=('Arial',12),width=30,justify='center')
    entrada.pack(pady=5)
    def  mostrar_nombre():#este método va dentro del método etiuqetas_y_texto()
        # obtenemos  lo que hay en entrada con el método get y eliminamos los espacios
        # del inicio o del final, con el método strip()
        nombre=entrada.get().strip()
        if nombre: #si hay información en la variable nombre, entoces
            messagebox.showinfo('Nombre: ',f'Tu nombre es: {nombre}') 
        else:#si no hay informaicón 
            messagebox.showwarning('Advertencia','Por favor ingresa tu nombre')
    # creamos un frame por si  deseas agurpar  o centrar varios botones
    marco_botones=tk.Frame(ventana)
    marco_botones.pack(pady=10, expand=True)#separamos 10 pixeles del objeto anterior y expandimos
    marco_botones.pack(padx=10, anchor='center')#centra el frame en la ventana
    # insertamos un botón para mostrar el nombre
    boton_mostrar=tk.Button(marco_botones, text='Mostrar',font=('Arial',12),
                            bg='green',fg='white',width=10, command=mostrar_nombre)
    boton_mostrar.pack(side=tk.LEFT,padx=10)#sepración de 10 puntos sobre ele elemento de al lado
    #mostramos la ventana
    ventana.mainloop()

etiquetas_y_texto()#fuera del método, lo llamams con su nombre 