import random

def generador_flor(num):
    lista = []
    abecedario = 'abcdefghyjklmnopqrstuvwxyz'
    tamano = 'LS'
    for flor in range(num):
        tipo = random.choice(abecedario)
        size = random.choice(tamano)
        lista.append(tipo+size)
    return lista



class Inventario:
    def __init__(self,nombre):
        self.__nombre_archivo = nombre +".txt"
        self.__crear_archivo()
    
    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Inventario Iniciado")
    
    def agregar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("\n"+elemento)

bodega_flor = Inventario("flores")

mis_flores = generador_flor(100)
print(mis_flores)
for i in mis_flores:
    bodega_flor.agregar_elemento(i)


diccionario = {}

for i in mis_flores:
    if i in diccionario.keys():
        diccionario[i] +=1
    else:
        diccionario[i] = 1


for key, value in diccionario.items():
    print(key," - ",value)