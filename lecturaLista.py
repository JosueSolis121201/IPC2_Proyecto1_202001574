
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

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


#    def imprimirG(self,):   
#       graph = ""

#       puntero= self.end
#       while puntero != None:
#          print(puntero.dato)
#          graph = graph + "N+"id(puntero)"[BLA BLA]" + "N"+id(puntero)"->" + "N"+id(puntero.siguiente)
#         puntero = puntero.anterior
#
#       escribir(graph)
#
#      cmd.("graph - text.txt")


    def imprimir(self,):
        puntero= self.end
        while puntero != None:
            print(puntero.dato)
            puntero = puntero.anterior
          





lista = ListaDoble()
for i in [1,2,3,4,5,6,7,8]:
    lista.agregar(i)


lista.imprimir()
