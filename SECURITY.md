```markdown
# SECURITY.md

La seguridad es de suma importancia para el proyecto {project_name}. Nos tomamos en serio la protección de nuestros usuarios y sus datos.

Este documento describe nuestra política de seguridad, cómo reportar vulnerabilidades y las prácticas de seguridad que implementamos.

## Reportar Vulnerabilidades de Seguridad

Creemos que la divulgación responsable de vulnerabilidades es crucial para mantener la seguridad de {project_name}. Si descubre una vulnerabilidad de seguridad, le agradecemos que nos la informe de manera responsable.

**Por favor, NO cree un issue público en el repositorio de GitHub.** Esto podría alertar a atacantes potenciales antes de que tengamos la oportunidad de solucionar el problema.

En su lugar, envíe un correo electrónico a: {contact_email}

Por favor, incluya la siguiente información en su reporte:

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad.
*   Versiones de {project_name} afectadas.
*   Posibles impactos de la vulnerabilidad.
*   Sugerencias para la mitigación (si las tiene).

Nos comprometemos a responder a su reporte en un plazo de **72 horas**. Trabajaremos con usted para comprender el problema y desarrollar una solución.

Una vez que la vulnerabilidad se haya solucionado, coordinaremos una divulgación pública responsable. Esto podría incluir la publicación de un aviso de seguridad y la atribución a su descubrimiento (si lo desea).

## Prácticas de Seguridad

Implementamos las siguientes prácticas de seguridad para proteger {project_name}:

### 3.1 Gestión de Dependencias

Es crucial mantener nuestras dependencias actualizadas y libres de vulnerabilidades conocidas.

*   **Verificación de Dependencias:** Utilizamos herramientas como `pip-audit` (para Python) y `npm audit` (para JavaScript) para escanear nuestras dependencias en busca de vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

    ```bash
    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantenimiento Actualizado:** Regularmente actualizamos nuestras dependencias a las últimas versiones para aplicar parches de seguridad.

    ```bash
    # Ejemplo con pip
    pip install --upgrade -r requirements.txt
    ```

    ```bash
    # Ejemplo con npm
    npm update
    ```

*   **Alertas de Vulnerabilidades:**  Configuramos alertas de vulnerabilidades en GitHub para ser notificados cuando se detectan vulnerabilidades en nuestras dependencias.

### 3.2 Manejo de Secretos

El manejo adecuado de secretos es esencial para evitar la exposición de información sensible.

*   **No Hardcodear Secretos:** NUNCA incluya secretos (contraseñas, claves API, etc.) directamente en el código fuente.

    **Ejemplo INSEGURO:**

    ```python
    api_key = "ESTA_ES_UNA_CLAVE_SECRETA"  # ¡NUNCA HAGAS ESTO!
    ```

*   **Variables de Entorno:** Utilice variables de entorno para almacenar secretos de forma segura.

    **Ejemplo SEGURO:**

    ```python
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **.env en .gitignore:** Incluya el archivo `.env` (donde se almacenan las variables de entorno en desarrollo) en el archivo `.gitignore` para evitar que se suba al repositorio.

*   **Herramientas de Detección de Leaks:** Utilizamos herramientas como `git-secrets` o `trufflehog` para escanear el historial del repositorio en busca de secretos accidentalmente comprometidos.

### 3.3 Validación de Entrada

La validación de la entrada del usuario es fundamental para prevenir ataques de inyección.

*   **Validar Entrada:** SIEMPRE valide la entrada del usuario antes de procesarla.

    **Ejemplo INSEGURO (sin validación):**

    ```python
    import os
    usuario = input("Ingrese su nombre: ")
    os.system("echo Hola " + usuario) # Vulnerable a inyección de comandos
    ```

    **Ejemplo SEGURO (con validación):**

    ```python
    import shlex
    import subprocess

    def sanitize_input(input_str):
        """Sanitiza la entrada para prevenir inyección de comandos."""
        return shlex.quote(input_str)

    usuario = input("Ingrese su nombre: ")
    sanitized_usuario = sanitize_input(usuario)
    subprocess.run(["echo", f"Hola {sanitized_usuario}"])
    ```

*   **Prevenir Inyección:** Utilice funciones y bibliotecas seguras para interactuar con el sistema operativo y las bases de datos.  Evite la concatenación directa de cadenas para construir comandos SQL o del sistema operativo. Utilice sentencias preparadas o funciones de escape proporcionadas por las bibliotecas de base de datos.

### 3.4 Gestión de Acceso

Controlar el acceso a los recursos es clave para la seguridad.

*   **Principio de Mínimo Privilegio:** Otorgue a los usuarios y procesos solo los privilegios necesarios para realizar sus tareas.

*   **SSH Keys vs HTTPS:**  Prefiera el uso de claves SSH para la autenticación en lugar de contraseñas, especialmente para acceso a servidores. Utilice HTTPS para todas las comunicaciones web para proteger los datos en tránsito.

*   **Permisos de Archivos:** Configure los permisos de archivos y directorios de manera que solo los usuarios autorizados tengan acceso.  Utilice `chmod` para modificar los permisos.

## 4. Seguridad en CI/CD

La seguridad debe integrarse en el proceso de CI/CD (Integración Continua/Entrega Continua).

*   **Secrets en Jenkins/GitHub Actions:** Almacenar los secretos necesarios para el despliegue (claves API, contraseñas de bases de datos, etc.) de forma segura en el sistema de CI/CD.  Utilice las funcionalidades de gestión de secretos proporcionadas por Jenkins, GitHub Actions u otras herramientas de CI/CD.

*   **Cómo Usar Credentials:**  Referencie los secretos utilizando variables de entorno o nombres de credenciales definidos en el sistema de CI/CD.  Evite hardcodear los secretos directamente en los scripts de despliegue.

    **Ejemplo en GitHub Actions:**

    ```yaml
    steps:
      - name: Deploy
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          # Usa $API_KEY en el script de despliegue
          echo "Deploying with API key: $API_KEY"
    ```

*   **No Loguear Información Sensible:**  Evite loguear información sensible (secretos, contraseñas, datos personales) en los logs del sistema de CI/CD.  Configure el sistema de logging para filtrar o enmascarar la información sensible.

## 5. Testing de Seguridad

El testing de seguridad debe ser parte integral del ciclo de desarrollo.

*   **Herramientas:** Utilizamos herramientas como `bandit` (para Python), `safety` (para Python) y `pip-audit` (para Python) para analizar el código en busca de vulnerabilidades.

    ```bash
    # Ejemplo con bandit
    bandit -r .
    ```

    ```bash
    # Ejemplo con safety
    safety check
    ```

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

*   **Cómo Ejecutar:** Integre estas herramientas en el proceso de CI/CD para que se ejecuten automáticamente en cada cambio de código.

*   **Qué Buscar:**  Busque vulnerabilidades comunes como inyección de SQL, cross-site scripting (XSS), cross-site request forgery (CSRF), y problemas de autenticación y autorización.

*   **Análisis SAST (Static Application Security Testing):**  Realizamos análisis SAST para identificar vulnerabilidades en el código fuente antes de que se despliegue la aplicación.

## 6. Checklist de Seguridad para Contribuidores

Para garantizar la seguridad de {project_name}, pedimos a todos los contribuyentes que sigan estas pautas:

*   **No Incluir Secretos:** NUNCA incluya secretos (contraseñas, claves API) en el código que contribuya.
*   **No Usar `shell=True`:** Evite usar `shell=True` en las funciones `subprocess.run` o similares.  Esto puede abrir puertas a ataques de inyección de comandos.
*   **Validar Inputs:** Valide todos los inputs del usuario para prevenir inyección y otros ataques.
*   **Sin Hardcoded Passwords:** No incluya contraseñas hardcodeadas en el código.
*   **Revisar Cambios:** Revise cuidadosamente todos los cambios antes de enviarlos para detectar posibles problemas de seguridad.

## 7. Vulnerabilidades Conocidas

Esta sección lista las vulnerabilidades conocidas y ya parcheadas en {project_name}.

*   **CVE-2023-XXXX:** Vulnerabilidad de Cross-Site Scripting (XSS) en la función de búsqueda.  Afecta a las versiones anteriores a la 1.2.3.  Solucionado al escapar la entrada del usuario.  Recomendamos actualizar a la versión 1.2.3 o superior.
*   **CVE-2023-YYYY:** Vulnerabilidad de Inyección SQL en el módulo de autenticación.  Afecta a las versiones anteriores a la 1.2.5.  Solucionado mediante el uso de sentencias preparadas.  Recomendamos actualizar a la versión 1.2.5 o superior.

## 8. Recursos de Seguridad

Estos recursos pueden ser útiles para comprender mejor los problemas de seguridad:

*   [OWASP Top 10](https://owasp.org/www-project-top-ten/): Lista de las 10 vulnerabilidades web más críticas.
*   [Python Security Best Practices](https://wiki.python.org/moin/WebProgramming): Guía de buenas prácticas de seguridad para Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Lista de los 25 errores de software más peligrosos.

## 9. Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en ponerse en contacto con nosotros.

*   **Cómo Reportar:** Envíe un correo electrónico a {contact_email}.
*   **Email de Seguridad:** {contact_email}
*   **Contacto Directo:** Si necesita contactarnos directamente, puede hacerlo a través del repositorio de GitHub en {repository_url}, pero recuerde NO publicar información sensible en los issues públicos. En su lugar, cree un issue mencionando que necesita discutir un problema de seguridad en privado.
```