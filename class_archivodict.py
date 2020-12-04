import json
from datetime import datetime
import random
import time

class ArchivoDict:
    def __init__(self):
        self.__nombre_archivo = "Bodega_"+self.__repr__() +"_.json"
        self.__crear_archivo()

    #problemas !!!!!!!!!!!!!!!!!!!!!!!!!
    # reset archivo
    def __crear_archivo(self):
        data = {}
        with open(self.__nombre_archivo, 'w') as file:
            json.dump(data, file)
    
    
    def agregar_elemento(self, clave, valor):
        with open(self.__nombre_archivo, 'r') as archivo:
            linea = archivo.readline()

        json_data = json.loads(linea) # crea un diccionario
        if clave in json_data.keys():
            json_data[clave] += valor
        else:
            json_data[clave] = valor
        
        with open(self.__nombre_archivo, 'w') as archivo:
            string_json = json.dumps(json_data) # creo un string json desde el diccionario python
            archivo.write(string_json)
    
    def eliminar_elemento(self, clave):
        with open(self.__nombre_archivo, 'r+') as f:
            json_data = json.load(f)
            json_data.pop(clave, None)
            f.write(json.dumps(json_data))
            

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

class Bodega(ArchivoDict):

    def __init__(self):
        super().__init__()
    
    '''
    def agregar_set_flores(self, diccionario):
        with open("Bodega.json", 'r+') as f:
            json_data = json.load(f)
            print(json_data)
            for clave, valor in diccionario.items():
                if clave in json_data.keys():
                    json_data[clave] += valor
                else:
                    json_data[clave] = valor
            f.seek(0)
            f.write(json.dumps(json_data))
            f.truncate()

        print("Actualizado con exito")
    '''

class Proveedor:

    def __init__(self, nombre):
        self.nombre = nombre

    def gen_flor(self, tipo):
        tamano = 'LS'
        size = random.choice(tamano)
        return tipo + size

    def gen_set_flor(self, cantidad, tipos):
        diccionario = {}
        tamano = 'LS'
        for flor in range(cantidad):
            tipo = random.choice(tipos)
            size = random.choice(tamano)
            #lista.append(tipo+size)
            if (tipo+size) in diccionario.keys():
                diccionario[tipo+size] +=1
            else:
                diccionario[tipo+size] = 1
        return diccionario

mi_proveedor = Proveedor("Doña Flora")

print(mi_proveedor.gen_flor("t"))




#Instancia del objeto
mi_bodega = Bodega()

while True:
    stock_1 = mi_proveedor.gen_set_flor(100,'abcd')
    stock2 = mi_bodega.cargar_datos()
    
    for clave, valor in stock_1.items():
        mi_bodega.agregar_elemento(clave,valor)

    time.sleep(5)
'''
#Agregar 1 elemento al objeto
mi_bodega.agregar_elemento("xx",0)
mi_bodega.agregar_elemento("yy",10)

#carga el archivo en memoria
stock = mi_bodega.cargar_datos()

#Agregando elementos al diccionario
stock["elem1"] = 0
stock["elem3"] = 0
stock["elem2"] = 0

# eliminar un elemento del diccionario cargado
del stock["xx"]

#actualizar el archivo, sobreescribe
mi_bodega.actualizar_datos(stock)

# eliminar un elemento del archivo
mi_bodega.eliminar_elemento("elem3")
mi_bodega.agregar_elemento("nn",10)
'''