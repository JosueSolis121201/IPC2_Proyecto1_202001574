#from xml.etree.ElementTree import parse, Element



#nombre_archivo ="datos.xml"
#doc_xml = parse(nombre_archivo)
#raiz = doc_xml.getroot()
##print(raiz)

class numero:                   #Clase
    def __init__(self,digito):  #Constructor
        self.numero = digito    

    def Numero(self):           #Funcion
        print("este es el numero"+self.numero)

numero1=numero("este es 1")     #Instancias
numero1.Numero()

class letras:
    print("sadwa")