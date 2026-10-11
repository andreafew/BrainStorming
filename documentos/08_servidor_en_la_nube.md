# 08 · Servidor en la nube (Estudio y Universidad)

Nada de esto se contrata ni se ejecuta. Es la propuesta que el equipo entrega a los dos clientes con el mismo esquema.
Los precios se completan con **fuente oficial y fecha de consulta**; no se escriben de memoria.

## Qué se pone en la nube
| | Estudio Contable (A) | Universidad (B) |
|---|---|---|
| Función | Tango y su base de datos (versión **SUPUESTO**) | Perfiles de usuario, espacio de alumnos, impresión y repositorio de software |
| Sistema del servidor | Windows Server compatible con Tango y SQL Server (verificar con el distribuidor) | Ubuntu Server o Windows Server, según resulte de las pruebas |
| Usuarios | 30 | Los 25 equipos del laboratorio |

## Pasos (mismo orden para ambos)
1. **Elegir proveedor:** comparar al menos 2 con CPU, RAM, disco, región, precio mensual, fuente y fecha.
2. **Dimensionar:** partir de los requisitos publicados por el fabricante de cada programa y sumar margen.
3. **Conectividad:** medir o relevar el ancho de banda del cliente y calcular el mínimo por usuario simultáneo. Si el enlace no alcanza, queda registrado como riesgo.
4. **Seguridad:** acceso por VPN o escritorio remoto con doble factor, un usuario por persona, permisos por rol.
5. **Migración:** backup completo del servidor actual, restauración en la nube, prueba con 2 usuarios y recién después corte.
6. **Vuelta atrás:** el servidor viejo se conserva hasta que la restauración esté probada.
7. **Backup en la nube:** copia automática y prueba de restauración cronometrada (criterios CA-06 y CB-01).

## Riesgos a registrar
| Riesgo | Respuesta |
|---|---|
| Se cae la conexión a internet | Plan de contingencia y segundo enlace si el cliente lo justifica |
| Costo mensual mayor al estimado | Alerta de gasto y revisión trimestral |
| Latencia alta en Tierra del Fuego (Estudio) | Medir antes de decidir; documentar el resultado |
| Licencia del servidor no incluida | Incluirla en el costo (criterios CA-02 y CB-02) |
