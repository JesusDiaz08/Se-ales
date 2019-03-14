# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:11:13 2018

@author: kaimo
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana",12)

"""

""" """Establecemos la raíz, la cual nos servirá como ventana""" """
raiz = Tk()
raiz.title("Convolucion")   #Establecemos el título de la ventana
raiz.resizable(True,True)   #Permitimos que se edite la longitud y la altitud.
raiz.iconbitmap("sum.ico")  #Ponemos el icono de la suma en la ventana
#raiz.geometry("650x350")    Dimensionamos a la pantalla.
raiz.config(bg="black")     #Ponemos un background de color negro.



"""  """Establecemos el frame dentro de la raiz""" """
myFrame = Frame()           #Creamos el frame.
#myFrame.pack()              #Empaquetamos el frame: Lo metemos dentro de la raiz.
myFrame.pack(side="left",anchor="n")
myFrame.pack(fill="both",expand="True");
myFrame.config(bg="red")    #Establecemos el background de color rojo
myFrame.config(width="650", height="350");  #Dimensionamos al hijo de la raiz
myFrame.config(bd="10")
myFrame.config(relief="groove")     #Tipo de borde del frame.

"""

class AppMain(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.iconbitmap(self,default="sum.ico")
        tk.Tk.wm_title(self,"Convolución")
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand="True")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        for F in (StartPage,PageGraph):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        
        team = "Díaz Medina Jesús Kaimorts.\n"+"Castro Karla\n"+"Oswaldo\n"+"Vargas Romero Erick Efraín\n"
        gpo = "\n\n\n3CV7.\nTeoría de Comunicaciones y Señales"
        pract = "\n\n\n\nPRÁCTICA II: CONVOLUCIÓN"
        
        info = team + gpo + pract        
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text=info,font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button = ttk.Button(self,text="View graphic",
                            command=lambda: controller.show_frame(PageGraph))
        button.pack()

class PageGraph(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graphic",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
                
        button = ttk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        """
        #Creando la etiqueta de entrada
        xn = tk.Label(self,text="X(n) = ", font=LARGE_FONT)
        xn.pack(pady=20, padx=70)    """
        
        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(111)
        
        a.plot([1,2,3,4,5,6],[3,4,6,1,8,7])
        
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand="True")
        
        
        g = Figure(figsize=(5,5),dpi=100)
        b = g.add_subplot(111)
        
        b.plot([1,4,2,8,5,9],[3,4,6,1,8,7])
        
        canvasG = FigureCanvasTkAgg(g,self)
        canvasG.show()
        canvasG.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand="True")
        
        
raiz = AppMain()
raiz.mainloop()