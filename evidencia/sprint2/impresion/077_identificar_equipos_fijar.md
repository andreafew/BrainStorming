# 77 · Identificar equipos y fijar IP de impresoras del Estudio

**Cliente:** A - Estudio · **Sprint:** 2 · 

## Qué se pidió
Asignar IP fija a cada impresora del Estudio sin conflictos y comprobarlo con ping.

**Criterio de aceptación:** Tabla de IP fijas sin conflictos, comprobada con ping.

## Qué se hizo
Se configuraron IPs fijas fuera del rango DHCP del router del estudio. Se validó la conectividad con ping desde 3 equipos aleatorios.

## Datos y resultados
| Impresora | Modelo | IP Fija | Ubicación |Ping|
|---|---|---|---|---|
| Color Multifunción | HP OfficeJet Pro 9132e	| 192.168.1.61 | Área Balances | Exitoso (TTL=64)|
| Mono Rápida | Brother HL-L2460DW | 192.168.1.60 | Pasillo Central| Exitoso (TTL=64)|

Resultados: Se creó la tabla de IPs sin conflictos. La conectividad fue validada con éxito desde múltiples equipos.

## Conclusión
Las impresoras tienen direccionamiento estático, lo que garantiza que los 30 equipos siempre las encuentren en la red, evitando reconfiguraciones por cambios de IP.
