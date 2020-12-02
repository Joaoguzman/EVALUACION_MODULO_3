with open("archivo_bodega.txt", "w") as archivo:
    archivo.write("lS, lS, lS, lL, lL, lL, lL, lL, rS, rS, gS, gS, rS, rS, gL, rL, rL, rL, rL, rL")
class Archivo:
    def __init__(self,nombre):
        self.__nombre_archivo = nombre +".txt"
        self.__crear_archivo()
    
    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Inventario Iniciado")
    
    def agregar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("\n"+elemento)

#class Bodega (Archivo):
#    __init__(self,)
#    Archivo.__init__(self, __nombre_archivo)
lista_bodega = []
diccionario_stock = {}
def actualizar_stock_flores():
    with open("archivo_bodega.txt", "r") as file:
            file.read()
            file.seek(0)
            archivo_bodega = file.read()
    print(archivo_bodega)
    for indice in range(len(archivo_bodega)):
        if archivo_bodega[indice].islower() == True:
            lista_bodega.append(archivo_bodega[indice:indice+2])
    return lista_bodega

def diccionario_bodega():
    for item in lista_bodega:
        if item not in diccionario_stock.keys():
            diccionario_stock[item] = lista_bodega.count(item)
    return diccionario_stock

def 
print(actualizar_stock_flores())
print(diccionario_bodega())