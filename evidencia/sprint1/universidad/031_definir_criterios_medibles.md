# 31 · Definir criterios medibles de la Universidad

**Cliente:** B - Universidad · **Sprint:** 1 · 

## Qué se pidió
Definir, para la Universidad, cada criterio de evaluación con su unidad y su método de medición (incluidos tiempo de restauración y permisos), para que la comparación sea objetiva.

**Criterio de aceptación:** Igual que el ítem anterior, incluyendo tiempo de restauración y manejo de permisos.

## Qué se hizo
Se definieron 10 criterios de evaluación para el laboratorio de la Universidad (25 equipos). Cada uno tiene una unidad de medida y un método de medición concreto, y un peso que indica cuánto influye en la decisión final. Los pesos suman 100.

Los criterios se definieron a partir de las respuestas del cuestionario a la Universidad (tarea 7)

## Datos y resultados

| Criterio | Unidad | Cómo se mide | Peso | Por qué importa |
|---|---|---|---|---|
| CB-01 Restauración del estado original | Minutos y cambios revertidos | Se instalan y borran programas y archivos, se restaura con la herramienta elegida y se verifica. | 20 | Es la frase central del cliente: 'como las dejé el viernes'. |
| CB-02 Costo del primer año (25 equipos y servidor en la nube) | ARS o USD | Precio oficial vigente de sistema, software y nube, con fuente y fecha. | 15 | El presupuesto no alcanza para licencias caras. |
| CB-03 Aislamiento entre usuarios | Acciones denegadas de 3 | Con el usuario 2 se intenta abrir, modificar y borrar un archivo del usuario 1. | 15 | Cientos de estudiantes comparten los equipos. |
| CB-04 Compatibilidad con el software de las materias | Programas OK / requeridos | Instalación y ejecución de las herramientas de programación, bases de datos, diseño y ofimática. | 15 | Cada materia pide software distinto. |
| CB-05 Administración de usuarios | Minutos para crear 20 usuarios | Se crean 20 usuarios y se asignan a un grupo por terminal; se cronometra. | 10 | Hay decenas de usuarios distintos por administrar. |
| CB-06 Memoria RAM en reposo | MB | Get-Counter o free -m tras 5 minutos sin tocar nada. | 5 | Los equipos pueden ser modestos. |
| CB-07 Tiempo de arranque | Segundos (mediana de 3) | Cronómetro desde el encendido hasta poder abrir un programa. | 5 | Cada clase empieza con la sala encendida. |
| CB-08 Instalación de herramientas de programación | Minutos | Se cronometra la instalación de compilador, editor y base de datos. | 5 | Los estudiantes instalan sus propias herramientas. |
| CB-09 Años de actualizaciones de seguridad | Años | Fecha de fin de soporte publicada por el fabricante, con fuente y fecha de consulta. | 5 | Importa, pero la sala se restaura con frecuencia. |
| CB-10 Registro de impresión por usuario | Impresiones registradas | Dos usuarios imprimen y se revisa el registro de la cola. | 5 | Control del uso de la isla de impresión. |
| **Total** | | | **100** | |

### Pregunta de control
Para cada criterio: si otro equipo repitiera la medición, ¿obtendría el mismo resultado?

| Criterio | ¿Otro equipo obtendría lo mismo? | Observación |
|---|---|---|
| CB-01 | Sí, con condiciones | Depende de la herramienta de restauración elegida. Usar siempre la misma lista de programas y archivos a instalar y borrar. |
| CB-02 | Sí | Con la misma fuente oficial y la misma fecha de consulta, el precio es el mismo. |
| CB-03 | Sí | Se intentan siempre las mismas 3 acciones sobre el mismo archivo. |
| CB-04 | Sí, con condiciones | La lista de programas queda definida de antemano; anotar la versión instalada de cada uno. |
| CB-05 | Sí, con condiciones | Depende de si se usa la interfaz gráfica o la terminal. Usar el mismo método y la misma planilla de 20 usuarios. |
| CB-06 | Sí, con condiciones | Depende de lo que haya abierto. Medir siempre tras 5 minutos sin tocar nada y con el mismo equipo. |
| CB-07 | Sí | Mediana de 3 repeticiones en el mismo equipo. |
| CB-08 | Sí, con condiciones | Depende de la velocidad de internet. Anotar la conexión usada y el horario. |
| CB-09 | Sí | Es una fecha publicada por el fabricante, con fuente y fecha de consulta. |
| CB-10 | Sí | Se usan siempre los mismos 2 usuarios y la misma impresora. |
