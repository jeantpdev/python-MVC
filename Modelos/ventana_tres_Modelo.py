from ventana_principal import *

class Ventana_Tres_Model:

    def __init__(self):
        self.texto_humano = tk.StringVar()
        self.textoIA = tk.StringVar()

    def set_texto_humano(self, texto_humano):
        self.texto_humano = texto_humano

    def get_texto_traducir(self):
        return self.texto_humano
    
    def set_texto_IA(self, texto_IA):
        self.texto_IA = texto_IA

    def get_texto_IA(self):
        return self.texto_IA

        