import random 
import pickle

diccionario_flores = {"lilium":"l", "rosa":"r", "gardenia":"g", "alheli":"a", "begonia":"b", "jazmin":"j", "tulipan":"t"}
especies_flores = ["a", "b", "j", "l", "r", "g", "f", "t"]
tamaño_flores = ["S", "L"]

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

class Bodega (Archivo):
    def __init__(self, __nombre_archivo):
        Archivo.__init__(self, __nombre_archivo)
        self.lista_bodega = []
        self.bodega_sistematizada = {}
    
    def recibir_flores(self, numero_flores_recibir):
        for numero in range(0,numero_flores_recibir):
            especie_escogida = random.choice(especies_flores)
            tamaño_escogido = random.choice(tamaño_flores)
            flor_definida = str(especie_escogida+tamaño_escogido)
            print(numero, flor_definida)
            self.lista_bodega.append(flor_definida)
        return self.lista_bodega

    def listar_bodega(self):
        with open("archivo_bodega.txt", "r") as file:
                file.read()
                file.seek(0)
                archivo_bodega = file.read()
        print(archivo_bodega)
        for indice in range(len(archivo_bodega)):
            if archivo_bodega[indice].islower() == True:
                self.lista_bodega.append(archivo_bodega[indice:indice+2])
        return self.lista_bodega

    def sistematizacion_bodega(self): #actualiza el diccionario
        for item in self.lista_bodega:
            if item not in self.bodega_sistematizada.keys():
                self.bodega_sistematizada[item] = self.lista_bodega.count(item)
        return self.bodega_sistematizada  

    def actualizar_archivo(self):#crear archivo y guardar diccionario en un archivo (pikle)
        with open("bodega_actualizada.dat", "wb") as file:
            pickle.dump(self.bodega_sistematizada, file)
        return self.bodega_sistematizada
    
    def buscar_flor(self, codigo_flor):
        if codigo_flor in self.bodega_sistematizada.keys():
            return print(self.bodega_sistematizada.items())
        else:
            print("La flor no se encuentra en el inventario")

#funcion generar flores (sin guardarlas: flor generada + lista de flores iniciales)
#actualizar diccionario: te entrega diccionario tal como lo pase o con modificaciones: se guarda en archivo diccionario
#archivo registro de flores: llegan flores una por una 
#archivo de diccionario (se sobre escribe)

#FUNCION QUE SOBRE ESCRIBA EL ARCHIVO ORIGINAL 

bodega1 = Bodega("bodega.txt")
bodega1.recibir_flores(500)
bodega1.listar_bodega()
bodega1.sistematizacion_bodega()
print(bodega1.bodega_sistematizada)
bodega1.actualizar_archivo()
#generar lista de flores
#transformo a diccionario
#se guarda en dat
#lo leo y le agrego las flores generadas
#dos archivos: uno de lista de flores generadas
#siempre vamos a trabajar con archivo de diccionario