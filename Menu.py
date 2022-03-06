
from calendar import c
import imp
from turtle import clear
from xml.etree.ElementTree import parse, Element
from xml.dom import minidom
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename       #complemento para el explorador ^^^
from matriz import Matriz
from lecturaLista import ListaDoble

class Programa:
    def __init__(self):
        self.listamatrices = ListaDoble()
        self.contador=0
        self.menu()

        #self.menu()



    def leerXML(self):
        Tk().withdraw()
        archivoxml=""
        try:
            filename = askopenfilename(title="Seleccione un archivo",
                                            filetypes=[("Archivos","*.xml"), 
                                                        ("All files","*")])
                                                        
            print(filename)
            with open(filename) as infile:
                archivoxml=infile.read().strip()       #limpia cualquier carracter "corrupto"

        except:
            print("no se selecciono ningun archivo")
            print("error")
            
            
            with open(filename) as infile:
                archivoxml=infile.read().strip()       #limpia cualquier carracter "corrupto"
            return


        #Lectura
        #print(archivoxml)

        file = open("C:\\Users\\josue\\Desktop\\IPC2\\IPC2_Proyecto1_202001574\\prueba.xml",mode="r",encoding="utf8")
        leerArchivo = file.read()
        file.close()    
        leerArchivo = leerArchivo.replace("”","\"")
        leerArchivo = leerArchivo.replace("”","\"")
        #print(leerArchivo)

        doc = minidom.parseString(archivoxml)
        piso = doc.getElementsByTagName("piso")
        #print(piso)

        self.listamatrices = ListaDoble()
        self.contador = 0
        

        for piso in piso:
            sid = piso.getAttribute("nombre")
            patronid = piso.getAttribute("patron")
            R = piso.getElementsByTagName("R")[0].firstChild.data
            C = piso.getElementsByTagName("C")[0].firstChild.data
            S = piso.getElementsByTagName("S")[0].firstChild.data
            F = piso.getElementsByTagName("F")[0].firstChild.data
            patron = piso.getElementsByTagName("patron")[0].firstChild.data
            patron_futuro = piso.getElementsByTagName("patron")[1].firstChild.data

            sid=str(sid).strip().replace("\n","").replace("\t","").replace("\r","")
            patronid=str(patronid).strip().replace("\n","").replace("\t","").replace("\r","")
            patron=str(patron).strip().replace("\n","").replace("\t","").replace("\r","")
            patron_futuro=str(patron_futuro).strip().replace("\n","").replace("\t","").replace("\r","")



            print("nombre:%s " % sid)
            print("R:%s" % R)
            print("C:%s" % C)
            print("S:%s" % S)
            print("F:%s" % F)
            print("patron:%s" % patron)
            print("patron Futuro:%s" % patron_futuro)
            

            self.listamatrices.agregar(Matriz(R,C,F,S,sid,patronid,patron,patron_futuro)) # pasando datos a clase matriz.py
            self.contador=self.contador+1
           
            print("******lista*****")
            print(self.listamatrices)
            print(self.contador)



       # self.listamatrices.graficar_todo()
        #self.listamatrices.costo_todos()



    def EjecutarUnaMatriz(self):

        for i in self.contador:
            pass

    def menu(self):
            while True:
                x=input('''
        1. Cargar datos
        2. Generar piso actual
        3. Costes del piso futuro
        4. Generar Todo
        5. Salir
        Escoja una opcion:''')
                if x =="1":
                    self.leerXML()

                elif x =="2":
                    self.listamatrices.graficar_original(input("introdusca el nombre de el piso deseado:"))

                elif x =="3":
                    y=input("introdusca el nombre de el piso deseado:")
                    self.listamatrices.graficar_futuro(str(y))
                    self.listamatrices.costo_uno(str(y))
                elif x =="4":
                    self.listamatrices.graficar_todo()
                    self.listamatrices.costo_todos()
                elif x =="5":
                    print("saliendo...")
                    break
                else:
                    print("Escoja un dato valido porfavor:")

                  
archivo = Programa()
