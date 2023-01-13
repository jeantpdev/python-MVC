#from turtle import width
from ventana_principal import *
from tkinter import ttk
import tkinter as tk
from tkinter import *

class Ventana_Tres_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configurar_ventana()
        self.decorar_ventana()
        
    def configurar_ventana(self):
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.title("Chatbot con openAI") #Aplica un titulo a la ventana
        self.parent.config(bg="#0D1216")
        self.parent.resizable(0,0)
        self.dimensiones_ventana()

    def decorar_ventana(self):

        self.lblTitulo_servicio=tk.Label(self.parent, text = "CHATBOT con OpenAI")
        self.lblTitulo_servicio.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblTitulo_servicio.grid(row = 0, column = 0, padx = 0, pady = 5, ipadx = 0, ipady = 10)

        myscroll = Scrollbar(self.parent)
        self.historial_de_conversacion = Listbox(self.parent, yscrollcommand = myscroll.set, borderwidth = 1, relief = "solid")
        self.historial_de_conversacion.grid(row = 1 ,column = 0, padx = 10, pady = 5, ipadx = 325, ipady = 120)

        self.lblTexto_usuario = tk.Label(self.parent,text="Escribe acá")
        self.lblTexto_usuario.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '12', 'bold'))
        self.lblTexto_usuario.grid(row = 2,column = 0,ipady = 5)

        self.txtEntrada_texto_usuario = tk.Entry(self.parent, borderwidth=1, relief="solid")
        self.txtEntrada_texto_usuario.grid(row = 3,column = 0,padx = 10, pady = 5, ipadx = 80, ipady = 2)

        self.botones_widget()

    def dimensiones_ventana(self): #Funcion que va dentro de configurar_ventana()
        wventana = 800
        hventana = 630

        #Calcula el tamaño de la resolucion de la pantalla
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def botones_widget(self):      #Funcion que va dentro de configurar_ventana()
        self.btnEnviar_texto_hacia_IA = tk.Button(self.parent,text="Enviar", width=10,height=1)
        self.btnEnviar_texto_hacia_IA.grid(row = 4, column = 0,pady = 5)
