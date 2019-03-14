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
from tkinter import Entry
import numpy as np

LARGE_FONT = ("Verdana",12)

class AppMain(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.iconbitmap(self,default="sum.ico")
        tk.Tk.wm_title(self,"Convolución")
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand="True")
       # container.grid_rowconfigure(0)
       # container.grid_columnconfigure(0)
        
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
       
        button.pack(side=tk.TOP)
   
class PageGraph(tk.Frame):        
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graphic",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
                
        button = ttk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        
        button.pack()
        
        #Etiquetas
        text_Xn = "X[n]"
        text_Hn = "H[n]"        
            
        labeld1=tk.Label(self,text=text_Xn,font=LARGE_FONT,bd=1)
        #labeld1.grid(row=0,column=0)
        entry_Xn = Entry(self)
        #entry_Xn.grid(row=0,column=1)
        
        labeld2=tk.Label(self,text=text_Hn,font=LARGE_FONT)
        #labeld2.grid(row=1,column=0)
        entry_Hn = Entry(self)
        #entry_Hn.grid(row=1,column=1)
        
        #labeld1.pack()
        labeld1.pack(after=button,side="top")
        entry_Xn.pack()
        #si añades SIDE se va al siguiente grid
        #e1.pack(side=tk.LEFT)
        labeld2.pack()
        entry_Hn.pack()
        
        
        Yn = []
        Yi = 0
        Yf = 0
        rangeYn = []
        
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
                while Gi < center:
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
               
            
        def execute(self):
            Xn = entry_Xn.get().split(",")
            Hn = entry_Hn.get().split(",")
            print(Xn)
            print(Hn)
            
            centerX = whereIsCenter(Xn)
            centerH = whereIsCenter(Hn)
            print(centerX)
            print(centerH)
            
            Xi = getGi(Xn,centerX)  #Xi : Start of X(n)
            Xf = getGf(Xn,centerX)  #Xf : End of X(n)
            Hi = getGi(Hn,centerH)  #Hi : Start of H(n)
            Hf = getGf(Hn,centerH)  #Hf : End of H(n)
            
            print(Xi)
            print(Xf)
            print(Hi)
            print(Hf)
            
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
            Yn = np.convolve(Xn,Hn).tolist()
            Yi = Xi+Hi
            Yf = Xf+Hf+1
            rangeYn = np.arange(Yi,Yf)
            
            print("\nY[n]: ",Yn)
            print("Yi: ",Yi)
            print("Yf: ",Yf-1)
            print("Range: ",rangeYn)
            
            print("\n\n")
            """
            f = Figure(figsize=(5,5),dpi=100)
            first = f.add_subplot(121)
            markerline, stemlines, baseline = first.stem(rangeXn, Xn, '-.')
            first.setp(baseline, color='r', linewidth=2)
            first.title("X[n]")
            first.grid()
            
            second = f.add_subplot(122)
            markerline, stemlines, baseline = second.stem(rangeHn, Hn, '-.')
            second.setp(baseline, color='r', linewidth=2)
            second.title("H[n]")
            second.grid()"""
        
        data = tk.Button(self,text="Convolve",command=execute(self))        
        data.pack()
        
        sp = tk.Label(self,text="")
        sp.pack()
        
        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(121)
        a.plot([1,2,3,4,5,6],[3,4,6,1,8,7])
        b = f.add_subplot(122)
        b.plot([1,4,2,8,5,9],[3,4,6,1,8,7])
            
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand="True")
            
        
raiz = AppMain()
raiz.mainloop()
