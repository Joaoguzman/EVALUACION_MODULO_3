import random 
import pickle
from pathlib import Path

diccionario_flores = {"lilium":"l", "rosa":"r", "gardenia":"g", "alheli":"a", "begonia":"b", "jazmin":"j", "tulipan":"t"}
especies_flores = ["a", "b", "j", "l", "r", "g", "f", "t","c"]
tamaño_flores = ["S", "L"]

class Bodega ():
    def __init__(self): #inicializa la clase con un argumento nombre de archivo
        self.__nombre_archivo = "bodega_actualizada.dat"
        self.lista_bodega = []
        self.bodega_sistematizada = {}
        self.bodega_pickle = []
        self.__crear_archivo()

    def __crear_archivo(self):
        if Path(self.__nombre_archivo).is_file():
            print ("File exist")
        else:
            data = {}
            with open(self.__nombre_archivo, 'wb') as file:
                pickle.dump(data, file)
                
    def recibir_diccionario(self, dic):
        self.bodega_sistematizada = dic
        with(open("bodega_actualizada.dat", "wb")) as pf:
                pickle.dump(self.bodega_sistematizada, pf)
        
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
                pickle_abierto = pickle.load(pf)
            for clave, elemento in self.bodega_sistematizada.items():
                if clave in pickle_abierto.keys():
                    pickle_abierto[clave] += elemento
                else:
                    pickle_abierto[clave] = elemento
            with(open("bodega_actualizada.dat", "wb")) as pf:
                pickle.dump(pickle_abierto, pf)
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
            return self.bodega_sistematizada