import random
import time
import os
import re
import unittest

class Armado:

    def __init__(self):
        self.tipo_diseño = ''

    def set_diseno(self, diseno):
        self.tipo_diseño = diseno

    def __separar_palabras(self, string):
        patron = r'(\w)([a-zA-Z]){1}'
        return re.sub(patron, r'\1 \2 ', string)


    def procesar_string(self):
        string2 = self.__separar_palabras(self.tipo_diseño)
        lista = string2.split(" ")
        cuerpo = []
        cola = int(lista[-1])
        for elem in range(0,len(lista)-1):
            if lista[elem].isupper():
                cuerpo.append(lista[elem])
            elif lista[elem].isdigit() and lista[elem+1].islower():
                cuerpo.append(int(lista[elem]))
                cuerpo.append(lista[elem+1])

        cuerpo.append(cola)
        return cuerpo
             
    def armar_ramo(self, pedido , diccionario):
        
        maximo = max(diccionario.keys(), key=lambda k: diccionario[k])
        
            
        pedir_stock = []
        pedir_stock.append(pedido[0])
        pedir_stock.append(pedido[1])
        total = 0
        for elem in range(0,len(pedido)-1):
            if type(pedido[elem]) == int:
                total += pedido[elem]

        cantida_faltante = pedido[-1] - total 
        if cantida_faltante != 0:
            pedido.remove(pedido[-1])
            pedido.append(cantida_faltante)
            pedido.append(maximo[0])
        else:
            pedido.remove(pedido[-1])

        for flor in range(2,len(pedido)):
            if type(pedido[flor]) == str:
                flor_tamano = pedido[flor]+pedido[1]
                pedir_stock.append(flor_tamano)
            else:
                pedir_stock.append(pedido[flor]) 
        
        return pedir_stock
        
    def ver_disponibilidad_bodega(self, ramo_consulta,stock_bodega):
        stock_bodega_aux = stock_bodega 
        estado = 2
        estado_aux=False
        for elem in range(0,len(ramo_consulta)-1):
            if ramo_consulta[elem+1] in stock_bodega_aux.keys():
                if stock_bodega_aux[ramo_consulta[elem+1]] >= ramo_consulta[elem]:
                    estado +=2
                    if estado == 8:
                        estado_aux = True
        
        print("Estado: ", estado)
        if estado_aux:
            for elem in range(0,len(ramo_consulta)-1):
                if ramo_consulta[elem+1] in stock_bodega_aux.keys():
                    if stock_bodega_aux[ramo_consulta[elem+1]] >= ramo_consulta[elem]:
                        stock_bodega_aux[ramo_consulta[elem+1]] -= ramo_consulta[elem]

            return stock_bodega_aux, ramo_consulta
        else:
            ramo_consulta = False
            return stock_bodega, ramo_consulta

    def ramo_string(self, ramo):
        string=""
        for elem in ramo:
            string+= str(elem)
        return string




class TestArmadoRamo(unittest.TestCase):

    def setUp(self):
        self.ramo1 = Armado()
        self.ramo2 = Armado()
        self.ramo3 = Armado()
        self.ramo1.set_diseno('BL33a33b33d99')
        self.ramo2.set_diseno('CL1d4a10c15')
        self.ramo3.set_diseno('AL3a3b3c19')

    def test_identificar_flores(self):
        lista1 = self.ramo1.procesar_string()
        self.assertEqual(['B','L',33 ,'a',33 ,'b',33 ,'d',99],lista1)

    def test_identificar_flores_2(self):
        lista1 = self.ramo2.procesar_string()
        self.assertEqual(['C','L',1 ,'d',4 ,'a',10 ,'c',15 ],lista1)

    def test_identificar_flores_3(self):
        lista1 = self.ramo3.procesar_string()
        self.assertEqual(['A','L',3 ,'a',3 ,'b',3,'c',19],lista1)
    
    def test_armar_ramo_1(self):
        stock_bodega = {'aL':12, 'bL':120, 'cL':1200}
        lista1 = self.ramo1.procesar_string()
        ramo_armado = self.ramo1.armar_ramo(lista1, stock_bodega)
        self.assertEqual(['B','L',33 ,'aL',33 ,'bL',33 ,'dL'], ramo_armado)
    
    def test_armar_ramo_2(self):
        stock_bodega = {'aL':12, 'bL':120, 'cL':1200}
        lista1 = self.ramo2.procesar_string()
        ramo_armado = self.ramo2.armar_ramo(lista1, stock_bodega)
        self.assertEqual(['C','L',1 ,'dL',4 ,'aL',10 ,'cL'], ramo_armado)
    
    def test_armar_ramo_3(self):
        stock_bodega = {'aL':12, 'bL':120, 'cL':1200}
        lista1 = self.ramo3.procesar_string()
        ramo_armado = self.ramo3.armar_ramo(lista1, stock_bodega)
        self.assertEqual(['A','L',3 ,'aL',3 ,'bL',3,'cL',10,'cL'], ramo_armado)



if __name__ == '__main__':
    
    unittest.main()
    '''
    ramo1 = Armado()
    ramo1.set_diseno('BL90a90b9d270')
    lista_ramo = ramo1.identificar_flores()
    print(lista_ramo)
    '''






'''
stock_bodega = {'aL':1200, 'bL':1200, 'cL':1200}


diseno1 = Armado()

while True:
    diseno1.set_diseno("AL10a10b30c50")

    lista_flores = diseno1.identificar_flores()
    
    print("Flores pedido: ",lista_flores)

    ramo_a_pedir = diseno1.armar_ramo(lista_flores)
    print(stock_bodega)
    print("Ramo para armar: ",ramo_a_pedir)
    stock, ramo_ok = diseno1.ver_disponibilidad_bodega(ramo_a_pedir, stock_bodega)
    
    if ramo_ok:
        print("Guardar ramo ok en archivo de salida")
        ramo = diseno1.ramo_string(ramo_ok)
        print(ramo)
        print("Actualizar archivo de bodega")
        print(stock)
        time.sleep(1)
        os.system('cls')
    else:
        print("Actualizar archivo de bodega")
        time.sleep(1)
        os.system('cls')

    '''
