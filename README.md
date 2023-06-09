# Flight Ticket Reservation System
[Alternative](Verde Rojo Amarillo Simple y Minimalista Plan de Proyecto Presentación Empresarial.jpg)

El proyecto 'Flight Ticket Reservation System' es una aplicación de creada mediante el lenguaje de programación Python que permite a los usuarios emular la reserva de vuelos y emitir tickets de manera sencilla y eficiente. La aplicación solicita los siguientes datos del usuario:

-Nombre
-Apellido
-Número de teléfono
-Documento de Identidad
-Sitio de origen del usuario, desde donde partiría (País de salida)
-Sitio de destino del usuario, a donde arribaría (País de destino)

Una vez que el usuario ha ingresado todos los datos solicitados, la aplicacion proporcionará opciones de vuelos disponibles para que el usuario pueda elegir.  Seleccionado uno de los vuelos disponibles, la aplicación genera un ticket de reserva detallado que se puede imprimir o guardar para su uso posterior.

Este proyecto es útil para cualquier persona que necesite reservar vuelos de manera rápida y eficiente, y puede ser utilizado como base para la construcción de sistemas de reservas más complejos en el futuro.


Nuestra meta a largo plazo es seguir mejorando la aplicación, y se considera la posibilidad de añadir la solicitud de los siguientes datos en futuras actualizaciones:
- Fecha tentativa del viaje
- Número de pasajeros que abordará en el vuelo

Explayado el propósito del proyecto en forma general, es necesario explicar cómo es el funcionamiento de la aplicación:

La aplicación es presentada ante el usuario, el cual es el que usará el servicio del sistema de reserva de ticket de vuelos, y eventualmente realizar de forma satisfactoria la reserva de uno de los vuelos disponibles. Luego de una serie de solicitudes que la aplicación solicita, se le otorgará al usuario todas las  opciones de vuelo existentes que respondan a los parámetros ingresados por el mismo.
Por otro lado, el proyecto también abarca el uso de una Base de datos que contienen más de doscientos registros de vuelos que nuestra aplicación ofrece. La BBDD consta de los siguientes campos: ID del vuelo, origen, costo, asientos disponibles y fecha de salida. Resaltamos que todos los registros contienen, en el campo fecha de salida, valores que van desde el primero de abril hasta el 30 de abril (todos los vuelos ocurren en abril de 2023).
Entonces, teniendo los parámetros que el usuario expone de acuerdo a sus necesidades, éstos sirven para realizar la consulta con la BBDD que la aplicación trabaja. Los resultados se muestran en pantalla y el usuario elige el viaje deseado. Luego se resta la cantidad de asientos reservados del registro correspondiente.
Para finalizar, el programa mostrará en pantalla el resumen de la reservación del boleto de vuelo. 
