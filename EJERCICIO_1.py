##crear lista de radio button que muestre la opcion que se ha seleccionado y que contenga un boton de reinicio 
#para que deje todo como al principio. Al principio no debe habr nada seleccionado


from tkinter import *
import string
import tkinter

window = tkinter.Tk()

checkeado = StringVar()
checkeado.set(None)

def seleccionaste():
    print("hola hago algo cuando le dan click al boton")
    ventana.config(text="{}".format(checkeado.get()))
    
def reiniciarVentana():
    print("estoy reiniciando la ventana")
    checkeado.set(None)
    ventana.config(text=" ")

def salir():
    window.quit()

boton_1 = tkinter.Radiobutton(window, text="soy el boton 1", variable=checkeado, value="soy el boton 1", command=seleccionaste)
boton_1.pack()  

boton_2 = tkinter.Radiobutton(window, text="soy el boton 2", variable=checkeado, value="soy el boton 2", command=seleccionaste)
boton_2.pack()

boton_3 = tkinter.Radiobutton(window, text="soy el boton 3", variable=checkeado, value="soy el boton 3", command=seleccionaste)
boton_3.pack()

ventana = Label(window)
ventana.pack()

botonReiniciar = (tkinter.Button(window, text="reiniciar", command=reiniciarVentana)).pack()
botonSalir = (tkinter.Button(window, text="leave", bg="black", fg="white", command=salir)).pack()

window.mainloop()