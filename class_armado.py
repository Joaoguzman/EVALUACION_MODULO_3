import random

class Armado:

    def __init__(self):
        self.tipo_diseño = ''

    def set_diseno(self, diseno):
        self.tipo_diseño = diseno
    
    def identificar_flores(self):

        lista_flores = []
        abecedario = 'abcdefghyjklmnopqrstuvwxyz'
        tamano = 'LS'
        lista_flores.append(self.tipo_diseño[0])
        lista_flores.append(self.tipo_diseño[1])

        # proceso para descomponer el string y generar una lista nueva con elementos separados
        
        for elem in range(0, len(self.tipo_diseño)-2):
            
            if self.tipo_diseño[elem].isdigit() and self.tipo_diseño[elem+1].isalpha():
                if int(self.tipo_diseño[elem]) !=0:   
                    lista_flores.append(int(self.tipo_diseño[elem]))
                    lista_flores.append(self.tipo_diseño[elem+1])
            elif self.tipo_diseño[elem].isdigit() and self.tipo_diseño[elem+1].isdigit() and self.tipo_diseño[elem+2].isalpha():
                lista_flores.append( int(self.tipo_diseño[elem] + self.tipo_diseño[elem+1]))
                lista_flores.append(self.tipo_diseño[elem+2])

        total = self.tipo_diseño[-2] + self.tipo_diseño[-1] 
        #print("Total: ",total)
        lista_flores.append(int(total))
        #print(lista_flores)
        return lista_flores  
             
    def armar_ramo(self, pedido):
        abecedario = 'abcdefghyjklmnopqrstuvwxyz'
        pedir_stock = []
        pedir_stock.append(pedido[0])
        pedir_stock.append(pedido[1])
        total = 0
        for elem in range(0,len(pedido)-1): #el ultimo elemento de la lista siempre será el total de flores
            if type(pedido[elem]) == int:
                total += pedido[elem]

        cantida_faltante = pedido[-1] - total 
        if cantida_faltante != 0:
            print("Necesito: ",cantida_faltante," flores para terminar de diseñar el ramo")
            pedido.remove(pedido[-1])
            pedido.append(cantida_faltante)
            pedido.append(random.choice(abecedario))
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
        for elem in range(0,len(ramo_consulta)-1):
            if ramo_consulta[elem+1] in stock_bodega_aux.keys():
                if stock_bodega_aux[ramo_consulta[elem+1]] > ramo_consulta[elem]:
                    stock_bodega_aux[ramo_consulta[elem+1]] -= ramo_consulta[elem]
                    estado +=2
        
        print("Estado: ", estado)
        if estado == len(ramo_consulta):
            print("Ramo armado")
            return stock_bodega_aux, ramo_consulta
        else:
            print("Aun no está el stock! ")
            ramo_consulta = False
            return stock_bodega, ramo_consulta

    def ramo_string(self, ramo):
        string=""
        for elem in ramo:
            string+= str(elem)
        return string

'''

stock_bodega = {'xL': 14, 'qL': 28, 'uS': 21, 'yL': 44, 'gL': 19, 'aS': 22, 
'mL': 15, 'sS': 11, 'oL': 16, 'wS': 21, 'tS': 19, 'cS': 13, 'yS': 47, 
'pL': 15, 'wL': 22, 'lL': 17, 'bS': 20, 'rL': 9, 'rS': 15,              'dL':20,       
'uL': 10, 'pS': 20, 'lS': 26, 'vS': 20, 'zS': 24, 'fS': 18, 'zL': 18,
'xS': 22, 'bL':19, 'kS': 27, 'hL': 22, 'oS': 16, 'jL': 18, 'dS': 16,
'mS': 16, 'aL': 19, 'vL': 20, 'eS': 22, 'gS': 22, 'tL': 20, 'eL': 25,
'sL': 19, 'hS': 31, 'fL': 18, 'qS': 12, 'kL': 23, 'cL': 12, 'nS': 18,
'jS': 16, 'nL': 23}


diseno1 = Armado()
diseno1.set_diseno("AL8d8r5t30")

lista_flores = diseno1.identificar_flores()

print("Flores pedido: ",lista_flores)

ramo_a_pedir = diseno1.armar_ramo(lista_flores)

print("Ramo para armar: ",ramo_a_pedir)
stock, ramo_ok = diseno1.ver_disponibilidad_bodega(ramo_a_pedir, stock_bodega)

if ramo_ok:
    print("Guardar ramo ok en archivo de salida")
    ramo = diseno1.ramo_string(ramo_ok)
    print(ramo)
    print("Actualizar archivo de bodega")
else:
    print("Actualizar archivo de bodega")

'''
