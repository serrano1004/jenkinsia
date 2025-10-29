```markdown
# SECURITY.md

La seguridad es una prioridad en el proyecto {project_name}. Este documento describe nuestras prácticas de seguridad, cómo reportar vulnerabilidades de manera responsable y otra información importante relacionada con la seguridad.

Este documento cubre las políticas de seguridad para el proyecto {project_name}, incluyendo cómo reportar vulnerabilidades, las prácticas de seguridad que seguimos, y las vulnerabilidades conocidas y mitigaciones.

## Reportar Vulnerabilidades de Seguridad

Creemos que la seguridad de {project_name} es importante y agradecemos la ayuda de la comunidad para identificar y resolver vulnerabilidades. Si descubre una vulnerabilidad de seguridad, **NO cree un issue público**. En su lugar, envíe un correo electrónico directamente a: {contact_email}.

Por favor, incluya la siguiente información en su reporte:

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad (si es posible).
*   Versión del software afectado.
*   Posibles impactos de la vulnerabilidad.
*   Sugerencias para la mitigación o solución (si las tiene).

Nos comprometemos a responder a su reporte dentro de un plazo de [X días/horas] para acusar recibo del informe y proporcionar una estimación del tiempo necesario para investigar y corregir la vulnerabilidad.

Practicamos la divulgación responsable.  No divulgaremos públicamente la vulnerabilidad hasta que se haya investigado, parcheado y probado adecuadamente.  Trabajaremos con usted para coordinar la divulgación pública una vez que la vulnerabilidad haya sido abordada.  Agradecemos su cooperación y discreción.

## Prácticas de Seguridad

Implementamos las siguientes prácticas de seguridad para proteger el proyecto {project_name} y sus usuarios:

### 3.1 Gestión de Dependencias

Es crucial gestionar las dependencias de manera segura para evitar vulnerabilidades introducidas por bibliotecas de terceros.

*   **Verificación de Dependencias:** Use herramientas como `pip-audit` (para Python) o `npm audit` (para Node.js) para escanear sus dependencias en busca de vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

    ```bash
    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantenimiento Actualizado:** Mantenga sus dependencias actualizadas a las últimas versiones para corregir vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip
    pip install --upgrade -r requirements.txt
    ```

    ```bash
    # Ejemplo con npm
    npm update
    ```

*   **Alertas de Vulnerabilidades:** Configure alertas de vulnerabilidades en plataformas como GitHub para recibir notificaciones cuando se detecten vulnerabilidades en sus dependencias.  GitHub Dependency Graph y Dependabot pueden ayudar con esto.

### 3.2 Manejo de Secretos

El manejo seguro de secretos es fundamental para prevenir la exposición de información sensible.

*   **No Hardcodear Secretos:** NUNCA incluya contraseñas, claves API u otra información sensible directamente en el código.

    ```python
    # INSEGURO: Clave API hardcodeada
    api_key = "YOUR_API_KEY"

    # SEGURO: Usar variables de entorno
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **Variables de Entorno:** Use variables de entorno para almacenar información sensible y acceder a ella en tiempo de ejecución.

*   **.env en .gitignore:** Incluya el archivo `.env` (si lo usa para desarrollo local) en el archivo `.gitignore` para evitar que se suba al repositorio.

*   **Herramientas de Detección de Leaks:** Use herramientas como `git-secrets` o `trufflehog` para escanear el repositorio en busca de posibles fugas de secretos.

### 3.3 Validación de Entrada

Validar la entrada del usuario es crucial para prevenir ataques de inyección y otros problemas de seguridad.

*   **Validar Entrada:** Siempre valide y limpie la entrada del usuario antes de usarla.

    ```python
    # INSEGURO: Sin validación de entrada
    user_input = request.args.get('input')
    # Ejecuta comando directamente con la entrada del usuario (VULNERABLE A INYECCIÓN DE COMANDOS)
    os.system("echo " + user_input)

    # SEGURO: Validar y limpiar la entrada
    import re
    user_input = request.args.get('input')
    if re.match("^[a-zA-Z0-9]*$", user_input): # Permitir solo alfanumérico
        os.system("echo " + user_input)
    else:
        print("Entrada inválida")
    ```

*   **Prevenir Inyección:** Use parametrización o escaping para prevenir ataques de inyección SQL, inyección de comandos y otros tipos de inyección.

### 3.4 Gestión de Acceso

La gestión adecuada del acceso es esencial para proteger los recursos del proyecto.

*   **Principio de Mínimo Privilegio:** Otorgue a los usuarios solo los permisos necesarios para realizar sus tareas.

*   **SSH Keys vs HTTPS:** Use SSH keys para el acceso al repositorio en lugar de contraseñas (HTTPS) siempre que sea posible.

*   **Permisos de Archivos:** Establezca permisos de archivos adecuados para proteger la información sensible.

## 4. Seguridad en CI/CD

La seguridad en el proceso de Integración Continua/Entrega Continua (CI/CD) es fundamental para evitar la introducción de vulnerabilidades en el código.

*   **Secrets en Jenkins/GitHub Actions:**  Use las funcionalidades de gestión de secretos proporcionadas por su plataforma de CI/CD (por ejemplo, "Credentials" en Jenkins o "Secrets" en GitHub Actions) para almacenar de forma segura las credenciales y otra información sensible.

*   **Cómo usar Credentials:**  Acceda a los secretos a través de las variables de entorno que la plataforma de CI/CD proporciona.  Evite hardcodear o loguear las credenciales directamente en los scripts.

    ```yaml
    # Ejemplo en GitHub Actions
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        env:
          API_KEY: ${{ secrets.API_KEY }} # Acceder al secreto API_KEY
        run: pytest
    ```

*   **No loguear información sensible:** Evite loguear información sensible (como contraseñas, claves API, etc.) en los registros de CI/CD.  Si necesita depurar, use logs temporales y asegúrese de eliminarlos después.

## 5. Testing de Seguridad

El testing de seguridad es una parte integral del ciclo de vida del desarrollo de software seguro.

*   **Herramientas:** Use herramientas de análisis estático de código (SAST) y análisis dinámico de código (DAST) para identificar vulnerabilidades en su código.  Ejemplos de herramientas incluyen `bandit` (para Python), `safety` (para Python), y `pip-audit` (para Python).

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

*   **Cómo ejecutar:** Integre estas herramientas en su proceso de CI/CD para realizar pruebas de seguridad automatizadas.

*   **Qué buscar:** Busque vulnerabilidades comunes como inyección SQL, cross-site scripting (XSS), y desbordamiento de búfer.

*   **Análisis SAST:** El Análisis Estático de Seguridad de Aplicaciones (SAST) examina el código fuente en busca de posibles vulnerabilidades sin ejecutar el programa.

## 6. Checklist de Seguridad para Contribuidores

Como contribuidor, es importante seguir estas pautas de seguridad:

*   **No incluir secrets:** Nunca incluya contraseñas, claves API u otra información sensible en el código.
*   **No usar shell=True:** Evite usar `shell=True` en funciones como `subprocess.run` en Python, ya que puede ser vulnerable a inyección de comandos.
*   **Validar inputs:** Siempre valide y limpie la entrada del usuario antes de usarla.
*   **Sin hardcoded passwords:** No incluya contraseñas hardcodeadas en el código.
*   **Revisar cambios:** Revise cuidadosamente los cambios de código antes de fusionarlos para detectar posibles vulnerabilidades.

## 7. Vulnerabilidades Conocidas

Esta sección lista las vulnerabilidades conocidas que han sido parcheadas en versiones anteriores de {project_name}.

*   **CVE-2023-XXXX:** Vulnerabilidad de XSS en la versión 1.0.0.  Actualice a la versión 1.0.1 o superior para corregir esta vulnerabilidad.
*   **CVE-2023-YYYY:** Vulnerabilidad de inyección SQL en la versión 1.1.0.  Actualice a la versión 1.1.1 o superior para corregir esta vulnerabilidad.

## 8. Recursos de Seguridad

Aquí hay algunos recursos adicionales que pueden ser útiles para aprender más sobre seguridad de software:

*   [OWASP Top 10](https://owasp.org/www-project-top-ten/): Una lista de las 10 vulnerabilidades web más críticas.
*   [Python Security Best Practices](https://wiki.python.org/moin/Security):  Guía de seguridad para desarrolladores de Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Una lista de las 25 debilidades de software más peligrosas.

## 9. Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en ponerse en contacto con nosotros.

*   Para reportar vulnerabilidades, envíe un correo electrónico a: {contact_email}.
*   Para otras consultas relacionadas con la seguridad, puede contactarnos directamente.
```