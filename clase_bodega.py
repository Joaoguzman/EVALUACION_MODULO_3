import random 
import pickle
from pathlib import Path

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
        self.bodega_pickle = []
    
    def recibir_flores(self, numero_flores_recibir):
        for numero in range(0,numero_flores_recibir):
            especie_escogida = random.choice(especies_flores)
            tamaño_escogido = random.choice(tamaño_flores)
            flor_definida = str(especie_escogida+tamaño_escogido)
            print(numero, flor_definida)
            self.lista_bodega.append(flor_definida)

    def sistematizacion_bodega(self): #actualiza el diccionario
        for item in self.lista_bodega:
            if item not in self.bodega_sistematizada.keys():
                self.bodega_sistematizada[item] = self.lista_bodega.count(item)

    def actualizar_archivo(self):#crear archivo y guardar diccionario en un archivo (pikle)
        if Path("bodega_actualizada.dat").is_file():
            print ("File exist")
            with (open("bodega_actualizada.dat", "rb")) as pf:
                self.pickle_abierto = pickle.load(pf)
            for clave, elemento in self.bodega_sistematizada.items():
                if clave in self.pickle_abierto.keys():
                    self.pickle_abierto[clave] += elemento
                else:
                    self.pickle_abierto[clave] = elemento
            with(open("bodega_actualizada.dat", "wb")) as pf:
                pickle.dump(self.pickle_abierto, pf)
        else:
            with(open("bodega_actualizada.dat", "wb")) as pf:
                pickle.dump(self.bodega_sistematizada, pf) 
    def buscar_flor(self, codigo_flor):
        if codigo_flor in self.bodega_sistematizada.keys():
            return print(self.bodega_sistematizada.items())
        else:
            print("La flor no se encuentra en el inventario")
    
    def abrir_pickle(self):
        with (open("bodega_actualizada.dat", "rb")) as openfile:
            while True:
                try:
                    self.bodega_pickle.append(pickle.load(openfile))
                except EOFError:
                    break
            print(self.bodega_pickle)

#funcion generar flores (sin guardarlas: flor generada + lista de flores iniciales)
#actualizar diccionario: te entrega diccionario tal como lo pase o con modificaciones: se guarda en archivo diccionario
#archivo registro de flores: llegan flores una por una 
#archivo de diccionario (se sobre escribe)

#FUNCION QUE SOBRE ESCRIBA EL ARCHIVO ORIGINAL 

bodega1 = Bodega("bodega.txt")
x = bodega1.recibir_flores(100)
#bodega1.listar_bodega()
bodega1.sistematizacion_bodega()
print(bodega1.bodega_sistematizada)
bodega1.actualizar_archivo()
bodega1.abrir_pickle()
#generar lista de flores
#transformo a diccionario
#se guarda en dat
#lo leo y le agrego las flores generadas
#dos archivos: uno de lista de flores generadas
#siempre vamos a trabajar con archivo de diccionario