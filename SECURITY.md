```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Este documento describe nuestras políticas y prácticas de seguridad, proporcionando información sobre cómo reportar vulnerabilidades, las medidas de seguridad implementadas y las mejores prácticas para contribuir de forma segura al proyecto.

Este documento cubre los siguientes aspectos:

*   Cómo reportar vulnerabilidades de seguridad de manera responsable.
*   Prácticas de seguridad implementadas en el proyecto.
*   Vulnerabilidades conocidas y sus mitigaciones.
*   Recursos adicionales para mejorar la seguridad.

## Reportar Vulnerabilidades de Seguridad

Creemos que la seguridad de {project_name} depende de la colaboración entre nuestros desarrolladores y la comunidad de seguridad. Si descubre una vulnerabilidad de seguridad en {project_name}, le agradecemos que nos la informe de manera responsable.

**Por favor, NO cree un issue público en el repositorio de GitHub para reportar una vulnerabilidad de seguridad.** Los issues públicos son visibles para todos y podrían exponer la vulnerabilidad antes de que tengamos la oportunidad de abordarla.

En su lugar, envíe un correo electrónico a {contact_email} con los detalles de la vulnerabilidad.

Por favor, incluya la siguiente información en su reporte:

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad.
*   Versión(es) de {project_name} afectadas.
*   Posibles impactos de la vulnerabilidad.
*   Sugerencias para la mitigación (si las tiene).

Nuestro equipo de seguridad responderá a su reporte dentro de los **3 días hábiles** para confirmar la recepción y comenzar a investigar la vulnerabilidad. Nos comprometemos a trabajar con usted para solucionar la vulnerabilidad de manera oportuna y responsable.

**Proceso de Divulgación Responsable:**

Una vez que hayamos confirmado la vulnerabilidad y desarrollado una solución, trabajaremos con usted para coordinar una divulgación responsable. Esto significa que le daremos la oportunidad de revisar nuestro parche y publicar su propio aviso de seguridad antes de que hagamos pública la información sobre la vulnerabilidad. El plazo específico para la divulgación se acordará mutuamente, teniendo en cuenta la gravedad de la vulnerabilidad y la complejidad de la solución.

## Prácticas de Seguridad

En {project_name}, nos esforzamos por mantener altos estándares de seguridad en todo el ciclo de vida del desarrollo. A continuación, se describen algunas de las prácticas de seguridad clave que implementamos:

### Gestión de Dependencias

Utilizamos herramientas para verificar las dependencias de nuestro proyecto en busca de vulnerabilidades conocidas.

*   **Python:** `pip-audit` y `safety` son herramientas que escanean las dependencias de Python para detectar vulnerabilidades. Puede instalarlas usando `pip install pip-audit safety`.  Para ejecutar una auditoría, use `pip-audit` o `safety check`.

*   **JavaScript:** `npm audit` y `yarn audit` son comandos que escanean las dependencias de JavaScript para detectar vulnerabilidades. Ejecute `npm audit` o `yarn audit` en la raíz de su proyecto.

Es crucial mantener las dependencias actualizadas a las últimas versiones, ya que las actualizaciones a menudo incluyen correcciones de seguridad.  También configuramos alertas de vulnerabilidades en nuestros repositorios de GitHub para recibir notificaciones automáticas sobre nuevas vulnerabilidades en nuestras dependencias.

### Manejo de Secretos

Nunca debemos hardcodear secretos como contraseñas, claves API o claves de cifrado en el código fuente.

*   **Variables de Entorno:** Use variables de entorno para almacenar información confidencial.
*   **.env:**  Cree un archivo `.env` para almacenar variables de entorno localmente, pero asegúrese de agregarlo a su archivo `.gitignore` para evitar que se confirme en el repositorio.

```python
# Ejemplo inseguro: contraseña hardcodeada
password = "mysecretpassword"

# Ejemplo seguro: contraseña desde variable de entorno
import os
password = os.environ.get("DATABASE_PASSWORD")
```

Herramientas como `git-secrets` pueden ayudar a prevenir la confirmación accidental de secretos en el repositorio.

### Validación de Entrada

Siempre valide la entrada del usuario para prevenir ataques de inyección y otros problemas de seguridad.

*   **Validación:**  Verifique que la entrada coincida con el formato esperado y esté dentro de los límites aceptables.
*   **Sanitización:**  Escape o elimine caracteres no válidos de la entrada.

```python
# Ejemplo inseguro: sin validación de entrada
user_input = input("Ingrese su nombre: ")
# El código podría ser vulnerable a inyección de código si el usuario ingresa caracteres especiales.

# Ejemplo seguro: con validación de entrada
import re
user_input = input("Ingrese su nombre: ")
if re.match("^[a-zA-Z]+$", user_input):
    print("Nombre válido")
else:
    print("Nombre inválido")
```

### Gestión de Acceso

Aplique el principio de mínimo privilegio, otorgando a los usuarios y procesos solo los permisos necesarios para realizar sus tareas.

*   **SSH vs HTTPS:** Utilice HTTPS para todas las comunicaciones web y considere el uso de claves SSH para el acceso seguro a los servidores.
*   **Permisos de archivos:** Configure los permisos de archivos y directorios correctamente para evitar el acceso no autorizado.

## Seguridad en CI/CD

La seguridad en las canalizaciones de Integración Continua/Entrega Continua (CI/CD) es crucial para garantizar que el software se entregue de forma segura.

*   **Secrets:**  Utilice sistemas de gestión de secretos como las variables de entorno de Jenkins o GitHub Actions Secrets para almacenar credenciales y claves API de forma segura.
*   **Credenciales:** Evite hardcodear credenciales en los scripts de CI/CD.
*   **Logs:** No registre información confidencial en los registros de CI/CD.

```yaml
# Ejemplo en GitHub Actions:
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy to server
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
          REMOTE_HOST: ${{ secrets.REMOTE_HOST }}
          REMOTE_USER: ${{ secrets.REMOTE_USER }}
        run: |
          # Usa la clave SSH almacenada de forma segura para conectarte al servidor y desplegar el código
          echo "$SSH_PRIVATE_KEY" > private_key
          chmod 400 private_key
          ssh -i private_key ${REMOTE_USER}@${REMOTE_HOST} "deploy.sh"
```

## Testing de Seguridad

Realizamos pruebas de seguridad regulares para identificar y solucionar vulnerabilidades.

*   **Herramientas:** Utilizamos herramientas como `bandit` (para Python) para analizar el código en busca de problemas de seguridad comunes.  Instale con `pip install bandit` y ejecute con `bandit -r ./`.
*   **Análisis SAST:** El análisis estático de seguridad de aplicaciones (SAST) nos ayuda a identificar vulnerabilidades en el código fuente antes de que se implemente.

Ejecute estas herramientas regularmente como parte de su proceso de desarrollo.

## Checklist de Seguridad para Contribuidores

Si contribuye a {project_name}, tenga en cuenta las siguientes pautas de seguridad:

*   No incluya secretos en su código.
*   Evite usar `shell=True` en las llamadas a subprocessos (esto puede ser vulnerable a inyección de comandos).
*   Valide todas las entradas del usuario.
*   No use contraseñas hardcodeadas.
*   Revise cuidadosamente sus cambios antes de enviarlos para detectar posibles problemas de seguridad.

## Vulnerabilidades Conocidas

Esta sección enumera las vulnerabilidades conocidas en {project_name} y sus mitigaciones.

*   **[CVE-YYYY-NNNNN] Vulnerabilidad de Cross-Site Scripting (XSS)**
    *   Versiones afectadas: 1.0.0 - 1.0.5
    *   Mitigación: Actualice a la versión 1.0.6 o posterior.
    *   Descripción: Una vulnerabilidad XSS permite a un atacante inyectar scripts maliciosos en las páginas web vistas por otros usuarios.

*   **[CVE-YYYY-MMMMM] Vulnerabilidad de Inyección SQL**
    *   Versiones afectadas: 1.1.0 - 1.2.2
    *   Mitigación: Actualice a la versión 1.2.3 o posterior. Se han implementado consultas parametrizadas para prevenir la inyección SQL.

## Recursos de Seguridad

Los siguientes recursos pueden ayudarle a mejorar su conocimiento de la seguridad del software:

*   [OWASP Top 10](https://owasp.org/www-project-top-ten/): Una lista de las vulnerabilidades de seguridad web más críticas.
*   [Python Security Best Practices](https://wiki.python.org/moin/Security):  Una guía de las mejores prácticas de seguridad para el desarrollo de Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Una lista de los errores de software más peligrosos y generalizados.

## Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en ponerse en contacto con nosotros.

*   Para reportar una vulnerabilidad de seguridad, envíe un correo electrónico a {contact_email}.
*   Para otras consultas, puede crear un issue en el repositorio de GitHub: {repository_url}.
```