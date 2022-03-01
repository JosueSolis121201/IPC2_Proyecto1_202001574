import string


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


    def imprimir(self,):
        puntero= self.end
        while puntero != None: 
            if hasattr(puntero.dato, 'imprimir'): 
                puntero.dato.imprimir()
            else:
                print(puntero.dato)
            puntero = puntero.anterior
          



#lista = ListaDoble()
#for i in [1,2,3,4,5,6,7,8]:
#    lista.agregar(i)


#    lista.imprimir()


