¿Qué es un método dunder?
=========================

En Python, los métodos dunder (abreviatura de «double underscore methods», también conocidos como «métodos mágicos» o «métodos especiales») son métodos especiales que tienen un doble guion bajo (__) al principio y al final de su nombre. 
Se emplean para definir el comportamiento especial de las clases y sus instancias, y son llamados automáticamente por el intérprete de Python en respuesta a ciertas operaciones.

Los métodos dunder pueden utilizarse para implementar características como la inicialización de objetos, la representación en forma de cadena, la sobrecarga de operadores, la comparación, entre otras.

Ejemplo de algunos métodos dunder
---------------------------------

__init__
~~~~~~~~

El método __init__() se llama automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.
Utilice el método __init__() para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto.

Por ejemplo, supongamos que queremos crear una clase llamada Persona con dos atributos: nombre y edad. 
Podríamos definir la clase de la siguiente manera:

.. code-block:: python

    class Persona:
        def __init__(self, nombre, edad): 
            self.nombre = nombre 
            self.edad = edad 

En este ejemplo, el método __init__ toma dos parámetros: nombre y edad. Estos se utilizan para inicializar los atributos nombre y edad de la instancia de la clase.

Al crear una instancia de la clase Persona, se debe proporcionar un valor para cada uno de los parámetros nombre y edad, como en el siguiente ejemplo:

.. code-block:: python

    persona1 = Persona("Sonia", 48)


__str__
~~~~~~~

El método __str__() controla lo que se debe devolver cuando el objeto de clase se representa como una cadena.
Este método se define dentro de una clase y se llama cuando se usa la función str() en un objeto de esa clase.

Si el método __str__() no está configurado, se devuelve la representación de cadena del objeto como se muestra a continuación:

.. code-block:: console

    <__main__.Person object at 0x1509bb384100>


Por ejemplo, supongamos que tenemos una clase Persona con los atributos nombre y edad. 
Podemos definir el método __str__ de la siguiente manera:

.. code-block:: python

    class Persona:
        def __init__(self, nombre, edad): 
            self.nombre = nombre 
            self.edad = edad 
        def __str__(self):
            return f"{self.nombre} ({self.edad} años)"

En este ejemplo, el método __str__ devuelve una cadena de caracteres que representa la instancia de la clase Persona. 
La cadena contiene el nombre y la edad de la persona, separados por un espacio.

Al utilizar la función str() con una instancia de la clase Persona, se llamará automáticamente al método __str__, como en el siguiente ejemplo:

.. code-block:: python

    persona1 = Persona("Sonia", 48)
    print(str(persona1)) # salida: Sonia (48 AÑOS)


__repr__  
~~~~~~~~~

El método __repr__() al igual que la anterior __str__() controla lo que se debe devolver pero a diferencia del otro se suele utilizar más para debugear.

Y se utiliza para devolver una representación de cadena legible de un objeto. 
Este método se define dentro de una clase y se llama cuando se usa la función repr() en un objeto de esa clase.

Ejemplo:

.. code-block:: python

    class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f"Invoice from {self.client} for {self.total}"

    def __repr__(self):
        return f"Invoice({self.client}, {self.total})"


    inv = Invoice('Google', 500)
    print(str(inv))
    print(repr(inv))

.. admonition:: Nota

    La implementación de __str__() en el ejemplo anterior devuelve una cadena fácil de leer que proporciona los detalles relevantes del objeto para un usuario. 

    La implementación de __repr__() devuelve una cadena que es una expresión válida de Python que podría usarse para recrear el objeto


Resources
---------

* `Métodos dunder <https://blog.hubspot.es/website/clases-python#:~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora>`_
