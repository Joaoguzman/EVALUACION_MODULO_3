import random 
import pickle
from pathlib import Path

diccionario_flores = {"lilium":"l", "rosa":"r", "gardenia":"g", "alheli":"a", "begonia":"b", "jazmin":"j", "tulipan":"t"}
especies_flores = "abcdef"
tamaño_flores = ["S", "L"]

class Bodega ():
    def __init__(self): #inicializa la clase con un argumento nombre de archivo
        self.__nombre_archivo = "bodega_actualizada.dat"
        self.lista_bodega = []
        self.__crear_archivo()

    def __crear_archivo(self):
        if Path(self.__nombre_archivo).is_file():
            print ("File exist")
        else:
            with open(self.__nombre_archivo, 'wb') as file:
                pickle.dump({"Inicio":0}, file)
                
    def recibir_flores(self, numero_flores_recibir):
        for numero in range(0,numero_flores_recibir):
            especie_escogida = random.choice(especies_flores)
            tamaño_escogido = random.choice(tamaño_flores)
            flor_definida = str(especie_escogida+tamaño_escogido)
            #print(numero, flor_definida)
            self.lista_bodega.append(flor_definida)


    def actualizar_archivo(self):#crear archivo y guardar diccionario en un archivo (pikle)
        if Path("bodega_actualizada.dat").is_file():
            #print ("File exist")
            with open("bodega_actualizada.dat", 'rb') as pf:
                pickle_abierto = pickle.load(pf)
            
            print(pickle_abierto)
            for elem in self.lista_bodega:
                if elem in pickle_abierto.keys():
                    pickle_abierto[elem] += 1
                else:
                    pickle_abierto[elem] = 1

            self.lista_bodega = []
            with(open("bodega_actualizada.dat", "wb")) as pf:
                pickle.dump(pickle_abierto, pf)
        else:
            print("Error!")

        
    def recibir_diccionario(self, diccionario):
        with(open("bodega_actualizada.dat", "wb")) as pf:
            pickle.dump(diccionario, pf)
    
    def get_diccionario(self):
        with (open("bodega_actualizada.dat", "rb")) as pf:
            pickle_abierto = pickle.load(pf)
        return pickle_abierto
   
'''
    def buscar_flor(self, codigo_flor):
        if codigo_flor in self.bodega_sistematizada.keys():
            return print(self.bodega_sistematizada.items())
        else:
            print("La flor no se encuentra en el inventario")
'''

'''
caso1 = Bodega()
while True:
    caso1.recibir_flores(5)
    caso1.actualizar_archivo()
    input("...")
    #caso1.recibir_diccionario("diccionario que retorna del proceso")
'''