```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Este documento describe nuestras prácticas de seguridad y cómo reportar vulnerabilidades de manera responsable.  Ayuda a usuarios y colaboradores a entender las consideraciones de seguridad del proyecto.

## Reportar Vulnerabilidades de Seguridad

Creemos que la seguridad de nuestra comunidad y nuestros usuarios es primordial, y valoramos enormemente el papel que los investigadores de seguridad juegan al ayudarnos a mantener {project_name} seguro. Si descubres una vulnerabilidad de seguridad, te pedimos que la reportes de manera responsable.

**Por favor, NO abras un issue público en GitHub** con detalles de la vulnerabilidad.  Esto podría exponer a otros usuarios antes de que tengamos la oportunidad de solucionarlo.

En su lugar, envía un correo electrónico a {contact_email} con los detalles de la vulnerabilidad.

**Incluye la siguiente información en tu reporte:**

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad.
*   Versiones de {project_name} afectadas.
*   Posible impacto de la vulnerabilidad.
*   Cualquier información adicional que pueda ayudarnos a comprender y solucionar la vulnerabilidad.

**Timeline de Respuesta Esperado:**

Nos comprometemos a acusar recibo de tu reporte dentro de las 72 horas.  Trabajaremos para validar la vulnerabilidad y desarrollar una solución lo más rápido posible.  Te mantendremos informado del progreso de la solución.

**Proceso de Divulgación Responsable:**

Una vez que hayamos solucionado la vulnerabilidad, te daremos crédito por tu descubrimiento (a menos que prefieras permanecer anónimo).  Trabajaremos contigo para divulgar la vulnerabilidad de manera responsable, coordinando la divulgación para minimizar el riesgo para nuestros usuarios. Generalmente, esto implica publicar detalles de la vulnerabilidad y su solución una vez que haya una versión parcheada disponible.

## Prácticas de Seguridad

Implementamos las siguientes prácticas de seguridad para proteger {project_name} y a nuestros usuarios:

### 3.1 Gestión de Dependencias

Es crucial gestionar las dependencias de manera segura para evitar la introducción de vulnerabilidades conocidas.

*   **Verificación de Dependencias:**  Utiliza herramientas como `pip-audit` (para Python) o `npm audit` (para Node.js) para verificar si tus dependencias tienen vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip-audit
    pip-audit

    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantener Actualizado:**  Mantén tus dependencias actualizadas a las últimas versiones para corregir vulnerabilidades conocidas y obtener las últimas mejoras de seguridad.

    ```bash
    # Ejemplo con pip
    pip install --upgrade -r requirements.txt

    # Ejemplo con npm
    npm update
    ```

*   **Alertas de Vulnerabilidades:** Configura alertas para recibir notificaciones cuando se detecten vulnerabilidades en tus dependencias.  GitHub ofrece alertas de Dependabot para ayudarte a mantener tus dependencias seguras.

### 3.2 Manejo de Secretos

El manejo adecuado de secretos es fundamental para prevenir la exposición de información sensible.

*   **No Hardcodear Secretos:** NUNCA incluyas contraseñas, claves API u otra información sensible directamente en el código fuente.

*   **Variables de Entorno:** Utiliza variables de entorno para almacenar secretos.  Esto permite configurar el entorno de ejecución sin modificar el código fuente.

    ```python
    # Ejemplo (Python)
    import os

    api_key = os.environ.get("API_KEY")
    if api_key:
        # Usar la clave API
        print("Clave API:", api_key)
    else:
        print("Error: La clave API no está definida.")
    ```

*   **.env en .gitignore:** Si utilizas archivos `.env` para almacenar variables de entorno durante el desarrollo, asegúrate de añadirlos a tu archivo `.gitignore` para evitar que se suban al repositorio.

*   **Herramientas para Detectar Leaks:** Utiliza herramientas como `git-secrets` o `truffleHog` para buscar secretos accidentalmente subidos al repositorio.

### 3.3 Validación de Entrada

La validación de entrada es esencial para prevenir ataques de inyección y otros problemas de seguridad.

*   **Validar Entrada de Usuario:**  SIEMPRE valida la entrada de usuario antes de utilizarla en cualquier operación.  Esto incluye verificar el tipo de datos, el formato y el rango de valores.

*   **Ejemplos de Código Seguro/Inseguro:**

    **Inseguro (SQL Injection):**

    ```python
    # INSEGURO: vulnerable a SQL injection
    username = request.form['username']
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    ```

    **Seguro (Prepared Statements):**

    ```python
    # SEGURO: utiliza prepared statements para prevenir SQL injection
    username = request.form['username']
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    ```

*   **Prevenir Inyección:** Utiliza mecanismos de protección contra ataques de inyección, como prepared statements (para SQL), escaping (para HTML) y sanitización (para otros tipos de entrada).

### 3.4 Gestión de Acceso

La gestión de acceso adecuada es crucial para limitar el daño potencial en caso de una brecha de seguridad.

*   **Principio de Mínimo Privilegio:**  Otorga a los usuarios y procesos solo los permisos necesarios para realizar sus tareas.

*   **SSH Keys vs HTTPS:** Utiliza claves SSH para acceso a servidores en lugar de contraseñas siempre que sea posible. Fuerza el uso de HTTPS para todas las comunicaciones web.

*   **Permisos de Archivos:** Configura permisos de archivos y directorios para limitar el acceso a usuarios no autorizados.  Utiliza `chmod` y `chown` para establecer los permisos adecuados.

## Seguridad en CI/CD

La seguridad en el pipeline de CI/CD es fundamental para evitar la introducción de vulnerabilidades en la producción.

*   **Secrets en Jenkins/GitHub Actions:** Almacena secretos (como claves API, contraseñas de bases de datos, etc.) de forma segura en tu sistema de CI/CD (por ejemplo, utilizando las "Secrets" de GitHub Actions o el plugin "Credentials" de Jenkins).

*   **Cómo Usar Credentials:** Utiliza las credenciales almacenadas en tu sistema de CI/CD en lugar de hardcodearlas en tus scripts de construcción.

    ```yaml
    # Ejemplo (GitHub Actions)
    steps:
      - name: Deploy to production
        uses: some-action
        with:
          api_key: ${{ secrets.API_KEY }}
    ```

*   **No Loguear Información Sensible:** Evita loguear información sensible (como contraseñas o claves API) en los registros de tu sistema de CI/CD.

## Testing de Seguridad

Realizar pruebas de seguridad es crucial para identificar y corregir vulnerabilidades antes de que sean explotadas.

*   **Herramientas:** Utiliza herramientas de análisis estático de código (SAST) como `bandit` (para Python) o `eslint` (para JavaScript) para detectar posibles vulnerabilidades en tu código.  Utiliza herramientas de auditoría de dependencias como `safety` o `pip-audit` (para Python) para verificar si tus dependencias tienen vulnerabilidades conocidas.

*   **Cómo Ejecutar:**

    ```bash
    # Ejemplo con bandit
    bandit -r .

    # Ejemplo con safety
    safety check
    ```

*   **Qué Buscar:** Busca vulnerabilidades comunes como SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), y problemas de autenticación y autorización.

*   **Análisis SAST:** Incorpora el análisis SAST en tu pipeline de CI/CD para detectar vulnerabilidades automáticamente en cada commit.

## Checklist de Seguridad para Contribuidores

Los contribuidores deben seguir las siguientes pautas de seguridad:

*   No incluir secretos (contraseñas, claves API, etc.) en el código.
*   Evitar usar `shell=True` en llamadas a `subprocess` (en Python) a menos que sea absolutamente necesario y la entrada esté completamente controlada.
*   Validar todas las entradas de usuario.
*   No usar contraseñas hardcodeadas.
*   Revisar cuidadosamente los cambios antes de enviarlos para asegurarte de que no introducen nuevas vulnerabilidades.

## Vulnerabilidades Conocidas

*   **CVE-2023-1234:** Vulnerabilidad de XSS en versiones anteriores a 1.2.0.  Solucionado en la versión 1.2.0.  Se recomienda actualizar a la última versión.
*   **CVE-2023-5678:** Vulnerabilidad de SQL injection en el módulo de autenticación en versiones anteriores a 1.2.1. Solucionado en la versión 1.2.1. Se recomienda actualizar a la última versión.

## Recursos de Seguridad

*   OWASP Top 10: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
*   Python Security Best Practices: [https://wiki.python.org/moin/WebProgrammingSecurity](https://wiki.python.org/moin/WebProgrammingSecurity)
*   CWE/SANS Top 25: [https://cwe.mitre.org/top25/](https://cwe.mitre.org/top25/)

## Soporte

Si tienes alguna pregunta o inquietud sobre la seguridad de {project_name}, por favor contáctanos:

*   Reportar vulnerabilidades: {contact_email}
*   Contacto directo: Puedes contactarnos a través del repositorio en {repository_url} creando un issue (para preguntas generales, NO para reportar vulnerabilidades).
```