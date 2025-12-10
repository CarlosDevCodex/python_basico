# creamos un ejemplo  de interfaz gráfico, usando la librería
import  tkinter as  tk #para crear interface gráfica
from  tkinter  import  messagebox#crear cajas de mensajes

# creamos  un método (bloque de código) en el cual ponemos el código
# del interface gráfica

def ventana_y_buton():
    # creamos la ventana principal
    ventana=tk.Tk()
    # poner títuloa a la ventana
    ventana.title('Ejemplo de boton')
    # Establecemos el tamaño y la posición de la ventana
    # (ancho x alto + posinix +posinY)
    ventana.geometry('400x200+400+100')
    # creamos el boton de la ventana, con el texto "haz click"
    # y al dar clic, se debe crear una caja de mensaje del titulo
    #'Mensaje' y y esl texto "botón presinado"
    boton=tk.Button(ventana, text='Haz click',
                 command=lambda:messagebox.showinfo('Mensaje','Botón presionado'))
    # separamos e botón 20 pixeles  en el eje y
    # boton.pack mete el boton en la ventana
    boton.pack(pady=20)
    # matenemos la ventana abierta esperando iteracción con el usuario
    ventana.mainloop()

    # invocación del método

ventana_y_buton()
