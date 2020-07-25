# Tarea hadoop MapReduce
## Autor
Ignacio Fuenzalida Veas

---

### Item 1

**Desarrolle mappers y reducers en Python que den solución a las siguientes preguntas, las cuales están enfocadas en el archivo “access_log” presente en el directorio “udacity_training_data” de la máquina virtual de Cloudera.**

 - a. ¿Cuántas peticiones GET devolvieron un error 4XX? 
 - b. Muestre cuántas peticiones se hacen al servidor agrupadas por mes.
  
En la primera solucion inicia en el **mapper1.py**, esta parte esta encargada de tomas todas las lineas y verificar primero que se encuentre integra(Sin datos perdidos), luego verificamos si el codigo de respuesta corresponde a la serie 400. Cumplida esas condiciones se genera como output el codigo **4XX** y un **1** separados por tabulación.

Los outputs generados por los mappers seran recibidos por el **reducer1.py** como input, aca basicamente se contaran las cantidad de peticiones 4xx de tipo get y daran como un único output la cantidad total.
  
La segunda solucion inicia con el **mapper2.py**, al igual que en el inciso a se verifica la integridad o de lo contrario se salta la linea. Luego basicamente se extrae el mes correpondiente del log y se envia como output de forma: **mes** y un **1** separados por tabulacion.

Los outputs generados por los mappers son recibidos por el **reducer2.py** como input, cabe aclarar que los datos llegaran ordenados por llave, por lo que el resultado sera la cantidad de peticiones agrupadas por mes.
