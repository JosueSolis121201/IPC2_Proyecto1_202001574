
from calendar import c
from turtle import clear
from xml.etree.ElementTree import parse, Element
from xml.dom import minidom


class Programa:
    def __init__(self,xml):
        self.archivo = xml


    def leerXML(self):
        file = open("C:\\Users\\josue\\Desktop\\IPC2\\IPC2_Proyecto1_202001574\\prueba.xml",mode="r",encoding="utf8")
        leerArchivo = file.read()
        file.close()
        leerArchivo = leerArchivo.replace("”","\"")
        leerArchivo = leerArchivo.replace("”","\"")
        print(leerArchivo)
        doc = minidom.parseString(leerArchivo)
        R = doc.getElementsByTagName("R")[0]
        print(R.firstChild.data)
        piso = doc.getElementsByTagName("piso")
        for piso in piso:
            sid = piso.getAttribute("nombre")
            R = piso.getElementsByTagName("R")[0]
            C = piso.getElementsByTagName("C")[0]
            print("nombre:%s " % sid)
            print("R:%s" % R.firstChild.data)
            print("C:%s" % C.firstChild.data)

        #           

archivo = Programa()
archivo.leerXML()