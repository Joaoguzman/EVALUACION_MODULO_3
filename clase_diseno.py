from pathlib import Path




class Archivo:
    def __init__(self,nombre):
        self.__nombre_archivo = nombre +".txt"
        self.__crear_archivo()
        
    
    def __crear_archivo(self):
        if Path(self.__nombre_archivo).is_file():
            print ("File exist")
        else:
            with open(self.__nombre_archivo, 'a') as file:
                file.write("Archivo Principal: ")
        
    def agregar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'a') as file:
            for elem in elemento:
                file.write("\n"+elem)
            

class Diseno(Archivo):

    def __init__(self, nombre):
        Archivo.__init__(self, nombre) 
            

    def agregar_diseno(self):
        while True:
            try:
                n_veces = int(input("Diseños a procesar hoy: "))
                if n_veces > 0 and n_veces < 5:
                    break
                else:
                    continue
            except ValueError:
                print("Error")
        
        lista_disenos = []

        print("*******DISEÑO DE RAMOS*******")
        contador = 1
        while n_veces >= contador:
            print(n_veces)
            print(contador)
            mayus= (input("Indique tipo de ramo (A, B o C): "))
            if mayus in ["A", "B", "C"]:
                while True:
                    tamano= (input("Indique tamaño ramo: "))
                    if tamano in ["S", "L"]:
                        tipo_de_flores=""
                        suma=0
                        variedad=3
                        while variedad != 0:

                            while True:
                                num_flor1= input("Indique cantidad de flor : ")
                            
                                if num_flor1.isdigit() and int(num_flor1) > 0 and int(num_flor1) < 100:
                                
                                    while True:
                                        variedad1= (input("Indique variedad flor: "))
                                        if variedad1.islower() == True:
                                            tipo_de_flores = tipo_de_flores + str(num_flor1) + variedad1[0]
                                            variedad = variedad -1
                                            suma= suma + int(num_flor1)
                                            break
                                        else: print("Error debe elegir una variedad existente!")
                                    break
                                                
                                        
                                else: print("Error, debe elegir un número entre 1 y 100")
                        print(tipo_de_flores)
                        diseno_listo = mayus+tamano+tipo_de_flores
                        print(diseno_listo)
                        #print(suma)
                        pregunta = input("Quiere agregar follaje?(s/n):  ")
                        if pregunta == "s":
                            cantidad = int(input("Cuánto quiere agregar?: "))
                            suma_final = cantidad + suma
                            suma_str = str(suma_final)
                            diseno_listo = diseno_listo + suma_str
                            print(diseno_listo)
                            lista_disenos.append(diseno_listo)
                            contador +=1
                        elif pregunta == "n":
                            diseno_listo= diseno_listo + str(suma)
                            print(diseno_listo)
                            lista_disenos.append(diseno_listo)
                            contador += 1 
                        elif pregunta != ("n", "s"):
                            print("Error, digite s o n:")
                        break       
                    else: print("Error, debe elegir entre tamaño S o L!") 
            else: print("Error, debe elegir entre tipo A, B o C!")

        return lista_disenos
'''
diseno1 = Diseno("diseno")   
diseno_listo = diseno1.agregar_diseno()     
print("Diseño Generado: ", diseno_listo)
diseno1.agregar_elemento(diseno_listo)
'''
                