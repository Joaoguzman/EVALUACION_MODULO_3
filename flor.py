import random
import pickle

class Inventario:
    def __init__(self,nombre):
        self.__nombre_archivo = nombre +".txt"
        self.__crear_archivo()
    
    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Inventario Iniciado")
    
    def agregar_elemento(self, dic):
        with open("flores.dat", "ab") as f:
            pickle.dump(dic, f)

    def cargar_datos(self, nombre):
        try:
            with open(nombre, "wb") as f:
                return pickle.load(f)
        except (OSError, IOError) as e:
            return dict()
    
    def guardar_datos(self, dic, nombre):
        with open(nombre, "wb") as f:
            pickle.dump(dic, f)


def generador_flor(num, diccionario):
    abecedario = 'abcd'
    tamano = 'LS'
    for flor in range(num):
        tipo = random.choice(abecedario)
        size = random.choice(tamano)
        #lista.append(tipo+size)
        if (tipo+size) in diccionario.keys():
            diccionario[tipo+size] +=1
        else:
            diccionario[tipo+size] = 1
    return diccionario

stock_bodega = {}

bodega_flor = Inventario("flores")

mis_flores = generador_flor(1000, stock_bodega)
print(type(mis_flores))
x = list(mis_flores.values())
print(sum(x))
print("\nDatos Generados: \n")
print(mis_flores)
bodega_flor.agregar_elemento(mis_flores)

##########################################################

archivo = bodega_flor.cargar_datos("flores.dat")
print("\nDatos cargados para modificar --->   1: \n")
print("Datos de entrada")
print(archivo)

for key, value in archivo.items():
    print(key," - ",value)
    if key == 'cS':
        print(key," -> ",value)
        archivo[key] = value -1 # modificando cantidad flor

bodega_flor.guardar_datos(archivo, "flores.dat")

###########################################

archivo2 = bodega_flor.cargar_datos("flores.dat")
print("\nDatos cargados despues de modificar: \n")
print("Archivo cargado: ",archivo2)

mis_flores = generador_flor(1000, stock_bodega)

x = list(mis_flores.values())
print(sum(x))
print("\nDatos Generados: \n")
print(mis_flores)
bodega_flor.agregar_elemento(mis_flores)

##########################################################

archivo = bodega_flor.cargar_datos("flores.dat")
print("\nDatos cargados para modificar   -----> 1 + 2: \n")
print("Datos de entrada")
print("Archivo cargado: ",archivo)

for key, value in archivo.items():
    print(key," - ",value)
    if key == 'cS':
        print(key," -> ",value)
        archivo[key] = value -1 # modificando cantidad flor

bodega_flor.guardar_datos(archivo, "flores.dat")

###########################################

archivo2 = bodega_flor.cargar_datos("flores.dat")
print("\nDatos cargados despues de modificar: \n")
print(archivo2)