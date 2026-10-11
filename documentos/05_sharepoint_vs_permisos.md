# 05 · SharePoint vs permisos locales
Objetivo: que cada usuario vea solo sus archivos y carpetas, al menor costo.
| | SharePoint (Microsoft 365) | Permisos NTFS en el servidor |
|---|---|---|
| Costo | Se paga por usuario (ver 03): desde USD 1.944 al año por 30 usuarios en el plan más barato citado | Sin costo de licencia adicional si el servidor ya existe para Tango |
| Conexión | Necesita internet estable | Funciona en la red local |
| Permisos por usuario | Sí, por sitio, biblioteca y carpeta | Sí, por carpeta (grupos + ACL) |
| Backup | Versionado y papelera | Hay que armarlo (ver 04) |
| Administración | Portal web | Herramientas de Windows |

**Lectura honesta:** SharePoint solo es "económico" si el estudio además necesita correo y Office del mismo plan; como solución única para separar carpetas, los permisos locales cuestan menos. **Hipótesis provisional:** permisos NTFS locales + copia en la nube, y SharePoint como complemento si se contrata Microsoft 365. Se confirma con la prueba de permisos y la medición de internet del estudio.
