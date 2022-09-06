from tkinter import *
import tkinter

window = tkinter.Tk()

window.title("lista de motos disponibles")

motos = ["pulsar 135", "pulsar 200", "apache 100", "apache 250"]
listadoMotos = StringVar(value=motos)

listadoMotons = (tkinter.Listbox(window, listvariable=listadoMotos)).pack()
etiqueta = (tkinter.Label(window, text="arriba puede verificar \n el listado de motos disponibles")).pack()

window.mainloop()