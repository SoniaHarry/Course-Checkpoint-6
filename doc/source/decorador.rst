¿Qué es un decorador de python?
===============================

Los decoradores son funciones que modifican el comportamiento de otras funciones, ayudan a acortar nuestro código.
Se usará un símbolo **@** seguido de la propiedad de nombre **property**. 
Y esto se llama decorador y lo que esencialmente hace es decorar y envolver la propiedad con la que queremos trabajar. 
Además, nos informa de que tenemos acceso para llamar directamente a esa función donde este el decorador y luego recuperar esos datos. 
Si llego a una clase, y no veo ningún decorador de propiedades es que todos esos datos son simplemente para el uso interno de la clase y que no debo recurrir a ellos directamente. 
Por eso, cada vez que escribimos código, no solo escribimos código que funciona, sino que también escribimos código que comunica la historia de cómo deben ejecutarse nuestros programas y cómo otros deben usar nuestro código. 
Eso es tan importante como asegurarnos de que nuestro Los programas funcionan correctamente.

Ejemplo Decorador property
---------------------------

El decorador puede ser usado sobre un método, que hará que actúe como si fuera un atributo.

.. code-block:: python

    class Clase:
        def __init__(self, mi_atributo):
            self.__mi_atributo = mi_atributo

        @property
        def mi_atributo(self):
            return self.__mi_atributo

Como si de un atributo normal se tratase, podemos acceder a el con el objeto . y nombre.

.. code-block:: python

    mi_clase = Clase("valor_atributo")
    mi_clase.mi_atributo # 'valor_atributo'

.. admonition:: Nota

    Muy importante notar que aunque mi_atributo pueda parecer un método, en realidad no lo es, por lo que no puede ser llamado con ().

Ejemplo Decorador setter
------------------------

Por último, existen varios añadidos al decorador @property como pueden ser el setter. 
Se trata de otro decorador que permite definir un “método” que modifica el contenido del atributo que se esté usando.

.. code-block:: python

    class Clase:
        def __init__(self, mi_atributo):
            self.__mi_atributo = mi_atributo

        @property
        def mi_atributo(self):
            return self.__mi_atributo

        @mi_atributo.setter
        def mi_atributo(self, valor):
            if valor != "":
                print("Modificando el valor")
                self.__mi_atributo = valor
            else:
                print("Error está vacío")

De esta forma podemos añadir código al setter, haciendo que por ejemplo realice comprobaciones antes de modificar el valor. 
Esto es una cosa que de usar un atributo normal no podríamos hacer, y es muy útil de cara a la encapsulación.

.. code-block:: python

    mi_clase = Clase("valor_atributo")
    mi_clase.mi_atributo # 'valor_atributo'

    mi_clase.mi_atributo = "nuevo_valor"
    mi_clase.mi_atributo # 'nuevo_valor'

    mi_clase.mi_atributo = "" # Error está vacío

Resources
---------

* `Python Decoradores <https://ellibrodepython.com/decoradores-python>`_
* `Decorador Property <https://ellibrodepython.com/decorador-property-python>`_
