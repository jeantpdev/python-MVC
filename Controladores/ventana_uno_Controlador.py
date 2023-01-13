from ventana_principal import *
from Modelos.ventana_uno_Modelo import *
from Vistas.ventana_uno_Vista import *
import tkinter as tk
import nlpcloud
import json

class Ventana_Uno_Controller:

    def __init__(self, root):
        self.model = Ventana_Uno_Model()
        self.view = Ventana_Uno_View(root)

        self.view.btnGuardar_texto_escrito.config(command=self.guardar_texto_a_traducir)
        self.view.btnMostrar_traduccion.config(command=self.traducir_texto)

    def guardar_texto_a_traducir(self):
        try:
            self.model.set_texto_traducir(self.view.txtTraducir.get())
            print(self.model.get_texto_traducir())
        except Exception as e:
            print(e)

    def existe_historial(self):
        try:
            with open('historial.json') as archivo:
                return True
        except FileNotFoundError as e:
            return False

    def devolver_respuestas(self,nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2):
        diccionario_generado = {}
        diccionario_generado = {espacio_1 : valor_espacio_1, espacio_2 : valor_espacio_2}
        respuesta_final = {nombre_servicio: diccionario_generado}
        return respuesta_final

    def crear_traduccion_json(self, nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2):

        if self.existe_historial() == True:
            nuevos_datos = self.devolver_respuestas(nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2)
            with open("historial.json",encoding="utf-8") as archivo_json:
                datos = json.load(archivo_json)
                datos.append(nuevos_datos)
            with open("historial.json", 'w',encoding="utf-8") as archivo_json:
                json.dump(datos, archivo_json, indent=3, ensure_ascii=False)
                print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")
        else:
            with open("historial.json", 'w',encoding="utf-8") as archivo_json:
                historial = []
                historial.append(self.devolver_respuestas(nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2))
                json.dump(historial, archivo_json, indent=3, ensure_ascii=False)
                print(archivo_json.name+" creado exitosamente")
                print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")      

    def comboBox_seleccion_idioma_traducir(self):
        if self.view.combo_idiomas.get() == "Español":
            return "spa_Latn"
        if self.view.combo_idiomas.get() == "Alemán":
            return "deu_Latn"
        if self.view.combo_idiomas.get() == "Portugués":
            return "por_Latn"
        if self.view.combo_idiomas.get() == "Ruso":
            return "rus_Cyrl"
        if self.view.combo_idiomas.get() == "Coreano":
            return "kor_Hang"
        if self.view.combo_idiomas.get() == "Japones":
            return "jpn_Jpan"
        if self.view.combo_idiomas.get() == "Inglés":
           return "eng_Latn"
    
    def detectar_idioma(self,texto): #Primer servicio
        token = "1c56cb1a8a4b5cb1079f2f2e0c89321585206468"
        client = nlpcloud.Client("python-langdetect", token)
        lang = client.langdetection(texto)

        a = lang.get('languages')
        listapy = a[0]
        listafinal = listapy.items()
        idioma = list(listafinal)[0][0]

        if   idioma == "es": return "spa_Latn"

        elif idioma == "de": return "deu_Latn"

        elif idioma == "pt": return "por_Latn"

        elif idioma == "ru": return "rus_Cyrl"

        elif idioma == "ko": return "kor_Hang"

        elif idioma == "ja": return "jpn_Jpan"

        elif idioma == "en": return "eng_Latn"

        else:                return print("No se detecta el idioma")
    
    def traducir_texto(self): #Segundo servicio
        #Se guarda el idioma al que se va a traducir el texto ingresado
        idioma_a_traducir_seleccionado = self.comboBox_seleccion_idioma_traducir()

        #Se guarda el texto para poder ser traducido
        texto_escrito = self.model.get_texto_traducir()

        #Se recibe en qué idioma fue escrito el texto anteriormente escrito (variable texto)
        idioma_escrito_detectado = self.detectar_idioma(texto_escrito)

        #Según el idioma en el que fue escrito el texto, se compara que no sea el mismo al que se quiera traducir, es decir, no se pueda traducir del español al español
        if idioma_escrito_detectado == idioma_a_traducir_seleccionado:
            print("No puedes traducir al mismo idioma")

        else:
            client = nlpcloud.Client("python-langdetect","1c56cb1a8a4b5cb1079f2f2e0c89321585206468",gpu=False)
            texto_traducido = client.translation(texto_escrito, source = idioma_escrito_detectado, target = idioma_a_traducir_seleccionado)
            self.view.lblres['text'] = self.traducir_texto()
            self.crear_traduccion_json("Traducción de textos:", "Texto a traducir", texto_escrito, "Texto traducido:", texto_traducido)
            
