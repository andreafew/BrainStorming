> **NOTA:** el servidor va a estar **en la nube** (ver `08_servidor_en_la_nube.md`). Donde este documento habla de un servidor físico en el sitio, leer 'servidor virtual en la nube'.

# 02 · Tango, requisitos y hardware
## Supuesto de versión
**SUPUESTO DE TRABAJO:** Tango Gestión **Delta 6**, a confirmar con el cliente. Los requisitos salen de la página de un revendedor ([Grupo Tesys](https://grupotesys.com.ar/tango-gestion/tango-software-delta6-requerimientos-tecnicos)); la página del fabricante (Axoft) no pudo consultarse. Marcar en el informe como **LEÍDO, no comprobado**.

## Requisitos de Tango Delta 6 (según el revendedor)
| | Mínimo | Recomendado |
|---|---|---|
| Servidor | Win 10 64 b o Server 2019; i5-3550 / Ryzen 3 1200; 8 GB; 100 GB libres | Win 11 o Server 2022; i5-10400 / Ryzen 5 5600; 16 GB; 100 GB SSD libres; red 1000 Mbps |
| Terminales | Win 10; i3-3210 / Athlon 3000; 4 GB; 50 GB | Win 10; i3-10105 / Ryzen 3 3200G; 8 GB; SSD 50 GB |
- Sistemas compatibles: **Windows 11 Pro**, Windows 10 64 bits (Pro, Education, Enterprise), Windows Server 2019, 2022, 2025. **No figura Linux ni Windows Home.**
- SQL Server 2017, 2019, 2022 o 2025; sistema de archivos **NTFS**; con **5 o más estaciones** conviene servidor dedicado.

## Requisitos de Windows 11 (Microsoft)
64 bits, 2 núcleos a 1 GHz, 4 GB RAM, 64 GB, **UEFI con Secure Boot**, **TPM 2.0**, DirectX 12. Fuente: [Microsoft](https://www.microsoft.com/es-ar/windows/windows-11-specifications).

## Especificación propuesta
| Equipo | Propuesta | Por qué |
|---|---|---|
| Notebook (30) | Core i5 o Ryzen 5 reciente, **16 GB RAM**, **SSD 512 GB**, TPM 2.0, USB-A (token de firma), **Windows 11 Pro** | Supera el recomendado de Tango (8 GB, SSD) y cumple Windows 11; Pro porque Tango lista Pro y no Home |
| Servidor Tango (1) | Equipo dedicado: i5-10400 o Ryzen 5 5600 o superior, 16 GB, SSD con ≥100 GB libres + disco de backup, red 1000 Mbps, Windows 11 Pro o Server 2022 | Es el recomendado del fabricante para multiusuario |
> Verificar en la tarea de requisitos de Windows 11 las 10 máquinas existentes (7 con Windows 10 reinstaladas, 3 con Windows 11): sin TPM 2.0 o Secure Boot no cumplen.
