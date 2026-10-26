# 125 · Prueba de impresión: pasos, tiempo y registro (ambos clientes y ambos sistemas)

**Cliente:** Ambos · **Sprint:** 3 · **Responsable:** [COMPLETAR] · **Fecha:** [COMPLETAR]

## Qué se pidió
Imprimir con el mismo procedimiento y la misma planilla en ambos clientes y sistemas, registrando pasos, tiempo y registro de impresión.

**Criterio de aceptación:** Mismo procedimiento y misma planilla para Estudio y Universidad.

## Qué se hizo
Se ejecutó una prueba de impresión controlada desde una estación Windows 11 y una estación Ubuntu, enviando como documento de prueba el archivo /etc/nsswitch.conf (en Linux) y la página de prueba estándar de Windows. 
Windows 11: Se accedió a Configuración > Bluetooth y dispositivos > Impresoras y escáneres > Propiedades de la impresora > Imprimir página de prueba.

Ubuntu: Se ejecutó el comando lp -d [Nombre_Cola] /etc/nsswitch.conf desde la terminal.


## Datos y resultados
Se verificó la salida física del documento y se registró el tiempo total del procedimiento (desde el envío hasta la confirmación de impresión). Se utilizó la misma planilla de registro para ambos entornos, garantizando la comparabilidad de los resultados.
Evidencia: Planilla de registro de pruebas (Anexo D) con los tiempos y observaciones.


## Conclusión
Las incidencias han sido resueltas satisfactoriamente. La isla de impresión se encuentra operativa en ambos entornos (Estudio y Universidad), con direccionamiento IP estático, colas de impresión configuradas y pruebas de funcionamiento validadas. La homogeneización de los procedimientos y el uso de una planilla de registro común permiten una gestión unificada y facilitan el mantenimiento futuro.
