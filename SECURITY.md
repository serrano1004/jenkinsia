```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Este documento describe nuestras prácticas de seguridad y cómo reportar vulnerabilidades de forma responsable.  Ayuda a mantener el proyecto seguro tanto para usuarios como para desarrolladores.

Este documento cubre:

*   Cómo reportar vulnerabilidades de seguridad.
*   Las prácticas de seguridad que seguimos en el desarrollo de {project_name}.
*   Vulnerabilidades conocidas y sus mitigaciones.
*   Consideraciones de seguridad para contribuidores.

## Reportar Vulnerabilidades de Seguridad

Creemos que la divulgación responsable de vulnerabilidades es crucial para mantener la seguridad de {project_name}. Si descubre una vulnerabilidad de seguridad, **NO cree un issue público en el repositorio**. En su lugar, envíe un correo electrónico detallado a:

{contact_email}

Por favor, incluya la siguiente información en su reporte:

*   Una descripción detallada de la vulnerabilidad, incluyendo cómo se puede explotar.
*   Los pasos para reproducir la vulnerabilidad.
*   La versión de {project_name} afectada.
*   Cualquier información adicional que pueda ser útil para entender y solucionar la vulnerabilidad.

**Timeline de Respuesta Esperado:**

*   Recibirá una confirmación de recepción de su reporte en un plazo de 24-48 horas.
*   Investigaremos la vulnerabilidad y le proporcionaremos una evaluación inicial en un plazo de 72 horas.
*   Trabajaremos para solucionar la vulnerabilidad lo más rápido posible y le mantendremos informado sobre el progreso.

**Proceso de Divulgación Responsable:**

Una vez que hayamos solucionado la vulnerabilidad, trabajaremos con usted para coordinar la divulgación pública de la vulnerabilidad.  Esto incluye la creación de un anuncio de seguridad y la publicación de un parche.  Preferimos divulgar las vulnerabilidades de manera responsable, dando tiempo a los usuarios para que actualicen antes de que la información detallada esté disponible públicamente.

## Prácticas de Seguridad

En {project_name}, nos esforzamos por seguir las mejores prácticas de seguridad en todas las etapas del desarrollo.

### 3.1 Gestión de Dependencias

Las dependencias de terceros pueden introducir vulnerabilidades en nuestro proyecto. Por lo tanto, es crucial gestionarlas de forma efectiva.

*   **Verificación de Dependencias:** Utilizamos herramientas como `pip-audit` (para Python) y `npm audit` (para Node.js) para verificar nuestras dependencias en busca de vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

    ```bash
    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantener Actualizado:** Mantenemos nuestras dependencias actualizadas a las últimas versiones para corregir vulnerabilidades y obtener mejoras de seguridad.

    ```bash
    # Ejemplo con pip
    pip install --upgrade -r requirements.txt
    ```

    ```bash
    # Ejemplo con npm
    npm update
    ```

*   **Alertas de Vulnerabilidades:** Configuramos alertas de vulnerabilidades en plataformas como GitHub para recibir notificaciones sobre nuevas vulnerabilidades en nuestras dependencias.  Esto nos permite reaccionar rápidamente ante problemas de seguridad.

### 3.2 Manejo de Secretos

El manejo seguro de secretos es fundamental para proteger la integridad de {project_name}.

*   **NUNCA Hardcodear Secrets:** Nunca incluya contraseñas, claves API u otra información sensible directamente en el código.
*   **Usar Variables de Entorno:** Almacene los secretos como variables de entorno y acceda a ellos a través del código.

    ```python
    # Ejemplo en Python
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **.env en .gitignore:** Asegúrese de que el archivo `.env` (si lo utiliza para almacenar variables de entorno localmente) esté incluido en el archivo `.gitignore` para evitar que se suba al repositorio.
*   **Herramientas para detectar leaks:** Utilize herramientas como `git-secrets` o `trufflehog` para escanear el historial del repositorio en busca de secretos accidentalmente commiteados.

### 3.3 Validación de Entrada

La validación de entrada es esencial para prevenir ataques de inyección y otros problemas de seguridad.

*   **Validar Entrada de Usuario:** Siempre valide y sanitize la entrada del usuario antes de usarla en su código.  Esto incluye verificar el tipo de datos, la longitud y el formato de la entrada.

*   **Ejemplos de código seguro/inseguro:**

    **Inseguro (Python):**

    ```python
    import os
    filename = input("Ingrese el nombre del archivo: ")
    os.system("cat " + filename) # Vulnerable a inyección de comandos
    ```

    **Seguro (Python):**

    ```python
    import os
    import shlex

    filename = input("Ingrese el nombre del archivo: ")
    filename = shlex.quote(filename) # Escapa caracteres especiales
    os.system("cat " + filename)
    ```

    Aunque el ejemplo "seguro" mitiga la inyección de comandos, es preferible usar funciones que no invoquen a la shell directamente, como `subprocess.run`.

*   **Prevenir Inyección:** Utilice técnicas de escape y parametrización para prevenir ataques de inyección SQL, inyección de comandos y otros tipos de inyección.

### 3.4 Gestión de Acceso

Restringir el acceso a los recursos es crucial para proteger la confidencialidad e integridad de los datos.

*   **Principio de mínimo privilegio:** Otorgue a los usuarios y procesos solo los permisos mínimos necesarios para realizar sus tareas.
*   **SSH keys vs HTTPS:** Utilice claves SSH en lugar de contraseñas para la autenticación SSH.  Utilice HTTPS para todas las comunicaciones web.
*   **Permisos de archivos:** Configure los permisos de archivo adecuados para proteger los archivos y directorios sensibles.  Por ejemplo, asegúrese de que los archivos de configuración solo sean legibles por el usuario que los necesita.

## Seguridad en CI/CD

La integración continua y la entrega continua (CI/CD) son partes importantes del proceso de desarrollo. Es importante asegurar que el pipeline de CI/CD no introduzca vulnerabilidades.

*   **Secrets en Jenkins/GitHub Actions:** Almacene los secretos utilizados en los pipelines de CI/CD (por ejemplo, claves API, contraseñas) de forma segura utilizando las funciones de gestión de secretos proporcionadas por Jenkins, GitHub Actions u otras herramientas de CI/CD.
*   **Cómo usar credentials:** Use las credenciales almacenadas en lugar de hardcodearlas en los scripts de CI/CD.
*   **No loguear información sensible:** Evite loguear información sensible en los logs de CI/CD.  Esto incluye contraseñas, claves API y otra información que pueda ser utilizada para comprometer el sistema.
*   **Ejemplos:**

    **GitHub Actions:**

    ```yaml
    steps:
      - name: Deploy to production
        uses: some-action@v1
        with:
          api_key: ${{ secrets.PRODUCTION_API_KEY }}
    ```

## Testing de Seguridad

El testing de seguridad es una parte importante del ciclo de vida del desarrollo de software.

*   **Herramientas:** Utilizamos herramientas como `bandit` (para Python), `safety` (para Python) y `pip-audit` (para Python) para realizar pruebas de seguridad automatizadas.
*   **Cómo ejecutar:**

    ```bash
    # Ejemplo con bandit
    bandit -r ./
    ```

    ```bash
    # Ejemplo con safety
    safety check
    ```
    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

*   **Qué buscar:** Buscamos vulnerabilidades comunes como inyección SQL, cross-site scripting (XSS), y vulnerabilidades de dependencias.
*   **Análisis SAST:** Realizamos análisis estático de código fuente (SAST) para identificar vulnerabilidades en el código antes de que se despliegue.

## Checklist de Seguridad para Contribuidores

Para garantizar la seguridad de {project_name}, solicitamos a todos los contribuidores que sigan las siguientes pautas:

*   **No incluir secrets:** No incluya contraseñas, claves API u otra información sensible en su código.
*   **No usar shell=True:** Evite usar `shell=True` en las funciones `subprocess` de Python, ya que puede introducir vulnerabilidades de inyección de comandos.
*   **Validar inputs:** Valide y sanitize la entrada del usuario antes de usarla en su código.
*   **Sin hardcoded passwords:** No incluya contraseñas hardcodeadas en el código.
*   **Revisar cambios:** Revise cuidadosamente todos los cambios antes de commitearlos para asegurarse de que no introducen vulnerabilidades de seguridad.

## Vulnerabilidades Conocidas

Esta sección enumera las vulnerabilidades conocidas en {project_name} y sus mitigaciones.

*   **CVE-2023-XXXX:** Vulnerabilidad de Cross-Site Scripting (XSS) en la versión 1.0.0.  Actualice a la versión 1.0.1 o posterior para solucionar esta vulnerabilidad.
*   **CVE-2023-YYYY:** Vulnerabilidad de inyección SQL en la versión 1.1.0.  Esta vulnerabilidad se soluciona en la versión 1.1.1.  Actualice a la versión 1.1.1 o posterior.

## Recursos de Seguridad

Los siguientes recursos proporcionan información valiosa sobre las mejores prácticas de seguridad:

*   [OWASP Top 10](https://owasp.org/www-project-top-ten/): Una lista de las vulnerabilidades de seguridad web más comunes.
*   [Python Security Best Practices](https://wiki.python.org/moin/Security): Una guía sobre las mejores prácticas de seguridad para el desarrollo de Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Una lista de los errores de software más peligrosos y generalizados.

## Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en contactarnos.

*   **Cómo reportar:** Envíe un correo electrónico a: {contact_email}.
*   **Email de seguridad:** {contact_email}
*   **Contacto directo:** Puede contactar directamente con los responsables de seguridad a través de {contact_email}.
```