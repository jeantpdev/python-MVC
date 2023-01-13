from turtle import width
from ventana_principal import *
from tkinter import ttk
import tkinter as tk

class Ventana_Uno_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.decorar_ventana_uno()

    def configurar_ventana(self):
        self.parent.config(bg="#0D1216")
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.title("Traductor y detecciòn de lenguaje") #Aplica un titulo a la ventana
        self.parent.resizable(0,0)
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 600
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana_uno(self):
        
        self.buscador = tk.LabelFrame(self.parent, text = "Traduccion")
        self.buscador.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.buscador.grid(row = 0, column = 0, padx = 40, pady = 10)
        
        self.lblInstruccionesTraduccion = tk.Label(self.buscador, text = "Ingresa un texto al que quieres traducir\nRecuerda que el traductor detectará automáticamente \nel lenguaje en el que fue escrito\nSolamente selecciona a qué idioma lo quieres traducir.")
        self.lblInstruccionesTraduccion.config(bg="#0D1216", fg = "white", font = ('Roboto', '16',))
        self.lblInstruccionesTraduccion.grid(row = 1, column = 0)
        
        #Simple label que indica que se va a mostrar el texto traducido
        self.lblFrameTexto_traducir = tk.LabelFrame(self.parent, text = "Texto a traducir", pady = 30)
        self.lblFrameTexto_traducir.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameTexto_traducir.grid(row = 1, column = 0, padx = 40, pady = 10)
        
        #Campo donde se escribe el texto que se va a traducir posteriormente
        self.txtTraducir = tk.Entry(self.lblFrameTexto_traducir)
        self.txtTraducir.config(borderwidth = 1, relief = "solid")
        self.txtTraducir.grid(row = 0,column = 0, ipadx = 140, padx = 10)

        self.comboBox_idiomas()
    
        #Label que recibe el texto traducido
        self.lblFrameTexto_traducido = tk.LabelFrame(self.parent, text = "Texto traducido", pady = 30)
        self.lblFrameTexto_traducido.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameTexto_traducido.grid(row = 2, column = 0, padx = 40, pady = 10)
        
        self.lblres = tk.Label(self.lblFrameTexto_traducido, text = "Acá se mostrará el texto traducido", bg = "white")
        self.lblres.grid(row = 0, column = 0, ipadx = 110, padx = 10)

        self.botones_widget()

    def comboBox_idiomas(self):
        self.opcion = tk.StringVar()
        idiomas = ("Español", "Aleman", "Inglés", "Portugués", "Ruso", "Coreano", "Japones")
        self.combo_idiomas = ttk.Combobox(self.lblFrameTexto_traducir, width = 10, textvariable = self.opcion, values = idiomas)
        self.combo_idiomas.current(0)
        self.combo_idiomas.grid(row = 0, column = 1, pady = 10)

    def botones_widget(self):
        self.btnGuardar_texto_escrito = tk.Button(self.lblFrameTexto_traducir,text = "Guardar", width = 10, height = 1)
        self.btnGuardar_texto_escrito.grid(row = 1, column = 1,padx = 10, pady = 0)

        self.btnMostrar_traduccion = tk.Button(self.lblFrameTexto_traducido,text = "Mostrar", width = 10, height = 1)
        self.btnMostrar_traduccion.grid(row = 0, column = 1, padx = 10, pady = 0)
