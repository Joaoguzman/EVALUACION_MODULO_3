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
        print("Total: ",total)
        lista_flores.append(int(total))
        print(lista_flores)
        return lista_flores  
             
    def armar_ramo(self, pedido):
        abecedario = 'abcdefghyjklmnopqrstuvwxyz'
        pedir_stock = []
        total = 0
        for elem in range(0,len(pedido)-1): #el ultimo elemento de la lista siempre será el total de flores
            if type(pedido[elem]) == int:
                total += pedido[elem]

        cantida_faltante = pedido[-1] - total   
        print("Necesito: ",pedido[-1] - total," flores para terminar el ramo")
        pedido.remove(pedido[-1])
        pedido.append(cantida_faltante)
        pedido.append(random.choice(abecedario))

        for flor in range(2,len(pedido)):
            if type(pedido[flor]) == str:
                flor_tamano = pedido[flor]+pedido[1]
                pedir_stock.append(flor_tamano)
            else:
                pedir_stock.append(pedido[flor]) 
        
        print(pedir_stock)



diseno1 = Armado("AL8d8r5t30")
diseno2 = Armado("AS3a4b6k20")


lista_flores = diseno1.identificar_flores()
lista_flores2 = diseno2.identificar_flores()

#print(lista_flores)
diseno1.armar_ramo(lista_flores)
print()
diseno1.armar_ramo(lista_flores2)