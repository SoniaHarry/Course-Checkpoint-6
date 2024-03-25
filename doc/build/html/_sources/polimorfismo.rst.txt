¿Qué es el polimorfismo?
========================

El término polimorfismo tiene origen en las palabras poly (muchos) y morfo (formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas. 

¿Pero qué significa esto?

Pues bien, significa que objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

En pocas palabras, a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos.

¿Cómo se implementa el polimorfismo?

Python permite la implementación de polimorfismo a través del uso de herencia y sobreescritura de métodos. 
El polimorfismo permite que un objeto se comporte de manera diferente en distintos contextos.

En Python, el polimorfismo se implementa de manera natural gracias a la capacidad de las funciones y métodos para aceptar argumentos de diferentes tipos. 

¿Que es la herencia de clases?
------------------------------

Es un concepto importante en la programación orientada a objetos, el cual, permite crear una clase nueva basada en una clase ya existente, heredando sus atributos y métodos. 
A esta nueva clase la llamamos clase derivada o subclase, mientras que la clase existente recibirá el nombre de clase base o superclase.

.. admonition:: Nota

    Para heredar una clase, simplemente se especifica el nombre de la clase padre dentro de los paréntesis después del nombre de la clase hija.

Ejemplo de Herencia:

.. code-block:: python

    #Clase Automóvil
    class Automovil:

        def __init__(self, marca, modelo, color, velocidad_maxima):
            self.__marca = marca
            self.__modelo = modelo
            self.__color = color
            self.__velocidad_maxima = velocidad_maxima

        def acelerar(self, gas):
            print("Suministrando gas al motor:", gas)

    #Declaramos clase
    class AutomovilElectrico(Automovil):
        def __init__(self, marca, modelo, color, velocidad_maxima, capacidad_bateria):
            super().__init__(marca, modelo, color, velocidad_maxima)
            self.__capacidad_bateria = capacidad_bateria

        def bateria(self):
            print("El automóvil eléctrico tiene una capacidad de bateria del ", self.__capacidad_bateria)

    #Creamos el objeto de la clase
    MicocheElectrico= AutomovilElectrico("Peugeot","3007","Rojo", 260, 75)
    #Llamamos al método heredado de la clase Automovil
    MicocheElectrico.acelerar(150) #Suministrando gas al motor: 150
    #Llamamos al método de la clase AutomovilElectrino
    MicocheElectrico.bateria() #El automóvil eléctrico tiene una capacidad de bateria del  75


Ejemplo Polimorfismo
--------------------

Siguiendo con el polimorfismo vamos a poner un ejemplo:

Para implementar el polimorfismo en la clase Automóvil, simplemente se deben definir diferentes métodos que compartan el mismo nombre pero que acepten distintos tipos de argumentos.
Se podría definir un método llamado "**acelerar**" en la clase Automóvil, el cual acepte un argumento que represente la cantidad de gas que se quiere suministrar al motor. 
Luego, se podrían definir diferentes versiones de este método que acepten distintos tipos de argumentos.

.. code-block:: python

    class Automovil:

        def __init__(self, marca, modelo, color, velocidad_maxima):
            self.__marca = marca
            self.__modelo = modelo
            self.__color = color
            self.__velocidad_maxima = velocidad_maxima

        def acelerar(self, gas):
            print("Suministrando gas al motor:", gas)

        def frenar(self):
            print("Frenando el automóvil")

    class AutomovilElectrico(Automovil):
        def __init__(self, marca, modelo, color, velocidad_maxima, capacidad_bateria):
            super().__init__(marca, modelo, color, velocidad_maxima)
            self.__capacidad_bateria = capacidad_bateria

        def acelerar(self, nivel_carga):
            if nivel_carga >= 50:
                print("El automóvil eléctrico acelera rápidamente")
            else:
                print("El automóvil eléctrico acelera lentamente")

    class AutomovilDeportivo(Automovil):
        def __init__(self, marca, modelo, color, velocidad_maxima, aleron):
            super().__init__(marca, modelo, color, velocidad_maxima)
            self.__aleron = aleron

        def acelerar(self, pedal_a_fondo=True):
            if pedal_a_fondo:
                print("El automóvil deportivo acelera rápidamente")
            else:
                print("El automóvil deportivo acelera lentamente")  

    Micoche= Automovil("Peugeot","307","Azul",210)
    Micoche.acelerar(100) #Suministrando gas al motor: 100

    MicocheElectrico= AutomovilElectrico("Peugeot","3007","Rojo", 260, 75)
    MicocheElectrico.acelerar(75) #El automóvil eléctrico acelera rápidamente

    MicocheDeportivo= AutomovilDeportivo("Peugeot","3007","Rojo", 260,1)
    MicocheDeportivo.acelerar(True) #El automóvil deportivo acelera rápidamente

En este ejemplo, la clase Automóvil tiene un método llamado acelerar que acepta un argumento gas, que representa la cantidad de gas que se suministra al motor. 
La subclase AutomovilElectrico redefine el método acelerar para aceptar un argumento nivel_carga, que representa el nivel de carga de la batería del automóvil eléctrico. 
Si el nivel de carga es mayor o igual a 50, el automóvil acelera rápidamente; de lo contrario, acelera lentamente.
La subclase AutomovilDeportivo también redefine el método acelerar, esta vez para aceptar un argumento opcional pedal_a_fondo. 
Si este argumento es True, el automóvil deportivo acelera rápidamente; de lo contrario, lo hace lentamente.


Resources
---------
* `Python Polimorfismo <https://blog.hubspot.es/website/clases-python#:~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora.>`_
* `Python Polimorfismo El Libro <https://ellibrodepython.com/polimorfismo-en-programacion#polimorfismo-en-python>`_