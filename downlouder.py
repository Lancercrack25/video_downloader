#Librerias necesarias para realizar el programa
from tkinter import *
from pytube import YouTube
#iniciamos definiendo la interfaz para el descargador de videos
rot = Tk()
rot.geometry("500x400")
rot.resizable(0,0)
rot.title("Tu propio desgargador de videos")
rot.configure(bg="black")
#parte de la interfaz para el descargador de videos
Label(rot, text="¡Descarga tus videos ya!", font='arial 20 bold', bg= "#FFFFFF").place(x=90, y=30)
link = StringVar()
Label(rot, text="Inserta el link", font='arial 14', bg= "#FFFFFF").place(x=190, y=90)
link_entrada = Entry(rot, width= 72, textvariable= link).place(x=32, y=122)
#definimos una funcion que haga la descarga correcta de los links puestos
def descargar():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(rot, text="Tu video esta listo", font='arial 14 bold', bg= "#FFFFFF").place(x=182, y=244)
#boton para que proceda a ejecutar la funcion de descarga
Button(rot, text="DESCARGAR", font='arial 14 bold', bg= "#FFFFFF", padx =2, command=descargar).place(x=182, y=240)
#mainloop para que nos descargue los videos que queramos y no se cierre despues de solo uno, el programa se cerrarara cuando tu decidas cerrarlo 
rot.mainloop()
#nota: los videos descargados se guardaran en la carpeta donde tengas este programa 