from clase_bodega import Bodega
from clase_diseno import Diseno
from class_armado import Armado
from ArchivoDict import ArchivoDict
import time
import os


registro_ramos_terminados = ArchivoDict("Ramos_salida_test1")
mi_bodega = Bodega()
diseno1 = Diseno("Diseno_test1")
proceso1 = Armado()

diseno_listo = diseno1.agregar_diseno()
diseno1.agregar_elemento(diseno_listo)

proceso_now = []
mi_bodega.recibir_flores(100)
for elem in diseno_listo:
    proceso1.set_diseno(elem)
    mi_bodega.actualizar_archivo()
    ramo_a_procesar = proceso1.procesar_string()
    stock_bodega = mi_bodega.get_diccionario()
    ramo_a_pedir = proceso1.armar_ramo(ramo_a_procesar, stock_bodega)
    proceso_now.append(ramo_a_pedir)

while True:
    for elem in proceso_now:
        mi_bodega.recibir_flores(10) # Se define las flores que llegaran a bodega
        print("Procesando diseño: ", elem)
        mi_bodega.actualizar_archivo()
        stock_bodega = mi_bodega.get_diccionario()
        stock, ramo_ok = proceso1.ver_disponibilidad_bodega(elem, stock_bodega)
        if ramo_ok:
            print("Ramo Guardado")
            ramo = proceso1.ramo_string(ramo_ok)
            print("ramo a guardar: ", ramo)
            registro_ramos_terminados.agregar_elemento(ramo,1)
            mi_bodega.recibir_diccionario(stock)
            time.sleep(1)
            os.system('cls')
        else:
            print("No hay flores para el armar el Ramo")
            mi_bodega.recibir_diccionario(stock)
            time.sleep(1)
            os.system('cls')