import string
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename       #complemento para el explorador ^^^


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None
        self.archivoxml =""

       # self.leer()


    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
       #Validamos si la lista esta vacia
        if self.head == None:
            self.head = nuevoNodo
            self.end = nuevoNodo
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            self.head.anterior = nuevoNodo
            nuevoNodo.siguiente = self.head
            self.head = nuevoNodo




    def graficar(self):
        puntero= self.end
        concateniacion=""
        while puntero != None:
            if hasattr(puntero.dato, 'imprimir'): 
                concateniacion=concateniacion + puntero.dato.string()
            else:
                print(puntero.dato)
            puntero = puntero.anterior
        return concateniacion




    def imprimir(self):
        puntero= self.end
        while puntero != None: 
            if hasattr(puntero.dato, 'imprimir'): 
                puntero.dato.imprimir()
            else:
                print(puntero.dato)
            puntero = puntero.anterior

    def graficar_original(self,nombre_buscar):
        puntero= self.end
        while puntero != None: 
            matriz = puntero.dato
            if nombre_buscar == matriz.sid:
                matriz.graficar()
            puntero = puntero.anterior

    def graficar_futuro(self,nombre_buscar):
        puntero= self.end
        while puntero != None: 
            matriz = puntero.dato
            if nombre_buscar == matriz.sid:
                matriz.graficar_futuro()
            puntero = puntero.anterior

    def graficar_todo(self):
        puntero= self.end
        while puntero != None: 
            matriz = puntero.dato
            matriz.graficar()
            matriz.graficar_futuro()
            puntero = puntero.anterior

    def costo_uno(self,nombre_buscar):
        puntero= self.end
        while puntero != None: 
            matriz = puntero.dato
            if nombre_buscar == matriz.sid:
                matriz.calcular_costos()
            puntero = puntero.anterior

    def costo_todos(self):
        puntero= self.end
        while puntero != None: 
            matriz = puntero.dato
            matriz.calcular_costos()
            puntero = puntero.anterior


    #Filtrado para archivos .data
    def leer(self):
        Tk().withdraw()
        self.archivoxml=""
        try:
            filename = askopenfilename(title="Seleccione un archivo",
                                            filetypes=[("Archivos","*.xml"), 
                                                        ("All files","*")])
            print(filename)
            with open(filename) as infile:
                self.archivoxml=infile.read().strip()       #limpia cualquier carracter "corrupto"

        except:
            print("no se selecciono ningun archivo")
            print("error")
            return


        #Lectura
        print(self.archivoxml)

        return self.archivoxml
          




