```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Este documento describe nuestras prácticas de seguridad, cómo reportar vulnerabilidades y las medidas que tomamos para proteger a nuestros usuarios y datos.

Este documento cubre:

*   Cómo reportar vulnerabilidades de seguridad de forma responsable.
*   Prácticas recomendadas de seguridad para desarrolladores y usuarios.
*   Vulnerabilidades conocidas y sus mitigaciones.
*   Funciones de seguridad implementadas y sus limitaciones.

## Reportar Vulnerabilidades de Seguridad

Creemos que la seguridad de {project_name} se fortalece con la colaboración de la comunidad. Si descubres una vulnerabilidad de seguridad, te agradecemos que la reportes de manera responsable.

**Por favor, NO abras un issue público en el repositorio de GitHub para reportar una vulnerabilidad de seguridad.** Esto podría exponer la vulnerabilidad a actores maliciosos antes de que podamos solucionarla.

En su lugar, envía un correo electrónico a: {contact_email}

Por favor, incluye la siguiente información en tu reporte:

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad (si es posible).
*   Versión de {project_name} afectada.
*   Posible impacto de la vulnerabilidad.
*   Sugerencias para la mitigación (opcional).

Nos comprometemos a responder a tu reporte en un plazo de [Número de días/horas] días/horas para confirmar la recepción y proporcionar una estimación del tiempo necesario para investigar y solucionar la vulnerabilidad.

Seguimos un proceso de divulgación responsable. Una vez que la vulnerabilidad haya sido solucionada y se haya publicado una nueva versión, publicaremos un aviso de seguridad que reconozca tu contribución (a menos que prefieras permanecer en el anonimato).

## Prácticas de Seguridad

### Gestión de Dependencias

Asegurar la seguridad de las dependencias es crucial para la seguridad general de {project_name}.

*   **Verificación de Dependencias:** Utiliza herramientas de auditoría de dependencias para identificar vulnerabilidades conocidas en tus dependencias.
    *   Para proyectos Python, usa `pip-audit`: `pip-audit`
    *   Para proyectos Node.js, usa `npm audit`: `npm audit`
    *   Para proyectos Ruby, usa `bundler-audit`: `bundle audit`
*   **Mantener Actualizado:** Actualiza regularmente tus dependencias a las últimas versiones para incorporar parches de seguridad.
    *   Python: `pip install --upgrade -r requirements.txt`
    *   Node.js: `npm update`
    *   Ruby: `bundle update`
*   **Alertas de Vulnerabilidades:** Configura alertas de vulnerabilidades en tus repositorios de GitHub o utiliza servicios de monitoreo de dependencias para recibir notificaciones sobre nuevas vulnerabilidades en tus dependencias.

### Manejo de Secretos

Manejar los secretos de forma segura es fundamental para evitar la exposición de información sensible.

*   **NUNCA Hardcodear Secrets:** Nunca incluyas contraseñas, claves API, tokens u otra información sensible directamente en el código fuente.
    *   **Inseguro:** `api_key = "YOUR_API_KEY"`
    *   **Seguro:** `api_key = os.environ.get("API_KEY")`
*   **Usar Variables de Entorno:** Almacenar secretos como variables de entorno es una práctica segura.
    *   Python: `os.environ.get("API_KEY")`
    *   Node.js: `process.env.API_KEY`
*   **.env en .gitignore:** Incluye el archivo `.env` en el archivo `.gitignore` para evitar que se suban accidentalmente secretos al repositorio.
*   **Herramientas para Detectar Leaks:** Utiliza herramientas como `git-secrets` o `trufflehog` para escanear el historial del repositorio en busca de secretos expuestos.

### Validación de Entrada

Validar la entrada del usuario es esencial para prevenir ataques de inyección y otros tipos de vulnerabilidades.

*   **Validar Entrada de Usuario:** Siempre valida y sanitiza la entrada del usuario antes de usarla en tu aplicación.
    *   **Inseguro:** `subprocess.call("rm -rf " + user_input, shell=True)`  (Vulnerable a inyección de comandos)
    *   **Seguro:** `subprocess.call(["rm", "-rf", user_input])` (Evita la shell y la inyección)
*   **Ejemplos de Código Seguro/Inseguro:**
    *   **Inyección SQL:** Evita concatenar cadenas para construir consultas SQL. Utiliza consultas parametrizadas u ORMs.
        *   **Inseguro:** `query = "SELECT * FROM users WHERE username = '" + username + "'"`
        *   **Seguro:** `query = "SELECT * FROM users WHERE username = %s"; cursor.execute(query, (username,))`
*   **Prevenir Inyección:** Utiliza técnicas de escaping y quoting para prevenir ataques de inyección.

### Gestión de Acceso

Controlar el acceso a los recursos es fundamental para proteger la información sensible.

*   **Principio de Mínimo Privilegio:** Otorga a los usuarios y procesos solo los permisos mínimos necesarios para realizar sus tareas.
*   **SSH Keys vs HTTPS:** Utiliza claves SSH para autenticarte en servidores en lugar de contraseñas. Utiliza HTTPS para cifrar la comunicación entre el cliente y el servidor.
*   **Permisos de Archivos:** Configura los permisos de archivos y directorios de forma adecuada para evitar el acceso no autorizado.  Utiliza `chmod` y `chown` para gestionar los permisos.

## Seguridad en CI/CD

Asegurar la seguridad en el proceso de Integración Continua y Entrega Continua (CI/CD) es crucial para evitar la introducción de vulnerabilidades en el código.

*   **Secrets en Jenkins/GitHub Actions:** Almacena secretos como claves API y contraseñas de forma segura en las herramientas de CI/CD. Utiliza las funcionalidades de gestión de secretos provistas por Jenkins, GitHub Actions u otras plataformas.
*   **Cómo usar credentials:** Utiliza las credenciales almacenadas en las herramientas de CI/CD en lugar de hardcodearlas en los scripts.
    *   **Ejemplo (GitHub Actions):**
        ```yaml
        steps:
          - name: Deploy
            run: |
              sshpass -e ssh -o StrictHostKeyChecking=no user@host "deploy.sh"
            env:
              SSH_PASSWORD: ${{ secrets.SSH_PASSWORD }}
        ```
*   **No loguear información sensible:** Evita loguear información sensible como contraseñas o claves API en los logs de CI/CD.
*   **Ejemplos:** Asegúrate de que los scripts de CI/CD no impriman variables de entorno que contengan secretos.

## Testing de Seguridad

Realizar pruebas de seguridad de forma regular es esencial para identificar y solucionar vulnerabilidades.

*   **Herramientas:** Utiliza herramientas de análisis estático de código (SAST) y análisis dinámico de código (DAST) para identificar vulnerabilidades.
    *   **Python:** `bandit`, `safety`, `pip-audit`
    *   **JavaScript:** `eslint`, `snyk`
*   **Cómo ejecutar:** Ejecuta las herramientas de testing de seguridad de forma regular como parte del proceso de CI/CD.
    *   **Ejemplo (Bandit):** `bandit -r ./`
*   **Qué buscar:** Busca vulnerabilidades comunes como inyección SQL, cross-site scripting (XSS) y vulnerabilidades de dependencias.
*   **Análisis SAST:** Incorpora análisis estático de código (SAST) en tu flujo de trabajo para detectar problemas de seguridad en las primeras etapas del desarrollo.

## Checklist de Seguridad para Contribuidores

Como contribuidor a {project_name}, es importante seguir estas pautas para mantener la seguridad del proyecto:

*   **No incluir secrets:** No incluyas contraseñas, claves API u otra información sensible en tu código.
*   **No usar shell=True:** Evita usar `shell=True` en la función `subprocess.call` ya que puede ser vulnerable a inyección de comandos.
*   **Validar inputs:** Valida y sanitiza la entrada del usuario para prevenir ataques de inyección.
*   **Sin hardcoded passwords:** No incluyas contraseñas hardcodeadas en el código.
*   **Revisar cambios:** Revisa cuidadosamente los cambios de código antes de enviarlos para asegurarte de que no introduzcan nuevas vulnerabilidades.

## Vulnerabilidades Conocidas

Esta sección enumera las vulnerabilidades conocidas en {project_name} y sus mitigaciones.

| Vulnerabilidad | CVE | Versiones Afectadas | Solución |
|---|---|---|---|
| [Descripción de la Vulnerabilidad] | [CVE ID (si aplica)] | [Versiones afectadas] | Actualizar a la versión [Versión] o superior |
| Ejemplo: Vulnerabilidad XSS en el módulo Y | CVE-2023-XXXX | 1.0.0 - 1.2.0 | Actualizar a la versión 1.2.1 o superior |

**Recomendación:** Mantén {project_name} actualizado a la última versión para asegurarte de tener las últimas correcciones de seguridad.

## Recursos de Seguridad

*   [OWASP Top 10](https://owasp.org/top10/): Lista de las 10 vulnerabilidades web más críticas.
*   [Python Security Best Practices](https://wiki.python.org/moin/Security): Guía de buenas prácticas de seguridad para Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Lista de los 25 errores de software más peligrosos.

## Soporte

Si tienes alguna pregunta o inquietud sobre la seguridad de {project_name}, no dudes en contactarnos.

*   **Cómo reportar:** Envía un correo electrónico a {contact_email} para reportar una vulnerabilidad de seguridad.
*   **Email de seguridad:** {contact_email}
*   **Contacto directo:** Puedes contactarnos directamente a través de [Otro método de contacto, si aplica].
```