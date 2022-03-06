
from lecturaLista import ListaDoble
from graphviz import Source






class Matriz:
    def __init__(self,R,C,F,S,sid,patronid,patron,patron_futuro):
        self.R=int(R)
        self.C=int(C)
        self.F=int(F)
        self.S=int(S)
        self.patron = patron
        self.patron_futuro = patron_futuro
        self.lista_filas = ListaDoble()
        self.lista_filas_futuro = ListaDoble()
        self.costo=0
        self.sid=sid
        self.patronid=patronid

        
    


        copia = self.patron
        self.cargarPatron_futuro()
        self.cargarPatron()
        self.patron = copia
      
        #self.graficar()
        #self.graficar_futuro()
        #self.calcular_costos()

    def calcular_costos(self):
        self.costo=0
        patronCopia = self.patron
        print("*******************************")
        print("Calculando Costo De: " + self.sid)
        if self.F < self.S:
            self.voltear()
        else:
            self.algoritmo()
            self.voltear()
        self.patron = patronCopia
        print("El Costo De "+self.sid+" Es:"+ str(self.costo))

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
        #self.lista_filas.imprimir()

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
        #self.lista_filas_futuro.imprimir()

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
     
    def graficar(self):
        inicio = """digraph html {
 abc [shape=none, margin=0, label=<
 <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">"""
        final ="""</TABLE>>];}"""
 
        medio = self.lista_filas.graficar()
        documento = inicio + medio + final
        g = Source(documento, filename=self.sid+'_copia.gv',format="png")
        g.view()

    def graficar_futuro(self):
        inicio = """digraph html {
                    abc [shape=none, margin=0, label=<
                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">"""
        final ="""</TABLE>>];}"""
 
        medio = self.lista_filas_futuro.graficar()
        documento = inicio + medio + final
        g = Source(documento, filename=self.sid+'_original.gv',format="png")
        g.view()
    
      



class Fila:
    def __init__(self):
        self.lista_columnas=ListaDoble()
    
    def agregar_columnas(self,columna):
        self.lista_columnas.agregar(columna)
        
    def imprimir(self):
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




