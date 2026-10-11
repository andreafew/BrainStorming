> **NOTA:** el servidor va a estar **en la nube** (ver `08_servidor_en_la_nube.md`). Donde este documento habla de un servidor físico en el sitio, leer 'servidor virtual en la nube'.

# 04 · Backups y servidor Tango
## Antes de tocar el equipo servidor
1. Avisar al estudio y elegir un horario sin operaciones; cerrar Tango en todos los puestos.
2. **Backup de la base de datos** (T-SQL, con el nombre real de la base): `BACKUP DATABASE [NombreBase] TO DISK = 'D:\Backups\NombreBase.bak' WITH CHECKSUM;`
3. **Imagen completa del disco** del servidor (por ejemplo con una herramienta de imágenes) y copia de la carpeta de instalación y los archivos compartidos.
4. Regla 3-2-1: **3 copias**, en **2 soportes**, **1 fuera del estudio**.
5. **Restauración probada** en otra máquina (puede ser una VM propia): restaurar el `.bak`, abrir Tango y comprobar un balance conocido.
6. Recién con la restauración probada se retira el servidor viejo.

## Backups por usuario
- Copia: `robocopy "C:\Users\USUARIO" "D:\Backups\USUARIO" /MIR /R:1 /W:1 /LOG:backup_USUARIO.log`
- Verificación: `(Get-ChildItem -Recurse -File ORIGEN | Measure-Object).Count` debe ser igual al del destino.
- Evidencia: log de robocopy + las dos cantidades en una tabla (30 usuarios).

## Después
Tabla: equipo, hash o cantidad de archivos, fecha, responsable, resultado. Guardar en `evidencia/sprint3/`.
