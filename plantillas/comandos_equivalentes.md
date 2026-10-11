# Comandos equivalentes (completar con capturas propias)

| Qué se mide | Linux (Ubuntu) | Windows (PowerShell) | Captura Linux | Captura Windows | Observación |
|---|---|---|---|---|---|
| Ver todos los procesos | `ps aux` | `Get-Process` | | | |
| Consumo en vivo | `top` | `Get-Counter` | | | |
| Terminar un proceso | `kill` | `Stop-Process` | | | |
| Memoria disponible | `free -h` | `Get-ComputerInfo` | | | |
| Ver archivos con permisos | `ls -l` | `Get-Acl` | | | |
| Cambiar permisos | `chmod` | `Set-Acl` | | | |
| Crear un usuario | `useradd` | `New-LocalUser` | | | |
| Ver bitácoras del sistema | `journalctl` | `Get-EventLog` (o `Get-WinEvent`) | | | |

Nota: en versiones recientes de PowerShell, `Get-EventLog` solo existe en Windows PowerShell 5.1; en PowerShell 7 se usa `Get-WinEvent`. Anotar cuál se usó.
