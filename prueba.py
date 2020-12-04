from clase_bodega import Bodega
from clase_diseno import Diseno
from class_armado import Armado
from ArchivoDict import ArchivoDict
import time


registro_ramos_terminados = ArchivoDict("Ramos_salida_test1")
mi_bodega = Bodega()
diseno1 = Diseno("Diseno_test1")
proceso1 = Armado()

diseno_listo = diseno1.agregar_diseno()
diseno1.agregar_elemento(diseno_listo)
while True:
    #diseno_listo = 'AL5a5b5c15'
    proceso1.set_diseno(diseno_listo)
    ramo_a_procesar = proceso1.identificar_flores()
    ramo_a_pedir = proceso1.armar_ramo(ramo_a_procesar)


    mi_bodega.recibir_flores(1000)
    mi_bodega.sistematizacion_bodega()
    mi_bodega.actualizar_archivo()
    stock_bodega = mi_bodega.abrir_pickle() # 

    print("Stock BODEGA\n", stock_bodega)
    print("Ramo para armar: ",ramo_a_pedir)
    stock, ramo_ok = proceso1.ver_disponibilidad_bodega(ramo_a_pedir, stock_bodega)
    if ramo_ok:
        print("Guardar ramo ok en archivo de salida")
        ramo = proceso1.ramo_string(ramo_ok)
        print(ramo)
        registro_ramos_terminados.agregar_elemento(ramo,1)



        print("Actualizar archivo de bodega")
        mi_bodega.recibir_diccionario(stock)
        time.sleep(1)

        
    else:
        print("Actualizar archivo de bodega")
        mi_bodega.recibir_diccionario(stock)
        time.sleep(1)
