import random

class Armado:

    def __init__(self, tipo_diseño):
        self.tipo_diseño = tipo_diseño
    
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
        total = 0
        for elem in range(0,len(pedido)-1): #el ultimo elemento de la lista siempre será el total de flores
            if type(pedido[elem]) == int:
                total += pedido[elem]

        cantida_faltante = pedido[-1] - total   
        print("Necesito: ",pedido[-1] - total," flores para terminar de diseñar el ramo")
        pedido.remove(pedido[-1])
        pedido.append(cantida_faltante)
        pedido.append(random.choice(abecedario))

        for flor in range(2,len(pedido)):
            if type(pedido[flor]) == str:
                flor_tamano = pedido[flor]+pedido[1]
                pedir_stock.append(flor_tamano)
            else:
                pedir_stock.append(pedido[flor]) 
        
        return pedir_stock, pedido[:2]
        
    def ver_disponibilidad_bodega(self, ramo_consulta,stock_bodega):
        stock_bodega_aux = stock_bodega 
        estado = 0
        for elem in range(0,len(ramo_consulta)-1):
            #print(ramo_consulta[elem]," - ",elem)
            if ramo_consulta[elem+1] in stock_bodega_aux.keys():
                if stock_bodega_aux[ramo_consulta[elem+1]] > ramo_consulta[elem]:
                    estado +=2
                    stock_bodega_aux[ramo_consulta[elem+1]] -= ramo_consulta[elem]
        
        if estado == len(ramo_consulta):
            print("Ramo armado")
            return stock_bodega_aux, ramo_consulta
        else:
            print("Aun no está el stock! ")
            return stock_bodega, ramo_consulta

        




stock_bodega = {'xL': 14, 'qL': 28, 'uS': 21, 'yL': 44, 'gL': 19, 'aS': 22, 
'mL': 15, 'sS': 11, 'oL': 16, 'wS': 21, 'tS': 19, 'cS': 13, 'yS': 47, 
'pL': 15, 'wL': 22, 'lL': 17, 'bS': 20, 'rL': 9, 'rS': 15, 'dL': 19, 
'uL': 10, 'pS': 20, 'lS': 26, 'vS': 20, 'zS': 24, 'fS': 18, 'zL': 18,
'xS': 22, 'bL':19, 'kS': 27, 'hL': 22, 'oS': 16, 'jL': 18, 'dS': 16,
'mS': 16, 'aL': 19, 'vL': 20, 'eS': 22, 'gS': 22, 'tL': 20, 'eL': 25,
'sL': 19, 'hS': 31, 'fL': 18, 'qS': 12, 'kL': 23, 'cL': 12, 'nS': 18,
'jS': 16, 'nL': 23}


diseno1 = Armado("AL8d8r5t30")

lista_flores = diseno1.identificar_flores()


print("Flores pedido: ",lista_flores)
ramo_a_pedir, encabezado = diseno1.armar_ramo(lista_flores)
print("Encabezado: ", encabezado)
print("Ramo para armar: ",ramo_a_pedir)
stock, ramo_ok = diseno1.ver_disponibilidad_bodega(ramo_a_pedir, stock_bodega)

print("ramo ok", encabezado + ramo_ok)


print("Stock actual")
print(type(stock))
stock_sorted = sorted(stock.items())
print(type(stock_sorted))
for elem in stock_sorted:
    print(elem)

