# 77 · Identificar equipos y fijar IP de impresoras del Estudio

**Cliente:** A - Estudio · **Sprint:** 2 · **Responsable:** [COMPLETAR] · **Fecha:** [COMPLETAR]

## Qué se pidió
Asignar IP fija a cada impresora del Estudio sin conflictos y comprobarlo con ping.

**Criterio de aceptación:** Tabla de IP fijas sin conflictos, comprobada con ping.

## Qué se hizo
Se configuraron IPs fijas fuera del rango DHCP del router del estudio. Se validó la conectividad con ping desde 3 equipos aleatorios.

## Datos y resultados
| Impresora | Modelo | IP Fija | Ubicación |
|---|---|---|---|
| Mono Rápida | Brother HL-L2460DW | 192.168.1.60 | Pasillo Central|

## Capturas
Subir las imágenes a esta misma carpeta y enlazarlas así:

<!-- ![Descripción de la captura](captura_01.png) -->

## Conclusión
Las impresoras tienen direccionamiento estático, lo que garantiza que los 30 equipos siempre las encuentren en la red, evitando reconfiguraciones por cambios de IP.
