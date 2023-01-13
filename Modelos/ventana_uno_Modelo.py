from ventana_principal import *

class Ventana_Uno_Model:

    def __init__(self):
        self.texto_traducir = tk.StringVar()

    def get_texto_traducir(self):
        return self.texto_traducir

    def set_texto_traducir(self, texto_traducir):
        self.texto_traducir = texto_traducir