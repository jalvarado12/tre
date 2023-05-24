from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.audio import SoundLoader
import random
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl


archivo = 'reporte.xlsx'
libro = xl.load_workbook(archivo)
df = pd.read_excel(archivo, engine='openpyxl')

hoja = libro.active



def agregar_colores():
        valor_colores = hoja["B2"].value
        hoja["B2"].value = valor_colores + 1
        libro.save(archivo)

def agregar_suma():
        valor_suma = hoja["B3"].value
        hoja["b3"].value = valor_suma + 1
        libro.save(archivo)

def agregar_abecedario():
        valor_abecedario = hoja["B4"].value
        hoja["B4"].value = valor_abecedario + 1
        libro.save(archivo)
    
def agregar_resta():
        valor_resta = hoja["B5"].value
        hoja["B5"].value = valor_resta + 1
        libro.save(archivo)

def agregar_animal():
        valor_animal = hoja["B6"].value
        hoja["B6"].value = valor_animal + 1
        libro.save(archivo)
    
def agregar_numeros():
        valor_numeros = hoja["B7"].value
        hoja["B7"].value = valor_numeros + 1
        libro.save(archivo)

def graficar():
            
    df = pd.read_excel(archivo, engine='openpyxl')

    x  =   df["MODULOS "]
    y  =   df["ACIERTOS"]

    plt.plot(x,y)
    plt.xlabel("Modulos")
    plt.ylabel("Aciertos")
    plt.title("Gráfica de aciertos")

    ruta_guardado = "C:\\Users\\Usuario\\OneDrive - Universidad del rosario\\Escritorio\\proyecto\\reporte.png"
    plt.savefig(ruta_guardado)



class Ui(ScreenManager):
    pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        Builder.load_file('design.kv')
        return Ui()
    

    def generar_suma(self):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9 - num1) # El segundo número debe ser lo suficientemente grande para que la suma no supere 9
        return f"{num1} + {num2}"

    def calcular_suma(self, texto):
        # Intentar evaluar la expresión matemática
        try:
            resultado = eval(texto)
        except (SyntaxError, TypeError):
            resultado = None
        return resultado

    def verificar_suma(self,suma,respuesta):
        if(self.calcular_suma(suma) == respuesta):
            agregar_suma()
            graficar()
            return "Es correcto"
        else:
            return "Resultado incorrecto, prueba con otro número"
        
    def generar_resta(self):
        num1 = random.randint(0, 9)  # Generar un número aleatorio entre 0 y 9 (inclusive)
        num2 = random.randint(0, num1)  # Generar otro número aleatorio entre 0 y el primer número generado (inclusive)
        return f"{num1} - {num2}"

    def calcular_resta(self, texto):
        # Intentar evaluar la expresión matemática
        try:
            resultado = eval(texto)
        except (SyntaxError, TypeError):
            resultado = None
        return resultado

    def verificar_resta(self,resta,respuesta):
        if(self.calcular_resta(resta) == respuesta):
            agregar_resta()
            graficar()
            return "Es correcto"
        else:
            return "Resultado incorrecto, prueba con otro número"

    def escoger_animal(self):
        animales = ["gato","elefante","leon","tigre","vaca","pato"]
        return animales[random.randint(0,len(animales)-1)]

    def reproducir_sonido(self,sonido):
        # Cargar el archivo de sonido
        sound = SoundLoader.load(f'audios/{sonido}.mp3')
        # Verificar si el archivo de sonido se ha cargado correctamente
        if sound:
            # Reproducir el sonido
            sound.play()
    
    def verificar_animal(self,animal,escogido):
        if(animal == escogido):
            agregar_animal()
            graficar()
            return "Respuesta correcta"
        else:
            return "Respuesta incorrecta"
        
        



graficar() 

if __name__ == '__main__':
    MainApp().run()

