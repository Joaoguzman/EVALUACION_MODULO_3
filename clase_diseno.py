import time

class Archivo:
    def __init__(self,nombre):
        self.__nombre_archivo = nombre +".txt"
        self.__crear_archivo()
    
    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Archivo Principal: ")
    
    def agregar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("\n"+elemento)

class Diseno(Archivo):

    lista_diseno = []

    def __init__(self, nombre):
        #self.__nombre_archivo = "data/diseno"+self.__repr__()+".txt"
        #self.__crear_archivo()
        Archivo.__init__(self, nombre)

    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Archivo Diseño: ")        

    def agregar_elemento(self,input_usuario, contenidos):
        input("Ingrese código de producto: ")
        '''
        with open('data/archivo_diseno.txt', 'a') as file:
            file.read()    
            file.seek(0)
            archivo_diseno == file.read
        print(archivo_diseno)

        for indice in range(len(archivo_diseno)):
            print(archivo_diseno[indice])
            if archivo_diseno[indice] != " " and archivo_diseno[indice] != ",":
                lista_diseno.append(archivo_diseno[indice])
        print(lista_diseno)
'''

            
#        while True:
 #           for contenido in contenidos:
  #              if  input_usuario != contenidos: 
   #                 print("Código Inválido! Intente nuevamente: ")   
    #            else:
     #               input_usuario == contenidos
      #              archivo_salida.append(contenidos)
       #             archivo_salida.close()
        #            print("Código ingresado con éxito.")
         #       time.sleep(0,1)
          #      print("¿Desea ingresar otro código?: ")
           #     else:
            #        pass input_usuario == ("Si"):


            #    elif input_usuario == ("No")
           # break()    
'''
    def eliminar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'w') as file:
            file.write("\n"+elemento)
            if codigo in datos:
                archivo_salida.write(contenidos)
                archivo_salida.close()
            else:

'''
diseno1 = Diseno("diseno")
diseno1.agregar_elemento

