¿Para qué usamos Clases en Python?
==================================

En Python una clase es una estructura de programación que sirve para definir atributos y métodos que describen a un objeto o entidad; en otras palabras, una clase es una plantilla o molde para crear objetos, donde se definen las propiedades (atributos) y comportamientos (métodos) que tendrán los objetos que se creen a partir de ella.

Declaración de una clase
------------------------

Se utiliza la palabra reservada "**class**"" seguida del nombre de la clase y dos puntos (:) y luego el cuerpo de la clase.

.. code-block:: python

    class Person:
        atributo1="valor1"
        def __init__(self, name, age):
            self.name=name
            self.age=age

        def greeting(self):
            print (f'Hi, my name is {self.name} and I’m {self.age} years old')

En este caso:

- la clase definida se llama "**Person**"

- tiene un atributo de clase "**atributo1**"

- tiene dos atributos de instancia "**name**" y "**age**"

- tiene un método “greeting” 

- y el método dunder "**__init__**""

.. admonition:: Nota

    Se podría decir que toda clase tiene un constructor, que recibe unos parámetros de entrada cuando el objeto es creado.
    Creamos por lo tanto el constructor "**__init__**" que es un método dunder que se usa para inicializar un objeto cuando se crea una instancia de una clase.

Creación de un objeto
---------------------

Siguiendo con la clase creada anteriormente, podemos crear un objeto de esta clase de la siguiente manera:

.. code-block:: python

    my_person= Person("Sonia",48)

Acceso a métodos y atributos
----------------------------

Siguiendo con la clase creada anteriormente, podemos acceder a los atributos y métodos de la clase de la siguiente manera:

.. code-block:: python

    my_person.atributo1
    my_person.name
    my_person.age
    my_person.greeting()

Atributos en las clases python
------------------------------
Un atributo es una variable que se define dentro de una clase, la cual almacena datos que pertenecen a un objeto de esa clase. Los atributos se utilizan para representar características o propiedades de un objeto, como su estado actual, su identificador, su tamaño, su color, etc.

Los atributos pueden ser de diferentes tipos de datos, como enteros, flotantes, cadenas, listas, diccionarios, entre otros. 

Además, los atributos pueden tener distintos niveles de visibilidad, que se especifican mediante los modificadores de acceso en la definición de la clase.

Los tres tipos principales de atributos son:

Atributos públicos
~~~~~~~~~~~~~~~~~~

Se puede acceder a ellos desde cualquier parte del programa, incluso desde fuera de la clase. 
En Python, los atributos se consideran públicos por defecto, lo que significa que no se requiere ningún modificador de acceso para especificar que un atributo es público. 
Para acceder a un atributo público, se utiliza la notación de punto (.) seguida del nombre del atributo.

Atributos privados 
~~~~~~~~~~~~~~~~~~

Sólo se puede acceder a ellos desde dentro de la clase en la que se definen. 

En Python, los atributos privados se definen mediante dos guiones bajos "**__**" seguido del nombre del atributo. 

.. code-block:: python
        
    class BankAccount:
        def __init__(self, saldo):
            self.__saldo=saldo

En este caso:

"**__saldo**" es un atributo privado de la clase "**BankAccount**", que solo se puede acceder a él desde dentro de la clase. 

Si intentamos acceder a este atributo desde fuera de la clase se producirá un error.

Atributos protegidos
~~~~~~~~~~~~~~~~~~~~

Sólo se puede acceder a ellos desde dentro de la clase en la que se definen y desde las clases derivadas (heredadas) de esa clase. 

En Python, los atributos protegidos se definen mediante un guión bajo "**_**" seguido del nombre del atributo. 

.. code-block:: python
        
    class BankAccount:
        def __init__(self, saldo):
            self._saldo=saldo

.. admonition:: Nota

    Sin embargo, en Python no existe un verdadero modificador de acceso protegido como en otros lenguajes de programación orientados a objetos, por lo que el uso del prefijo "**_**" es una convención para indicar que un atributo está protegido, pero aún es posible acceder a él desde fuera de la clase.

Métodos  en las clases python
------------------------------
En Python, los métodos son funciones que se definen dentro de una clase y se utilizan para realizar operaciones en los objetos creados a partir de esa clase. 

Los métodos se definen de la misma manera que las funciones, pero siempre tienen como primer parámetro el objeto al que se aplicará el método, que suele llamarse «**self**» por convención.

Ejemplo de un método, función **greeting**.

.. code-block:: python

    class Person:
        atributo1="valor1"
        def __init__(self, name, age):
            self.name=name
            self.age=age

        def greeting(self):
            print (f'Hi, my name is {self.name} and I’m {self.age} years old')

Para utilizar un método de una clase, primero debemos crear un objeto a partir de esa clase y luego llamar al método sobre ese objeto.

Ejemplo de creación del objeto y llamada al método **greeting**:

.. code-block:: python

    my_person= Person("Sonia",48)
    my_person.greeting()


.. admonition:: Nota

    En Python, "**self**" es una convención que se utiliza como nombre para el primer parámetro de un método en una clase. 
    El objetivo de «self» es hacer referencia al objeto que se está manipulando cuando se llama al método.

Métodos especiales en Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ver ¿Qué es un método dunder? de nuestra documentación.

.. toctree::

   dunder

Ventajas y desventajas del uso de las clases en Python
------------------------------------------------------

Ventajas
~~~~~~~~

Reutilización de código: las clases pueden reutilizarse en diferentes partes del programa o en distintos programas, lo que ahorra tiempo y reduce la duplicación de código.

Encapsulación: permiten ocultar la complejidad de un objeto y exponer solo una interfaz simple y fácil de usar para interactuar con él.

Modularidad: pueden descomponer un programa en componentes más pequeños y manejables, lo que facilita el mantenimiento y la solución de problemas.

Polimorfismo: ayudan a implementar el mismo conjunto de métodos con diferentes comportamientos para distintos tipos de objetos, lo que permite una mayor flexibilidad y extensibilidad en el diseño de programas.

Desventajas
~~~~~~~~~~~

Sobrecarga de complejidad: las clases pueden agregar complejidad adicional a un programa y hacer que sea más difícil de entender y depurar.

Curva de aprendizaje: el aprendizaje de las clases y la programación orientada a objetos en general pueden requerir una curva de aprendizaje más pronunciada para los programadores principiantes.

Uso innecesario: a veces, las clases se utilizan innecesariamente en situaciones en las que una función simple podría haber hecho el trabajo de manera más eficiente.

Resources
---------
* `Python´s classes <https://www.w3schools.com/python/python_classes.asp>` _
* `Python´s classes blog <https://blog.hubspot.es/website/clases-python#:~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora.>`_

