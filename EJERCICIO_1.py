##crear lista de radio button que muestre la opcion que se ha seleccionado y que contenga un boton de reinicio 
#para que deje todo como al principio. Al principio no debe habr nada seleccionado


from tkinter import *
import tkinter
from turtle import width

##crea la ventana
window = tkinter.Tk()
var = IntVar()
def seleccionado ():
    
    print("seleccionaste la opcion: ", str(var.get()))

def restart():   # ESTA ES LA SENTENCIA QUE DA ORIGEN A LA CONSULTA
    window.quit()  
    print("adios")
  
##crea el boton
BOTON_1 = tkinter.Radiobutton(window, text= "soy el boton 1", variable=var, value=1, command=seleccionado)
BOTON_1.pack(ipadx=50, ipady=50)

BOTON_2 = tkinter.Radiobutton(window, text= "soy el boton 2", variable=var, value=2, command=seleccionado)
BOTON_2.pack(ipadx=50, ipady=51)

BOTON_3 = tkinter.Radiobutton(window, text= "soy el boton 3", variable=var, value=3, command=seleccionado)
BOTON_3.pack(ipadx=50, ipady=52)

BOTON_4 = tkinter.Radiobutton(window, text= "soy el boton 4",variable=var, value=4, command=seleccionado)
BOTON_4.pack(ipadx=50, ipady=53)

reinicio = tkinter.Button(window, text="reiniciar", command=restart)
reinicio.pack(ipadx=50, ipady=55)


window.mainloop()
