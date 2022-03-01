
from numpy import concatenate
from lecturaLista import ListaDoble
from graphviz import Source






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

        self.graficar()

    def graficar(self):
        inicio = """digraph html {
 abc [shape=none, margin=0, label=<
 <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">"""
        final ="""</TABLE>>];}"""
 
        medio = self.lista_filas.graficar()
        documento = inicio + medio + final
        g = Source(documento, filename='hello.gv',format="png")
        g.view()
    
      



class Fila:
    def __init__(self):
        self.lista_columnas=ListaDoble()
    
    def agregar_columnas(self,columna):
        self.lista_columnas.agregar(columna)
        
    def imprimir(self):
        print("//////")
        self.lista_columnas.imprimir()

    def string(self):
        concatenacion=self.lista_columnas.graficar()
        return "<TR>"+concatenacion+"</TR>\n"
        

class Columna:
    def __init__(self,espacio):
        self.espacio =  espacio
    
    def imprimir(self):
        print(self.espacio)

    def string(self):
        concateniacion=self.espacio
        inicio = ""
        if concateniacion == "B":
            inicio = "<TD BGCOLOR=\"black\">"
        else:
           inicio= "<TD BGCOLOR=\"white\">"
        return inicio+concateniacion+"</TD>"


a = Matriz()
