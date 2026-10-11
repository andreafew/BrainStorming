# 32 · Plan de pruebas común para ambos sistemas

**Cliente:** Ambos · **Sprint:** 1 · 

## Qué se pidió
Escribir un único plan de pruebas que se aplique igual a Windows 11 y Ubuntu y a los dos clientes (versión, hardware, repeticiones y programas), para que los resultados sean comparables.

**Criterio de aceptación:** Plan con: versión y edición de cada SO, hardware usado, número de repeticiones y programas abiertos en cada prueba. Como se prueba en VirtualBox sobre notebooks de integrantes: misma RAM, CPU virtuales y disco en ambas VM, y nota de limitaciones (una VM no equivale a un equipo real ni a las PC de escritorio de la Universidad).

## 1. Objetivo
Medir Windows 11 y Ubuntu con **el mismo procedimiento, en las mismas condiciones y para los dos clientes** (Estudio Contable y Universidad), de modo que las diferencias que aparezcan se deban al sistema operativo y no al método.

## 2. Entorno de pruebas

### 2.1 Sistemas operativos
| | Windows 11 | Ubuntu |
|---|---|---|
| Edición | [COMPLETAR: por ejemplo, Pro] | Desktop |
| Versión | [COMPLETAR] | [COMPLETAR: versión LTS] |
| Compilación / kernel | [COMPLETAR] | [COMPLETAR] |
| Idioma | [COMPLETAR] | [COMPLETAR] |
| Origen de la imagen (ISO) y fecha de descarga | [COMPLETAR] | [COMPLETAR] |

Cómo obtener los datos (referencia): en Windows, `winver` o `Get-ComputerInfo | Select WindowsProductName, WindowsVersion, OsBuildNumber`; en Ubuntu, `lsb_release -a` y `uname -r`.

### 2.2 Virtualización
| Dato | Valor |
|---|---|
| Programa de virtualización | VirtualBox [COMPLETAR: versión] |
| Máquina anfitriona (notebook) | [COMPLETAR: modelo, procesador, RAM, disco libre] |
| Integrante que aporta la máquina | [COMPLETAR] |

### 2.3 Configuración de las máquinas virtuales
Las dos máquinas virtuales tienen **la misma configuración**:

| Recurso | Windows 11 | Ubuntu |
|---|---|---|
| RAM | [COMPLETAR] | [COMPLETAR: igual que Windows] |
| CPU virtuales | [COMPLETAR] | [COMPLETAR: igual que Windows] |
| Disco | [COMPLETAR] | [COMPLETAR: igual que Windows] |
| TPM 2.0 y Secure Boot | Sí (requisito de Windows 11) | No aplica |

Referencia: Microsoft exige para Windows 11 un mínimo de 4 GB de RAM, 2 núcleos, 64 GB de almacenamiento, TPM 2.0 y Secure Boot. Verificar el dato en la documentación oficial antes de definir la configuración.

## 3. Reglas comunes a todas las pruebas
1. Cada prueba se repite **3 veces** y se informa la **mediana**, salvo que el backlog indique otra cosa.
2. Siempre se usa la misma máquina anfitriona y la misma configuración de máquina virtual para ambos sistemas.
3. Antes de cada medición se reinicia la máquina virtual y no se abren programas que la prueba no pida.
4. Las actualizaciones automáticas se dejan en el mismo estado en ambos sistemas (instaladas o postergadas, según se decida) y se anota cuál.
5. Se registra la fecha, la hora y quién midió.
6. Cada resultado se acompaña de una captura, un dato de terminal o un cronometraje, guardado en `evidencia/` y enlazado desde la tabla de resultados.
7. Lo que no se pudo comprobar se marca como «leído, no comprobado» y se cita la fuente. No se presenta como medido.

## 4. Programas abiertos en cada prueba
| Prueba | Programas abiertos |
|---|---|
| Arranque | Ninguno: se mide hasta poder abrir un programa |
| RAM en reposo | Ninguno, tras 5 minutos sin tocar nada |
| Memoria con programas abiertos | [COMPLETAR: por ejemplo, navegador, planilla y editor de texto, los mismos en ambos sistemas] |
| Compatibilidad y aprendizaje | Los propios del cliente (ver cada prueba) |

## 5. Pruebas del plan
| Prueba | Qué mide | Criterio asociado | Cliente | N.º del backlog |
|---|---|---|---|---|
| Tiempo de arranque | Segundos hasta poder abrir un programa | CA-09, CB-07 | Ambos | 120 |
| RAM y procesos en reposo | MB ocupados y cantidad de procesos | CB-06 | Ambos | 121 |
| Memoria con los mismos programas abiertos | MB por proceso | Dato complementario | Ambos | 122 |
| Espacio en disco tras la instalación | GB usados | Dato complementario | Ambos | 123 |
| Avisos de seguridad y soporte | Aviso ante un instalador de prueba; años de soporte | CA-10, CA-04, CB-09 | Ambos | 124 |
| Compatibilidad del software | Funciones o programas OK | CA-01 / CB-04 | Estudio / Universidad | 91 / 106 |
| Curva de aprendizaje | Minutos y ayudas en 5 tareas | CA-03 | Estudio / Universidad | 92 / 107 |
| Usuarios, grupos y permisos | Acciones denegadas de 3 | CA-05 / CB-03 | Estudio / Universidad | 94 / 100 |
| Impresión | Pasos, tiempo y registro | CA-08 / CB-10 | Ambos | 125 |
| Restauración del equipo | Minutos y cambios revertidos | CB-01 | Universidad (y Estudio, mismo método) | 98 / 110 |
| Restauración del servidor | Minutos hasta quedar operativo | CA-06 | Ambos | 104 |
| Clonación de imagen | Minutos por equipo | CA-07 | Ambos | 99 / 111 |
| Gestión de procesos desde la terminal | Ver qué corre y detener un programa colgado | Dato complementario | Ambos | 93 |

## 6. Limitaciones
- Una máquina virtual **no equivale a un equipo real**: el rendimiento depende de la notebook anfitriona y de lo que esté usando en ese momento.
- Las notebooks de los integrantes **no reproducen** las computadoras de escritorio del laboratorio de la Universidad ni los equipos del Estudio.
- Los tiempos de restauración y de despliegue son orientativos, porque no se prueban sobre los 30 equipos del Estudio ni sobre los 25 de la Universidad.
- Los resultados sirven para comparar un sistema con otro **en las mismas condiciones**, no para predecir valores absolutos en el cliente.

[COMPLETAR: otras limitaciones que el equipo detecte]

## Capturas

<!-- ![Configuración de la VM de Windows 11](captura_01_vm_windows.png) -->
<!-- ![Configuración de la VM de Ubuntu](captura_02_vm_ubuntu.png) -->
<!-- ![Versión de Windows (winver)](captura_03_winver.png) -->
<!-- ![Versión de Ubuntu (lsb_release)](captura_04_ubuntu_version.png) -->

## Conclusión
[COMPLETAR: confirmar que el plan fue revisado por otro integrante y que todas las pruebas del Sprint 3 siguen este procedimiento]
