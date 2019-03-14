# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:30:28 2018

@author: kaimo
"""

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np

def whereIsCenter(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            return indice        
        indice += 1

"""
@name: getGi
@desc: This function return the Xi, initial index
@param: (list)Xn, (int)center
@return: Gi: Initial index
"""
def getGi(Xn,center):
    Gi = 0
    if center!=0:
        while Gi < center:         #Vemos desde donde inicia la funcion X(n)
            Gi += 1
        Gi = (-1)*Gi
    else:
        Gi = 0
    
    return Gi

"""
@name: getGf
@desc: This function return the Xf, final index
@param: (list)Xn, (int)center
@return: Gi: Final index
"""
def getGf(Xn,center):
     return len(Xn)-center-1


"""
@name: rangeToGraph
@desc: This function return the Xi, initial index, and Xf, final index.
       In others words, indicates where the function starts from,
       and where it ends from
@param: list, (int)center
@return: arange
"""
def rangeToGraph(list,int):
    Gi = getGi(list,int)  #Xi : Inicio de X(n)
    Gf = getGf(list,int)  #Xf : Fin de X(n)
    
    return np.arange(Gi,Gf)

def convertFunc(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            list[indice] = list[indice].replace('*','')
        indice += 1
    return list

"""
@name: infoGn
@desc: This function gives information like:
            - G(n) : Elements of function
            - Center G(n): Central element of function
            - Gi : Start index where the function starts from
            - Gf : Final index where the function starts from
            
@param: list, (int)center,Gi,Gf
"""
def infoGn(list,center,Gi,Gf):
    print("G(n) = ",list)
    print("Center G(n): ",center)
    print("Gi: ",Gi)
    print("Gf: ",Gf)


LARGE_FONT = ("Verdana",12)

Yn = []
Yi = 0
Yf = 0
rangeYn = []

raiz = Tk()
raiz.title("Convolucion")   #Establecemos el título de la ventana
raiz.resizable(True,True)   #Permitimos que se edite la longitud y la altitud.
raiz.iconbitmap("sum.ico")  #Ponemos el icono de la suma en la ventana
raiz.geometry("250x150")    #Dimensionamos a la pantalla.


myFrame = Frame(raiz,width=500,height=400)
myFrame.config(width="350", height="150");
myFrame.pack()


#Etiquetas
text_Xn = "X[n] = "
text_Hn = "H[n] = "
text_info = "Por favor, indique el centro con un '*' después del punto"

#Dibujamos las etiquetas y las entradas de texto
label_Xn = Label(myFrame,text=text_Xn,fg="blue",font=LARGE_FONT)
label_Xn.grid(row=1,column=0,padx=10,pady=10,sticky="w")

label_Hn = Label(myFrame,text=text_Hn,fg="blue",font=LARGE_FONT)
label_Hn.grid(row=2,column=0,padx=10,pady=10,sticky="w")

entry_Xn = Entry(myFrame)
entry_Xn.grid(row=1,column=1,padx=10,pady=10,sticky="w")
entry_Xn.config(justify="left")

entry_Hn = Entry(myFrame)
entry_Hn.grid(row=2,column=1,padx=10,pady=10,sticky="w")
entry_Xn.config(justify="left")


#Agregamos el botón para enviar
def getFunctions():
    Xn = entry_Xn.get().split(",")
    Hn = entry_Hn.get().split(",")
    print(Xn)
    print(Hn)
    centerX = whereIsCenter(Xn)
    centerH = whereIsCenter(Hn)
    Xi = getGi(Xn,centerX)  #Xi : Start of X(n)
    Xf = getGf(Xn,centerX)  #Xf : End of X(n)
    Hi = getGi(Hn,centerH)  #Hi : Start of H(n)
    Hf = getGf(Hn,centerH)  #Hf : End of H(n)
    
    rangeXn = rangeToGraph(Xn,centerX)  #Getting range to draw X(n)
    rangeHn = rangeToGraph(Hn,centerH)  #Getting range to draw H(n)
    
    #Convert the necessary functions
    Xn = [float(i) for i in convertFunc(Xn)] #Convert list to float list
    Hn = [float(i) for i in convertFunc(Hn)] #Convert list to float list
    
    #Information of X(n) and H(n)
    print("\n_____DATA X(n)_____\n")
    infoGn(Xn,centerX,Xi,Xf)
    print("\n_____DATA H(n)_____\n")
    infoGn(Hn,centerH,Hi,Hf)
    
    #Convolution of function
    global Yn 
    Yn= np.convolve(Xn,Hn).tolist()
    global Yi
    Yi = Xi+Hi
    global Yf
    Yf = Xf+Hf+1
    global rangeYn
    rangeYn = np.arange(Yi,Yf)
    
    print("\nY[n]: ",Yn)
    print("Yi: ",Yi)
    print("Yf: ",Yf-1)
    print("Range: ",rangeYn)
       
button_envia = Button(raiz,text="Convolve",command=getFunctions)
button_envia.pack()
   
raiz.mainloop()
