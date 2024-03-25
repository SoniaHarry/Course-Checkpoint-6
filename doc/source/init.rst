¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
=================================================================================

Este método se llama constructor y en Python se corresponde con el método "**__init__**" que recibe unos parámetros de entrada cuando el objeto es creado. 
Y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

Ejemplo:

.. code-block:: python

    class MiClase:
        atributo1 = "valor1"
        atributo2 = "valor2"
        def __init__(self, name, age):
            self.name = age
            self.age=age

En este ejemplo, el método __init__ toma dos parámetros: name y age. 
Estos se utilizan para inicializar los atributos name y age de la instancia de la clase.

Al crear una instancia de la clase Persona, se debe proporcionar un valor para cada uno de los parámetros nombre y edad, como en el siguiente ejemplo:

.. code-block:: python

    person1 = MiClase ("Sonia",48)
    print (person1.name)
    print (person1.age)

Resources
---------
* `Python método __Init__ <https://www.w3schools.com/python/gloss_python_class_init.asp>`_
* `Python´s clases <https://blog.hubspot.es/website/clases-python#:~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora.>`_