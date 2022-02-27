
from lecturaLista import ListaDoble

class Matriz:
    def __init__(self):
        self.R=2
        self.C=4
        self.F=1
        self.S= 2
        self.patron = "WBWBWWWB"
        self.lista_filas = ListaDoble()

        contador=0
        for i in range(self.R):
            fila = Fila()
            for j in range(self.C):
                letra = self.patron[contador]
                columna = Columna(letra)
                fila.agregar_columnas(columna)
                contador=contador+1
            self.lista_filas.agregar(fila)
        self.lista_filas.imprimir()

    def graficar(self):
        primerElemento = self.lista_filas.head
        if(primerElemento!=None):
            graphviz  = primerElemento.graficar()


class Fila:
    def __init__(self):
        self.lista_columnas=ListaDoble()
    
    def agregar_columnas(self,columna):
        self.lista_columnas.agregar(columna)
        
    def imprimir(self):
        print("//////")
        self.lista_columnas.imprimir()

    def graficar(self):
        return self.lista_columnas.graficar()
        

class Columna:
    def __init__(self,espacio):
        self.espacio =  espacio
    
    def imprimir(self):
        print(self.espacio)

    def graficar(self):
        return "algo"


a = Matriz()
