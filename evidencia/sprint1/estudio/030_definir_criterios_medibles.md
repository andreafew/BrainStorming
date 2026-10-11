# 30 · Definir criterios medibles del Estudio

**Cliente:** A - Estudio · **Sprint:** 1 · 

## Qué se pidió
Definir, para el Estudio, cada criterio de evaluación con su unidad y su método de medición, evitando expresiones vagas, para que luego la comparación entre sistemas sea objetiva.

**Criterio de aceptación:** Cada criterio con unidad y método; ninguno del tipo 'que sea fácil/rápido/moderno'. Pregunta de control: si otro equipo mide igual, ¿da lo mismo?

## Qué se hizo
Se definieron 10 criterios de evaluación para el Estudio Contable. Cada uno tiene una unidad de medida y un método de medición concreto, y un peso que indica cuánto influye en la decisión final. Los pesos suman 100.

Los criterios se definieron a partir de las respuestas del cuestionario al Estudio (tarea 6).

## Datos y resultados

| Criterio | Unidad | Cómo se mide | Peso | Por qué importa |
|---|---|---|---|---|
| CA-01 Compatibilidad con Tango, planillas, correo y firma digital | Funciones OK / probadas | Prueba funcional en cada sistema. Lo que no se pueda probar se marca 'leído, no comprobado' con la fuente. | 20 | Si Tango o la firma digital no funcionan, el estudio no puede operar. |
| CA-02 Costo total del primer año (30 equipos y servidor en la nube) | ARS o USD | Suma de licencias, soporte, capacitación y nube con precio oficial vigente, fuente y fecha. | 15 | Es una de las dos preocupaciones explícitas del dueño. |
| CA-03 Curva de aprendizaje | Minutos y ayudas | Una persona sin formación hace 5 tareas habituales en cada sistema; se cronometra y se cuentan las ayudas. | 15 | El dueño no quiere que su gente pierda una semana aprendiendo. |
| CA-04 Años de actualizaciones de seguridad | Años | Fecha de fin de soporte publicada por el fabricante, con fuente oficial y fecha de consulta. | 10 | Equipos con datos de clientes no pueden quedar sin parches. |
| CA-05 Separación de archivos entre usuarios | Acciones denegadas de 3 | Con el usuario 2 se intenta abrir, modificar y borrar un archivo del usuario 1. | 10 | Cada empleado maneja información reservada. |
| CA-06 Recuperación ante falla o migración | Minutos | Tiempo para restaurar un equipo y el servidor en la nube desde backup o imagen hasta quedar operativos. | 8 | Responde a '¿qué pasa si falla un martes a las 9?'. |
| CA-07 Despliegue por equipo | Minutos por equipo | Tiempo de instalación con imagen estándar, cronometrado de principio a fin. | 7 | Son 30 equipos y pocos días de trabajo. |
| CA-08 Conectar una impresora nueva | Pasos | Cantidad de pasos y minutos desde cero, con captura de cada pantalla. | 5 | Se imprime a diario, pero la tarea es acotada. |
| CA-09 Tiempo de arranque | Segundos (mediana de 3) | Cronómetro desde el encendido hasta poder abrir un programa. | 5 | Impacta cada mañana, aunque menos que el resto. |
| CA-10 Aviso antes de ejecutar un programa descargado | Sí / No | Se descarga un instalador de prueba y se registra si el sistema avisa. | 5 | Protege a usuarios sin formación informática. |
| **Total** | | | **100** | |

### Pregunta de control
Para cada criterio: si otro equipo repitiera la medición, ¿obtendría el mismo resultado?

| Criterio | ¿Otro equipo obtendría lo mismo? | Observación |
|---|---|---|
| CA-01 | Sí | Las funciones a probar quedan listadas de antemano; lo que no se pueda probar se marca como «leído, no comprobado» con su fuente. |
| CA-02 | Sí | Con la misma fuente oficial y la misma fecha de consulta, el precio es el mismo. |
| CA-03 | Sí, con condiciones | Depende de la persona. Usar las mismas 5 tareas en el mismo orden y registrar su nivel previo. |
| CA-04 | Sí | Es una fecha publicada por el fabricante, con fuente y fecha de consulta. |
| CA-05 | Sí | Se intentan siempre las mismas 3 acciones sobre el mismo archivo. |
| CA-06 | Sí, con condiciones | Depende del equipo y de la conexión. Anotar el hardware y la velocidad de internet usados. |
| CA-07 | Sí, con condiciones | Depende de la máquina. Usar la misma imagen y el mismo equipo para ambos sistemas. |
| CA-08 | Sí | Se cuentan pasos y minutos desde cero, con la misma impresora. |
| CA-09 | Sí | Mediana de 3 repeticiones en el mismo equipo. |
| CA-10 | Sí | Se descarga el mismo instalador de prueba en ambos sistemas. |
