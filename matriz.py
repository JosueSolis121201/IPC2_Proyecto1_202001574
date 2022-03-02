
from lecturaLista import ListaDoble
from graphviz import Source






class Matriz:
    def __init__(self):
        self.R=2
        self.C=4
        self.F=1
        self.S= 2
        self.patron = "WBWBWWWB"
        self.patron_futuro = "BWBWWWWW"
        self.lista_filas = ListaDoble()
        self.lista_filas_futuro = ListaDoble()
        self.costo=0


      #  self.cargarPatron()
      #  self.graficar()
        
      #  self.cargarPatron_futuro()
     #   self.graficar_futuro()
        self.calcular_costos()

    def calcular_costos(self):
        self.costo=0
        patronCopia = self.patron
        self.algoritmo()
        self.voltear()
        self.patron = patronCopia


    def cargarPatron(self):
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

    def cargarPatron_futuro(self):
        contador=0
        for i in range(self.R):
            fila = Fila()
            for j in range(self.C):
                letra = self.patron_futuro[contador]
                columna = Columna(letra)
                fila.agregar_columnas(columna)
                contador=contador+1
            self.lista_filas_futuro.agregar(fila)
        self.lista_filas_futuro.imprimir()

    def algoritmo (self):
        contador=0
        costo=0
        limite=self.R*self.C
        for i in range(self.R):
            fila = Fila()
            for j in range(self.C):
                if self.patron[contador] != self.patron_futuro[contador] :       
                    if  (contador+1)%self.C !=0 and (self.patron[contador] == self.patron_futuro[contador+1] and self.patron[contador + 1] == self.patron_futuro[contador]):#intercambio izquierda 
                        costo= self.S+costo
                        self.patron = self.patron[:contador] + self.patron_futuro[contador] + self.patron[contador + 1:]
                        self.patron = self.patron[:contador + 1] + self.patron_futuro[contador + 1] + self.patron[contador + 1 + 1:]
                        print(str(contador) + " derecha")
                    elif (contador)%self.C !=0 and (self.patron[contador-1] == self.patron_futuro[contador] and self.patron[contador] == self.patron_futuro[contador-1]):#intercambio derecha 
                        costo= self.S+costo
                        self.patron = self.patron[:contador] + self.patron_futuro[contador] + self.patron[contador + 1:]
                        self.patron = self.patron[:contador  -1] + self.patron_futuro[contador - 1] + self.patron[contador + 1 - 1:]   
                        print(str(contador) + " izquierda")
                    elif  (contador)-self.C >=0 and (self.patron[contador-self.C] == self.patron_futuro[contador] and self.patron[contador] == self.patron_futuro[contador-self.C] ):#intercambio arriba 
                        costo= self.S+costo
                        self.patron = self.patron[:contador] + self.patron_futuro[contador] + self.patron[contador + 1:]
                        self.patron = self.patron[:contador  -self.C] + self.patron_futuro[contador - self.C] + self.patron[contador + 1 - self.C:]   
                        print(str(contador) + " arriba")
                    elif (contador)+self.C <limite and (self.patron[contador] == self.patron_futuro[contador+self.C] and self.patron[contador+self.C] == self.patron_futuro[contador] ):#intercambio abajo 
                        costo= self.S+costo
                        self.patron = self.patron[:contador] + self.patron_futuro[contador] + self.patron[contador + 1:]
                        self.patron = self.patron[:contador  +self.C] + self.patron_futuro[contador + self.C] + self.patron[contador + 1 + self.C:]   
                        print(str(contador) + " abajo")
                contador=contador+1
        self.costo=costo+self.costo
        print(str(self.costo) + " costo")

    def voltear (self):
        contador=0
        costo = 0
        for i in range(self.R*self.C):
            if self.patron[contador] != self.patron_futuro[contador] :       
                costo= self.F+costo
                print(str(contador) + " voltear")
                self.patron = self.patron[:contador] + self.patron_futuro[contador] + self.patron[contador + 1:]
            contador = contador + 1
        self.costo=costo+self.costo    
        print(str(self.costo) + " costo")


    def graficar(self):
        inicio = """digraph html {
 abc [shape=none, margin=0, label=<
 <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">"""
        final ="""</TABLE>>];}"""
 
        medio = self.lista_filas.graficar()
        documento = inicio + medio + final
        g = Source(documento, filename='hello.gv',format="png")
        g.view()

    def graficar_futuro(self):
        inicio = """digraph html {
                    abc [shape=none, margin=0, label=<
                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">"""
        final ="""</TABLE>>];}"""
 
        medio = self.lista_filas_futuro.graficar()
        documento = inicio + medio + final
        g = Source(documento, filename='hello2.gv',format="png")
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
