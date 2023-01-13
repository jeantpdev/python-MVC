from ventana_principal import *
from tkinter import ttk
import tkinter as tk
from tkinter import *
class Ventana_dos_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.decorar_ventana()


    def configurar_ventana(self):
        self.parent.config(bg = "#0D1216")
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.title("Analisis de sentimientos y creación de preguntas") #Aplica un titulo a la ventana
        self.dimensiones_ventana()
        self.parent.resizable(0,0)

    def decorar_ventana(self):
        self.lblFrameTitulo_servicio_sentimiento = tk.LabelFrame(self.parent, text = "Servicios")
        self.lblFrameTitulo_servicio_sentimiento.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '25', 'bold'))
        self.lblFrameTitulo_servicio_sentimiento.grid(row = 0, column = 0, padx = 40, pady = 5, ipady = 10, ipadx = 20)
        
        self.lblInstruccionesSentimiento = tk.Label(self.lblFrameTitulo_servicio_sentimiento, text = "Esta ventana cuenta con dos servicios\nPuedes analizar el sentimiento que puede generar un texto,\ny tambien puedes generar una lista según lo que se le escriba")
        self.lblInstruccionesSentimiento.config(bg="#0D1216", fg = "white", font = ('Roboto', '17',))
        self.lblInstruccionesSentimiento.grid(row = 1, column = 0, ipadx = 10)
        
        self.lblFrameAnalizar_sentimiento = tk.LabelFrame(self.parent, text = "Sentimiento")
        self.lblFrameAnalizar_sentimiento.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameAnalizar_sentimiento.grid(row = 1, column = 0, padx = 40, pady = 10, ipady = 20, ipadx = 80)        
        
        self.txtEntrada = tk.Entry(self.lblFrameAnalizar_sentimiento, relief="solid")
        self.txtEntrada.grid(row = 0, column = 0, ipadx = 150, padx = 10)
        
        self.lblresultado=tk.Label(self.lblFrameAnalizar_sentimiento,text = "Acá se mostrará el sentimiento generado")
        self.lblresultado.config(bg="#0D1216", fg = "white", font = ('Roboto', '15',))
        self.lblresultado.grid(row = 2, column = 0, pady = 5)
        
        self.lblFrameGenerar_Preguntas = tk.LabelFrame(self.parent, text = "Listas y preguntas")
        self.lblFrameGenerar_Preguntas.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameGenerar_Preguntas.grid(row = 2, column = 0, padx = 40, pady = 10, ipady = 20, ipadx = 5)      

        self.lblPregunta=tk.Label(self.lblFrameGenerar_Preguntas,text = "Escribe un tema para realizar preguntas:" )
        self.lblPregunta.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lblPregunta.grid(row = 1, column = 0, pady=5)
        
        self.txtEntrada_pregunta = tk.Entry(self.lblFrameGenerar_Preguntas, relief="solid")
        self.txtEntrada_pregunta.grid(row = 1, column = 1, ipadx = 20, padx = 10)

        self.lblCantidad_preguntas=tk.Label(self.lblFrameGenerar_Preguntas, text = "Escoge la cantidad de preguntas que quieres generar: ")
        self.lblCantidad_preguntas.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lblCantidad_preguntas.grid(row = 3, column = 0)

        self.txtRespuesta = tk.Text(self.lblFrameGenerar_Preguntas, relief = "solid")
        self.txtRespuesta.config(wrap = WORD, width = 50, height = 10)
        self.txtRespuesta.grid(row = 4,column = 0,padx = 10, pady = 0)
        
        self.botones_widget()
        self.botones_spinbox()
        
    def dimensiones_ventana(self): #Funcion que va dentro de configurar_ventana()
        wventana = 780#610
        hventana = 700#600
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal / 2 - wventana / 2)
        pheight = round(htotal / 2 - hventana / 2)
        self.parent.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))

    def botones_widget(self):      #Funcion que va dentro de configurar_ventana()

        self.btnEnviar = tk.Button(self.lblFrameAnalizar_sentimiento, text = "Generar", width = 10,height = 1)
        self.btnEnviar.grid(row = 0, column = 1, pady = 5)
        self.btnspin = tk.Button(self.lblFrameGenerar_Preguntas, text = "Generar", width = 10,height = 1)
        self.btnspin.grid(row = 3, column = 2, pady = 5)
        
    def botones_spinbox(self):      #Funcion que va dentro de configurar_ventana()
        current_value = 2
        self.spin_box = ttk.Spinbox(self.lblFrameGenerar_Preguntas, from_ = 2 , to = 10, textvariable = current_value, wrap = True)
        self.spin_box.grid(row = 3, column = 1, padx = 10)
