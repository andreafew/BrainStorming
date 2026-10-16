# 78 · Disponibilizar impresoras en los equipos del Estudio

**Cliente:** A - Estudio · **Sprint:** 2 ·

## Qué se pidió
Dejar las impresoras disponibles en los equipos del Estudio e imprimir una prueba con cada sistema, registrando pasos y minutos.

**Criterio de aceptación:** Impresión de prueba desde un equipo con cada sistema; pasos y minutos registrados.

## Qué se hizo
Se creó un script de PowerShell para instalar la cola de impresión \\192.168.1.60\Estudio_Print en los 30 equipos. Se activó la "Impresión Retenida" para seguridad.
## Datos y resultados
° Equipos configurados: 30 PCs.
° Método: Script de despliegue masivo.
° Seguridad: Impresión Retenida activada (documentos se liberan con credenciales).
Resultados: Todos los equipos tienen la impresora instalada y lista para usar. Los documentos contables no quedan expuestos en la bandeja de salida.
## Conclusión
El despliegue masivo redujo el tiempo de instalación manual. La configuración de seguridad protege la información sensible del cliente.
