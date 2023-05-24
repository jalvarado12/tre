import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl

archivo = 'reporte.xlsx'
libro = xl.load_workbook(archivo)


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

libro.save(archivo)

def generar_grafica(archivo):

    df = pd.read_excel(archivo, engine='openpyxl')

    x  =   df["MODULOS "]
    y  =   df["ACIERTOS"]

    plt.plot(x,y)
    plt.xlabel("Modulos")
    plt.ylabel("Aciertos")
    plt.title("Gráfica de aciertos")

    ruta_guardado = "C:\\Users\\Usuario\\OneDrive - Universidad del rosario\\Escritorio\\proyecto\\reporte.png"
    plt.savefig(ruta_guardado)
    plt.show()
    

agregar_suma()
agregar_colores()    
generar_grafica(archivo)





