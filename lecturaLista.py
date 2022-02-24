from calendar import c
from turtle import clear
from xml.etree.ElementTree import parse, Element



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
          
        print("1")




#lista = ListaDoble()
#for i in [1,2,3,4,5,6,7,8]:
#    lista.agregar(i)


#    lista.imprimir()

class lectorXML:
    def __init__(self,xml):
        self.archivo = xml


    def leerXML(self):
        nombre_archivo ="datos.xml"
        doc_xml = parse(nombre_archivo)
        raiz = doc_xml.getroot()    #ejecuta raiz
        print(raiz)

        #remocion de elementos
        #raiz.remove(raiz.find(""))

        #insertar un nuevo nodo
        raiz.get(raiz.find("empleado"))   

        nodo_email = Element("elmail")
        nodo_email.text="clientes@asdsad"

        raiz.insert(1, nodo_email)

        #Estructura archivo xml modificado
        nombre_archivo_nuevo = "almacen_nuevo.xml"
        doc_xml.write(nombre_archivo_nuevo, xml_declaration=True)

        #           

archivo = lectorXML("")
archivo.leerXML()

