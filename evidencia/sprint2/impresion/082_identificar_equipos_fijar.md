# 82 · Identificar equipos y fijar IP de impresoras de la Universidad

**Cliente:** B - Universidad · **Sprint:** 2 ·

## Qué se pidió
Asignar IP fija a cada impresora de la Universidad sin conflictos y comprobarlo con ping.

**Criterio de aceptación:** Tabla de IP fijas sin conflictos, comprobada con ping.

## Qué se hizo
Se configuraron IPs fijas fuera del rango DHCP de la universidad. Se validó con ping desde 3 equipos.

## Datos y resultados
| Impresora | Modelo | IP Fija | Ubicación | Ping|
|---|---|---|---|---|
| Mono 1 | Brother HL-L2460DW | 192.168.1.50 | Sala A | Exitoso (TTL=64)|
| Color 1 |  HP OfficeJet Pro 9132e | 192.168.1.51 | Sala B | Exitoso (TTL=64)|


## Conclusión
Las IPs fijas garantizan que los 25 equipos (Windows y Ubuntu) encuentren las impresoras sin importar cuántas veces se reinicien.
