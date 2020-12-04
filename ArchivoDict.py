import json
from datetime import datetime
import random
import time
from pathlib import Path



class ArchivoDict:
    def __init__(self, nombre):
        self.__nombre_archivo = nombre+self.__repr__() +"_.json"
        self.__crear_archivo()

    #problemas !!!!!!!!!!!!!!!!!!!!!!!!!
    # reset archivo
    def __crear_archivo(self):
        if Path(self.__nombre_archivo).is_file():
            print ("File exist")
        else:
            data = {}
            with open(self.__nombre_archivo, 'w') as file:
                json.dump(data, file)
    
    
    def agregar_elemento(self, clave, valor):
        with open(self.__nombre_archivo, 'r') as archivo:
            linea = archivo.readline()

        json_data = json.loads(linea) # crea un diccionario
        print("Archivo---> ",json_data)
        if clave in json_data.keys():
            json_data[clave] += valor
        else:
            json_data[clave] = valor
        
        with open(self.__nombre_archivo, 'w') as archivo:
            string_json = json.dumps(json_data) # creo un string json desde el diccionario python
            archivo.write(string_json)
    
    def eliminar_elemento(self, clave):
        with open(self.__nombre_archivo, 'r') as archivo:
            linea = archivo.readline()

        json_data = json.loads(linea) # crea un diccionario
        json_data.pop(clave, None)
        
        with open(self.__nombre_archivo, 'w') as archivo:
            string_json = json.dumps(json_data) # creo un string json desde el diccionario python
            archivo.write(string_json)
            

    def cargar_datos(self):
        try:
            with open(self.__nombre_archivo, "r") as f:
                linea = f.readline()
                data = json.loads(linea)
                print("Archivo Cargado")
                return data
        except (OSError, IOError) as e:
            print("Error", e)
            return dict()
    
    def actualizar_datos(self, dic):
        with open(self.__nombre_archivo, 'w') as f:
            f.write(json.dumps(dic))

    def __repr__(self):
        fecha = datetime.now()
        return str(fecha.date())

'''
mi_bodega = ArchivoDict("Bodega")
mi_bodega2 = ArchivoDict("Bodega2")

stock2 = mi_bodega.cargar_datos()
    
mi_bodega.agregar_elemento("JOAO",10)

mi_bodega.eliminar_elemento("bS")

stock2 = mi_bodega.cargar_datos()

stock2["Gaga"] = 10 

mi_bodega.actualizar_datos(stock2)
'''