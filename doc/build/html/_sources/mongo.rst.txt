¿Es MongoDB una base de datos SQL o NoSQL?
==========================================

MongoDB es un sistema de base de datos NoSQL (Not only SQL – No sólo SQL). Es deicr, MongoDB es una base de datos NoSQL orientada a documentos. 
Se utiliza para almacenar volúmenes masivos de datos.

A diferencia de una base de datos relacional SQL tradicional, MongoDB no se basa en tablas y columnas. 

Los datos se almacenan como colecciones y documentos. Los documentos son pares value/key que sirven como unidad básica de datos. 

Las colecciones contienen conjuntos de documentos y funciones. Son el equivalente a las tablas en las bases de datos relacionales clásicas.

¿Qué son las bases de datos NoSQL?
----------------------------------

Son estructuras que nos permiten almacenar información en aquellas situaciones en las que las bases de datos relacionales generan ciertos problemas debido principalmente a problemas de escalabilidad y rendimiento de las bases de datos relacionales donde se dan cita miles de usuarios concurrentes y con millones de consultas diarias.

Además, las bases de datos NoSQL son sistemas de almacenamiento de información que no cumplen con el esquema entidad–relación. 
Tampoco utilizan una estructura de datos en forma de tabla donde se van almacenando los datos sino que para el almacenamiento hacen uso de otros formatos como clave–valor, mapeo de columnas o grafos.

Arquitectura de MongoDB y sus componentes
-----------------------------------------

La arquitectura de MongoDB se basa en varios componentes principales:

- En primer lugar, "**_id**" es un campo obligatorio para cada documento. Representa un valor único y puede considerarse como la clave principal del documento para identificarlo dentro de la colección. 

- Un documento es el equivalente a un registro en una base de datos tradicional. Se compone de campos de nombre y valor. Cada campo es una asociación entre un nombre y un valor y es similar a una columna en una base de datos relacional.

- Una colección es un grupo de documentos de MongoDB, y se corresponde con una tabla creada con cualquier otro RDMS como Oracle o MS SQL en una base de datos relacional. No tiene una estructura predefinida.

Una base de datos es un contenedor de colecciones, al igual que un RDMS es un contenedor de tablas para las bases de datos relacionales. Cada uno tiene su propio conjunto de archivos en el sistema de archivos. Un servidor MongoDB puede almacenar múltiples bases de datos.

Resources
---------

* `Todo sobre MongoDB <https://datascientest.com/es/mongodb-todo-sobre-la-base-de-datos-nosql-orientada-a-documentos>`_
* `MongoDB vs MySQL <https://oxygenacademy.es/mongo-db-vs-mysql-diferencias-ventajas-y-desventajas/>`_
