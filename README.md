# EVALUACION_MODULO_3


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://storage.googleapis.com/portalfruticola/2018/08/1e6f6146-floriculturacultivorosaspf.png" alt="Logo" width="220" height="160">
  </a>

  <h1 align="center">Bootcamp Awakelab</h1>
  <h2 align="center">Full Stack Python</h2>
  <h3 align="center">Evaluación 3</h3>
  <h4 align="center">Planta productora de flores</h4>
</p>
<br/>

**Daniela Corvalan - Joao Guzmán - Pedro Cid**

## Enunciado

FlorLinda Valdivia posee una planta de producción de ramos de flores. La empresa
compra flores de diferentes especies y tamaños para completar sus pedidos.
Los ramos producidos son de diferentes diseños y tamaños, según especificaciones de
diseño que indican cantidad de flores y de qué tipo.
Las flores llegan una a una a la bodega y se almacenan hasta que hay cantidad
suficiente para producir un ramo.
Se solicita crear un programa que procese el flujo de flores de llegada y obtenga el flujo de ramos como su resultado.
Debe crear una interfaz por línea de comandos programada en Python3.

## Implementación

### Paso 1:

* Maqueta del programa:
    * Definición de clases, herencia y funciones a implementar según el enunciado del problema:

    * ` Clase Archivo `  -> Clase madre de la que heredan todas las clases que deben crear un archivo de texto donde registrar los cambios en el proceso. Esta clase contiene los siguientes atributos y métodos: 
      -  `__init__ ` con atributo nombre de archivo que llama a metodo que crea el archivo.
      - `agregar_elemento()` abre el archivo y agrega el elemento de entrada con 'a', y agregar con write.
      - `eliminar_elemento()` abre el archivo, lo carga en memoria, verifica si el elemento esta, borrarlo y sobreescribe el archivo con 'w'.


    * ` Clase Diseno `  -> Hereda de clase Archivo, su fin es crear un archivo de texto con los diseños que vaya agregando el usuario mediante input para determinar qué clases de flores se necesitan para hacer la producción de los ramos.Esta clase contiene los siguientes atributos y métodos: 
      -  `__init__ ` inicializa herencia de ClaseArchivo y define un nombre.
      - `agregar_diseno()` abre el archivo y, mediante preguntas al usuario mediante input crea los códigos correspondientes a cada diseño de ramo con el siguiente formato:
      <p align="center">
        <nombre_ramo><tamano_ramo><cantidad_flor­1><especie_flor­1> <cantidad_flor­N><especie_flor­N><cantidad_flores_ramo>
      </p> 

      -> Los códigos se van almacenando dentro del archivo .txt creado.

     * ` Clase Bodega `  -> Su rol es definir y sistematizar el stock de flores. Esta clase contiene los siguientes atributos y métodos: 
        -  `__init__ ` inicializa la clase con un argumento nombre de archivo. Se definen los siguientes argumentos: __nombre_archivo, lista_bodega (crea lista vacía), bodega_sistematizada (crea un diccionario para almacenar el stock de flores), __crear_archivo (atributo encapsulado que se usa para crear el archivo ya que esta clase no hereda de la ClaseArchivo).
        - `def __crear_archivo` comprueba si existe el archivo bodega y en el caso de que no exista, lo crea.  
        - `def recibir_diccionario` actualiza el diccionario creado inicialmente.
        - `def recibir_flores` 
        - `def sistematizacion_bodega` actualiza el diccionario.
        - `def actualizar_archivo` crea archivo y guardar diccionario en un archivo (pikle)
        - `def buscar_flor` busca flores en el inventario y verifica si están o no.

     * ` Clase Armado`  -> Su rol es ejecutar la producción de los ramos. Esta clase contiene los siguientes atributos y métodos: 
        - `__init__` define qué flores necesito para armar el diseño, retorne la lista de pedido para armar el diseño.
        - `def identificar_flores` contiene varios procesos, como por ejemplo descomponer el string y generar una lista nueva con elementos separados.
        - `def armar_ramo` proceso de armado de los ramos que descuenta del inventario de la bodega.
        - `def ver_disponibilidad_bodega` revisa el archivo con el stock de la bodega y retorna el ramo armado o avisa que aún no es posible porque falta stock.

### Paso 2:
* Creación de un script donde se ejecuta el proceso completo.

### Paso 3:
*   Repositorio Github donde se trabaja con ramas por tareas asignadas según las funciones a desarrollar. Teniendo como base una rama Desarrollo donde convergen los aportes de los colaboradores.

### Paso 4:
* Aplicar merge con las diferentes ramas y empezar a realizar pruebas de funcionamiento.

### Paso 5:
* Publicar version operativa del programa en rama principal.