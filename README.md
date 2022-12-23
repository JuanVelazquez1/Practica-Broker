# Practica-Broker
Práctica 3 Arquitecturas Avanzadas

El objetivo de esta práctica es, a partir del código dado, habilitar la conexión de múltiples clientes. 
Ya que, en un principio, no puede conectarse más que uno.
El problema es que todos los clientes intentan conectarse al mismo puerto. 

La solución implementada hace que el nuevo cliente intente conectarse al puerto siguiente al ocupado.
De forma que incrementa el puerto hasta que encuentre uno que esté libre.

Una posible mejora sería que en lugar de que el cliente fuese probando uno por uno el siguiente puerto hasta encontrar uno libre,
el propio bróker guardase un array con los puertos ocupados y, al iniciar la comunicación, le indicase a qué puerto libre podría conectarse.
