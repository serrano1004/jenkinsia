```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Este documento describe cómo reportar vulnerabilidades de seguridad de manera responsable, las prácticas de seguridad recomendadas para el proyecto, las vulnerabilidades conocidas y sus mitigaciones, las características de seguridad implementadas, y las limitaciones de seguridad.

Este documento está dirigido a usuarios, desarrolladores y contribuidores de {project_name} que deseen comprender y mejorar la postura de seguridad del proyecto.

## Reportar Vulnerabilidades de Seguridad

Creemos que la seguridad de nuestra comunidad es primordial y agradecemos a aquellos que identifiquen y nos reporten vulnerabilidades de seguridad de manera responsable.

**Por favor, NO cree un issue público en el repositorio de GitHub para reportar una vulnerabilidad de seguridad.** Los issues públicos son visibles para todos, incluyendo posibles atacantes, y podrían exponer información sensible sobre la vulnerabilidad antes de que podamos corregirla.

En su lugar, envíe un correo electrónico a la siguiente dirección: {contact_email}

Al reportar una vulnerabilidad de seguridad, por favor incluya la siguiente información:

*   **Descripción detallada de la vulnerabilidad:** Explique la vulnerabilidad con la mayor claridad y precisión posible. Incluya los pasos necesarios para reproducirla (PoC - Proof of Concept) si es posible.
*   **Componente(s) afectado(s):** Indique qué parte(s) del proyecto se ven afectadas por la vulnerabilidad (por ejemplo, un módulo específico, una función, una API).
*   **Impacto potencial:** Describa el impacto potencial de la vulnerabilidad (por ejemplo, ejecución de código arbitrario, denegación de servicio, robo de información sensible).
*   **Versiones afectadas:** Especifique las versiones de {project_name} que se ven afectadas por la vulnerabilidad.
*   **Información de contacto:** Proporcione su nombre y dirección de correo electrónico para que podamos contactarlo si necesitamos más información.

**Timeline de respuesta esperado:**

Nos comprometemos a responder a su reporte de vulnerabilidad en un plazo de **72 horas** para confirmar la recepción y evaluar la gravedad de la vulnerabilidad.  Trabajaremos diligentemente para proporcionar una solución o mitigación en un plazo razonable, dependiendo de la complejidad de la vulnerabilidad.  Mantendremos una comunicación abierta y transparente durante todo el proceso.

**Proceso de Divulgación Responsable:**

Una vez que hayamos corregido la vulnerabilidad y lanzado una versión actualizada de {project_name}, le notificaremos y coordinaremos con usted la divulgación pública de la vulnerabilidad. Respetamos su derecho a ser reconocido por su contribución y estaremos encantados de incluir su nombre en el aviso de seguridad, a menos que prefiera permanecer anónimo.

## Prácticas de Seguridad

Las siguientes son las prácticas de seguridad recomendadas para el desarrollo y mantenimiento de {project_name}.

### 3.1 Gestión de Dependencias

Las dependencias son una parte integral de cualquier proyecto de software moderno. Es crucial asegurarse de que las dependencias que utilizamos sean seguras y estén actualizadas.

*   **Verificación de Dependencias:** Use herramientas como `pip-audit` (para Python) o `npm audit` (para Node.js) para verificar si sus dependencias tienen vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

    ```bash
    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantenimiento Actualizado:** Mantenga sus dependencias actualizadas a las últimas versiones para corregir vulnerabilidades y obtener mejoras de seguridad.

    ```bash
    # Ejemplo con pip (actualizar todas las dependencias)
    pip install --upgrade -r requirements.txt
    ```

    ```bash
    # Ejemplo con npm (actualizar una dependencia específica)
    npm update <paquete>
    ```

*   **Alertas de Vulnerabilidades:** Configure alertas de vulnerabilidades para sus dependencias utilizando herramientas como Dependabot (GitHub) o Snyk. Estas herramientas le notificarán automáticamente cuando se descubran nuevas vulnerabilidades en sus dependencias.

### 3.2 Manejo de Secretos

El manejo adecuado de secretos es crucial para la seguridad de cualquier aplicación.  Nunca debe almacenar secretos directamente en el código fuente.

*   **Nunca Hardcodear Secretos:** Evite almacenar contraseñas, claves API, tokens de acceso u otra información sensible directamente en el código fuente.

    **Inseguro:**

    ```python
    api_key = "ESTA_ES_UNA_CLAVE_SECRETA"
    ```

    **Seguro:**

    ```python
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **Variables de Entorno:** Use variables de entorno para almacenar información sensible fuera del código fuente.  Las variables de entorno son accesibles desde el código pero no están almacenadas directamente en el repositorio.

*   **.env y .gitignore:** Si utiliza un archivo `.env` para almacenar variables de entorno localmente, asegúrese de agregarlo a su archivo `.gitignore` para evitar que se suba al repositorio.

*   **Herramientas para Detectar Leaks:** Utilice herramientas como `git-secrets` o `trufflehog` para detectar si ha accidentalmente subido secretos a su repositorio.

### 3.3 Validación de Entrada

La validación de entrada es esencial para prevenir ataques de inyección y otros problemas de seguridad.

*   **Validar Entrada de Usuario:** Siempre valide y sanee la entrada del usuario antes de utilizarla en su aplicación.

    **Inseguro (vulnerable a inyección SQL):**

    ```python
    user_id = request.args.get('user_id')
    query = "SELECT * FROM users WHERE id = %s" % user_id
    cursor.execute(query)
    ```

    **Seguro (usando parámetros preparados):**

    ```python
    user_id = request.args.get('user_id')
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    ```

*   **Prevenir Inyección:** Utilice mecanismos de escape adecuados para prevenir ataques de inyección SQL, inyección de comandos y otros tipos de inyección.  Utilice bibliotecas y frameworks que proporcionen protección automática contra estos ataques.

### 3.4 Gestión de Acceso

La gestión adecuada de acceso es fundamental para proteger los recursos de su aplicación.

*   **Principio de Mínimo Privilegio:** Otorgue a los usuarios y procesos solo los privilegios mínimos necesarios para realizar sus tareas.  Evite otorgar permisos de administrador a menos que sea absolutamente necesario.

*   **SSH Keys vs HTTPS:** Use claves SSH en lugar de contraseñas para autenticarse en servidores.  Utilice HTTPS para cifrar la comunicación entre su aplicación y los usuarios.

*   **Permisos de Archivos:** Configure los permisos de archivos y directorios correctamente para evitar el acceso no autorizado.

## 4. Seguridad en CI/CD

La integración continua y la entrega continua (CI/CD) son partes críticas del proceso de desarrollo de software. Es importante asegurar que su pipeline de CI/CD sea seguro.

*   **Secrets en Jenkins/GitHub Actions:** Almacene secretos (como claves API, contraseñas, tokens de acceso) de forma segura en su sistema de CI/CD (por ejemplo, Jenkins Credentials, GitHub Actions Secrets).

*   **Cómo Usar Credentials:** Utilice las credenciales almacenadas en su sistema de CI/CD en lugar de hardcodearlas en sus scripts de CI/CD.

    ```yaml
    # Ejemplo de GitHub Actions
    steps:
      - name: Autenticar con AWS
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
    ```

*   **No Loguear Información Sensible:** Evite loguear información sensible (como contraseñas, claves API, tokens de acceso) en los logs de su sistema de CI/CD.

## 5. Testing de Seguridad

El testing de seguridad es una parte esencial del proceso de desarrollo de software.  Es importante realizar pruebas de seguridad de forma regular para identificar y corregir vulnerabilidades.

*   **Herramientas:** Utilice herramientas como `bandit` (para Python), `safety` (para Python), y `pip-audit` (para Python) para realizar pruebas de seguridad en su código.

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

*   **Cómo Ejecutar:** Ejecute las herramientas de testing de seguridad de forma regular como parte de su pipeline de CI/CD.

*   **Qué Buscar:** Busque vulnerabilidades comunes como inyección SQL, cross-site scripting (XSS), y ejecución de código arbitrario.

*   **Análisis SAST:** Implemente análisis estático de seguridad de aplicaciones (SAST) en su pipeline de CI/CD para detectar vulnerabilidades en su código antes de que se despliegue.

## 6. Checklist de Seguridad para Contribuidores

Para garantizar que las contribuciones al proyecto sean seguras, los contribuidores deben seguir la siguiente checklist:

*   **No Incluir Secretos:** No incluya contraseñas, claves API, tokens de acceso u otra información sensible en su código.
*   **No Usar `shell=True`:** Evite usar `shell=True` en la función `subprocess.run` de Python, ya que puede ser vulnerable a ataques de inyección de comandos.
*   **Validar Inputs:** Valide y sanee la entrada del usuario antes de utilizarla en su código.
*   **Sin Hardcoded Passwords:** No incluya contraseñas hardcoded en su código.
*   **Revisar Cambios:** Revise cuidadosamente sus cambios antes de enviarlos para asegurarse de que no introducen nuevas vulnerabilidades.

## 7. Vulnerabilidades Conocidas

Esta sección lista las vulnerabilidades conocidas en {project_name} que ya han sido parcheadas.

*   **CVE-2023-XXXX:** Vulnerabilidad de Cross-Site Scripting (XSS) en el módulo X. Afecta a las versiones anteriores a la 1.2.3.  Actualice a la versión 1.2.3 o posterior para mitigar esta vulnerabilidad.
*   **CVE-2023-YYYY:** Vulnerabilidad de Inyección SQL en el módulo Y. Afecta a las versiones anteriores a la 2.0.1.  Actualice a la versión 2.0.1 o posterior para mitigar esta vulnerabilidad.

## 8. Recursos de Seguridad

Los siguientes recursos pueden ser útiles para comprender y mejorar la seguridad de {project_name}:

*   **OWASP Top 10:** [https://owasp.org/top10/](https://owasp.org/top10/)
*   **Python Security Best Practices:** [https://wiki.python.org/moin/WebProgramming](https://wiki.python.org/moin/WebProgramming)
*   **CWE/SANS Top 25:** [https://cwe.mitre.org/top25/](https://cwe.mitre.org/top25/)

## 9. Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en contactarnos.

*   **Cómo Reportar:** Envíe un correo electrónico a {contact_email} para reportar vulnerabilidades de seguridad.
*   **Email de Seguridad:** {contact_email}
*   **Contacto Directo:** Puede contactar directamente a los mantenedores del proyecto a través de los canales de comunicación oficiales del proyecto (por ejemplo, el servidor de Discord, el foro de discusión).
```