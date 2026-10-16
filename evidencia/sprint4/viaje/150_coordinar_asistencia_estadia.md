# 150 · Coordinar asistencia y estadía de dos recursos en Tierra del Fuego

**Cliente:** A - Estudio · **Sprint:** 4 · **Responsable:** Lopez Salomon Federico · **Fecha:** 16/10/2026

## Qué se pidió
Planificar la asistencia y estadía de dos recursos en Tierra del Fuego: pasajes, alojamiento y costos.

**Criterio de aceptación:** Plan logístico (jueves a lunes, entre el 8 y el 25 del mes) con pasajes, alojamiento y costos.

## Qué se hizo
Se armó el plan logístico para dos técnicos de la consultora que viajan al Estudio. El viaje **no se realiza**: sirve para mostrar cómo se trabajaría. Se tomó como base `documentos/06_plan_viaje.md` y se lo ajustó a tres decisiones ya tomadas por el equipo:

1. **Las 20 notebooks se compran en destino** (evidencia 50, Zona Franca Tech, Ushuaia). Por eso no hay flete de equipos y el plan incluye la recepción de las notebooks.
2. **El servidor de Tango va a estar en la nube** (ver `documentos/08_servidor_en_la_nube.md`). Los pasos que hablaban de un servidor físico se reescribieron como migración a la nube.
3. **El viaje es de jueves a lunes**, como pide el criterio: son 5 días de trabajo y **4 noches** de alojamiento (jueves, viernes, sábado y domingo). El documento 06 decía 5 noches; con jueves a lunes son 4.

### Supuestos
Todo lo que sigue es **SUPUESTO** hasta que se confirme con el cliente o se mida.
- Destino: **Ushuaia** (ciudad del proveedor elegido en la evidencia 50). (a confirmar con el equipo)
- Tiempo por equipo: 60 minutos con la imagen estándar, es decir 30 equipos ≈ 30 h, unas 15 h por técnico. Es un supuesto hasta medirlo en la tarea de imagen estándar.
- Parque a atender: 20 notebooks nuevas y 10 equipos existentes (7 a reinstalar con Windows 11 y 3 que solo actualizan licencia).
- El sábado y el domingo el Estudio no atiende: se aprovechan para trabajar sin interrumpir a los empleados. (a confirmar con el equipo)

### Ventana de fechas
El criterio pide jueves a lunes dentro del 8 al 25 del mes. Propuesta, si el viaje fuera en noviembre de 2026:

| Opción | Salida (jueves) | Regreso (lunes) | Observación |
|---|---|---|---|
| A (recomendada) | 12/11 | 16/11 | Sin feriados cercanos conocidos |
| B | 19/11 | 23/11 | Verificar feriados del período antes de elegirla |

El mes definitivo lo decide el equipo en la planificación del Sprint 4.

### Plan día por día
| Día | Fecha (opción A) | Tareas |
|---|---|---|
| 1 | Jueves 12/11 | Vuelo EZE a USH, sale 03:50 y llega 07:30. Revisión de la red y de internet. Medición de la latencia hacia la nube. Backup completo de cada usuario y del servidor Tango actual. Recepción de las 20 notebooks compradas en destino. |
| 2 | Viernes 13/11 | Despliegue de la imagen en 10 notebooks nuevas. Migración de archivos de los usuarios. |
| 3 | Sábado 14/11 | Despliegue en las otras 10 notebooks. Alta del servidor Tango en la nube y restauración de la base. |
| 4 | Domingo 15/11 | Verificar requisitos y reinstalar los 7 equipos. Actualizar la licencia de los 3. Isla de impresión y permisos de usuarios. |
| 5 | Lunes 16/11 | Capacitación del primer día, pruebas de cierre, entrega de la guía y del plan de soporte. La capacitación debe terminar antes de las 17:30 para llegar al aeropuerto a tiempo. Vuelo USH a EZE a las 20:35, llega a las 00:05 del martes 17/11. |

**Plan B si algo falla:** soporte remoto desde el continente, un equipo de reposo y la posibilidad de extender un día (con costo adicional de alojamiento y viáticos; no está en el presupuesto base).

## Datos y resultados
> **Valores provisionales.** Los pasajes y el alojamiento se leyeron de una fuente, con captura. Viáticos y herramientas son **ESTIMACIÓN del equipo, sin cotizar**. Antes de la entrega final hay que reemplazarlas por valores con fuente y fecha.

### Presupuesto del viaje (ARS)
| Ítem | Cantidad | Precio unitario | Total | Fuente / fecha | Tipo de dato |
|---|---|---|---|---|---|
| Pasajes aéreos ida y vuelta (Buenos Aires a Ushuaia, jue. 12/11 a lun. 16/11, 2 personas) | 2 | 231.557,50 | 463.115 | Despegar, pantalla "Detalle del pago" (vuelo 302.205 + impuestos y tasas 160.910), consultado el 16/10/2026; ver `captura_01_pasajes.png` | LEÍDO |
| Alojamiento: Gente del Sur - Cinco Hermanos (4 estrellas, Av. San Martín 1138), Estudio Deluxe con 1 cama doble grande, solo hospedaje, 1 habitación para los 2 técnicos, check-in jue. 12/11 y check-out lun. 16/11 (4 noches) | 8 noches-persona (2 personas × 4 noches) | 85.518,88 | 684.151 | Despegar, hoteles de Ushuaia, detalle de la reserva y del pago, consultado el 16/10/2026; ver `captura_02_alojamiento.png` y `captura_03_alojamiento_pago.png` | LEÍDO |
| Viáticos (comidas y traslados locales) | 10 días-persona (2 personas × 5 días) | 50.000 | 500.000 | Estimación del equipo, sin cotizar | ESTIMACIÓN |
| Flete de equipos | No aplica | 0 | 0 | Las notebooks se compran en destino (evidencia 50) | DECISIÓN |
| Herramientas y medios (pendrives, cables, adaptadores) | 1 lote | 60.000 | 60.000 | Estimación del equipo, sin cotizar | ESTIMACIÓN |
| **Total estimado** | | | **1.707.266** | Suma de los totales anteriores | |

Cómo se calculó: pasajes 302.205 + 160.910 = 463.115; alojamiento para 2 personas 1.023.025 + 117.227 de impuestos y tasas − 456.100 de descuento = 684.152, que la pantalla ("A pagar al alojamiento", `captura_03_alojamiento_pago.png`) muestra redondeado como 684.151 (por noche-persona: 684.151 ÷ 8 = 85.518,88); viáticos 10 × 50.000 = 500.000; 463.115 + 684.151 + 500.000 + 60.000 = 1.707.266.

### Límites de los datos
- El precio de los pasajes corresponde exactamente a las fechas propuestas (jueves 12/11 a lunes 16/11, 2 personas) y es el precio sin descuento de socio. Es una consulta del 16/10/2026 y puede variar hasta la compra.
- Condiciones de la tarifa: los cambios tienen costo y la cancelación no es reembolsable. Los íconos de equipaje parecen indicar solo equipaje de mano; hay que verificarlo en "Ver más detalle" porque los técnicos llevan herramientas.
- El alojamiento elegido es un hotel de 4 estrellas sobre la Av. San Martín, con una cama doble grande para los dos técnicos y **solo hospedaje** (sin desayuno). El precio incluye un descuento de 456.100 y está convertido desde US$ 453 (unos ARS 1.510 por dólar), así que puede variar con la promoción y el tipo de cambio. La pantalla lo titula "a pagar al alojamiento" y la reserva indica que el proveedor se contactará para informar el cobro y la forma de pago, y que puede pedir un pago adicional por daños o gastos extras.
- Horarios del hotel: check-in a las 14:00 y check-out a las 10:00. Como el vuelo llega a las 07:30 y sale a las 20:35, hay que pedir guardar el equipaje el jueves y el lunes, o gestionar check-in anticipado y late check-out.
- **Alternativa más económica** (a elegir por el equipo): habitación cuádruple estándar de 14 m² con 4 camas individuales y desayuno, ARS 286.000 por las 4 noches ("precio más bajo disponible", con 45% de descuento y "solo queda 1"; cancelación gratis hasta el 12/11/2026 a las 14:00). Con esa opción el total del viaje sería ARS 1.309.115. Falta anotar el nombre de ese hotel.
- Los 50.000 por día de viáticos y los 60.000 de herramientas son supuestos de trabajo, sin cotizar.
- El costo de las notebooks no entra en este presupuesto: se calcula aparte en las evidencias 36 y 50.

### Qué falta para cerrar el costo
- Confirmar con el equipo cuál de las dos opciones de alojamiento se usa y verificar que quede cerca del Estudio.
- Definir de dónde sale el monto de viáticos (por ejemplo, la tabla de viáticos de la propia consultora).
- Reemplazar las filas de ESTIMACIÓN (viáticos y herramientas) por valores con fuente y pasar el tipo de dato a LEÍDO.

## Capturas

![Cotización de pasajes](<img width="565" height="708" alt="captura_01_pasajes" src="https://github.com/user-attachments/assets/397facc7-ed26-44d3-aa3b-f9c55f5384dd" />)
![Detalle de la reserva del alojamiento](<img width="1247" height="731" alt="captura_02_alojamiento" src="https://github.com/user-attachments/assets/20a2ddba-a470-44e7-a42b-7277e8881f9b" />)
![Desglose del pago del alojamiento](<img width="527" height="402" alt="captura_03_alojamiento_pago" src="https://github.com/user-attachments/assets/bbaa1c88-d485-4372-9132-4f701bb5860b" />)
![Alternativa económica de alojamiento](<img width="1535" height="595" alt="captura_04_alojamiento_alternativa" src="https://github.com/user-attachments/assets/1d5f49f9-8924-415d-a38b-f117c576c1b1" />)

## Conclusión
Con los datos actuales, el viaje de dos técnicos a Ushuaia (jueves 12/11 a lunes 16/11, 4 noches) costaría unos **ARS 1.707.266**, de los cuales ARS 1.147.266 (pasajes por 463.115 y alojamiento por 684.151, ambos con captura) salen de una fuente leída y el resto es estimación. Con la alternativa de alojamiento más económica el total sería ARS 1.309.115. No hay flete porque las notebooks se compran en destino. Los supuestos que siguen sin confirmar son la ciudad del Estudio, sus horarios de fin de semana, el mes del viaje y los montos de viáticos y herramientas. El plan es de referencia: el viaje no se realiza.
