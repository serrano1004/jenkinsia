```markdown
# SECURITY.md

La seguridad es de suma importancia para el proyecto {project_name}. Nos tomamos en serio la seguridad de nuestros usuarios y colaboradores.

Este documento describe nuestras políticas y procedimientos para manejar vulnerabilidades de seguridad, así como las mejores prácticas para desarrollar y mantener un código seguro.

## Reportar Vulnerabilidades de Seguridad

Si cree haber encontrado una vulnerabilidad de seguridad en {project_name}, le rogamos que nos la comunique de forma responsable. **Por favor, NO cree un issue público en el repositorio.** Esto podría exponer la vulnerabilidad a usuarios malintencionados antes de que tengamos la oportunidad de corregirla.

En su lugar, envíe un correo electrónico a {contact_email} con una descripción detallada de la vulnerabilidad. Incluya la siguiente información:

*   **Descripción de la vulnerabilidad:** Explique claramente la vulnerabilidad y cómo se puede explotar.
*   **Pasos para reproducir:** Proporcione instrucciones detalladas para reproducir la vulnerabilidad.  Cuanto más clara sea la información, más rápido podremos investigar y solucionar el problema.
*   **Componentes afectados:** Indique qué componentes del proyecto se ven afectados por la vulnerabilidad.
*   **Posible impacto:** Describa el posible impacto de la vulnerabilidad en los usuarios y el sistema.
*   **Información de contacto:** Incluya su nombre y dirección de correo electrónico para que podamos ponernos en contacto con usted si necesitamos más información.

Nos comprometemos a responder a su informe en un plazo de 72 horas.  Trabajaremos diligentemente para investigar la vulnerabilidad y desarrollar una solución.

**Proceso de Divulgación Responsable:**  Una vez que hayamos confirmado la vulnerabilidad y desarrollado una solución, trabajaremos con usted para coordinar la divulgación de la información.  Preferimos divulgar la información de forma pública una vez que se haya publicado una corrección y los usuarios tengan la oportunidad de actualizar sus sistemas.  Agradecemos su cooperación en este proceso.

## Prácticas de Seguridad

A continuación, se presentan algunas prácticas de seguridad importantes que seguimos en el proyecto {project_name}:

### 3.1 Gestión de Dependencias

Es crucial gestionar las dependencias de forma segura para evitar la introducción de vulnerabilidades a través de bibliotecas de terceros.

*   **Verificación de Dependencias:**  Utilizamos herramientas como `pip-audit` (para Python) y `npm audit` (para Node.js) para verificar si hay vulnerabilidades conocidas en nuestras dependencias.

    ```bash
    # Python
    pip install pip-audit
    pip-audit

    # Node.js
    npm audit
    ```

*   **Mantenimiento Actualizado:**  Mantenemos nuestras dependencias actualizadas a las últimas versiones para beneficiarnos de las correcciones de seguridad más recientes.

    ```bash
    # Python
    pip install --upgrade -r requirements.txt

    # Node.js
    npm update
    ```

*   **Alertas de Vulnerabilidades:**  Configuramos alertas de vulnerabilidades en nuestros repositorios de código (por ejemplo, a través de GitHub Dependabot) para ser notificados cuando se detectan nuevas vulnerabilidades en nuestras dependencias.

### 3.2 Manejo de Secretos

El manejo adecuado de secretos es esencial para proteger la información confidencial.

*   **NO Hardcodear Secretos:**  Nunca incluya secretos (contraseñas, claves API, etc.) directamente en el código fuente.

*   **Variables de Entorno:**  Utilice variables de entorno para almacenar secretos y acceder a ellos en su aplicación.

    ```python
    # Inseguro:
    api_key = "clave_secreta"

    # Seguro:
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **.env en .gitignore:**  Si utiliza archivos `.env` para almacenar variables de entorno localmente, asegúrese de agregarlos a su archivo `.gitignore` para evitar que se suban al repositorio.

*   **Herramientas de Detección de Leaks:**  Utilice herramientas de detección de leaks (como `git-secrets` o `truffleHog`) para buscar secretos expuestos accidentalmente en su historial de Git.

### 3.3 Validación de Entrada

La validación de entrada es fundamental para prevenir ataques de inyección y otros tipos de vulnerabilidades.

*   **Validar Entrada de Usuario:**  Siempre valide y limpie la entrada de usuario antes de utilizarla en su aplicación.

    ```python
    # Inseguro:
    nombre = input("Ingrese su nombre: ")
    # ... usar nombre directamente en una consulta SQL ...

    # Seguro:
    import re
    nombre = input("Ingrese su nombre: ")
    if re.match(r"^[a-zA-Z]+$", nombre):
        # ... usar nombre en la consulta SQL ...
    else:
        print("Nombre inválido")
    ```

*   **Prevenir Inyección:**  Utilice consultas parametrizadas o ORMs (Object-Relational Mappers) para prevenir ataques de inyección SQL.

    ```python
    # Inseguro:
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    consulta = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND clave = '{clave}'"
    # ... ejecutar consulta ...

    # Seguro:
    import sqlite3
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    consulta = "SELECT * FROM usuarios WHERE usuario = ? AND clave = ?"
    cursor.execute(consulta, (usuario, clave))
    # ... procesar resultados ...
    conexion.close()
    ```

### 3.4 Gestión de Acceso

Una gestión de acceso adecuada ayuda a limitar el impacto de posibles brechas de seguridad.

*   **Principio de Mínimo Privilegio:**  Asigne a los usuarios y procesos solo los permisos mínimos necesarios para realizar sus tareas.

*   **SSH Keys vs HTTPS:**  Utilice SSH keys para autenticar usuarios en lugar de contraseñas siempre que sea posible.  Asegúrese de que su sitio web utilice HTTPS para cifrar la comunicación entre el cliente y el servidor.

*   **Permisos de Archivos:**  Establezca permisos de archivos adecuados para proteger la información confidencial.

## Seguridad en CI/CD

La seguridad en la integración continua y la entrega continua (CI/CD) es crucial para automatizar la seguridad en el ciclo de vida del desarrollo.

*   **Secrets en Jenkins/GitHub Actions:**  Utilice las funciones de gestión de secretos proporcionadas por sus herramientas de CI/CD (por ejemplo, Jenkins Credentials Plugin o GitHub Actions Secrets) para almacenar y acceder a secretos de forma segura.

*   **Cómo Usar Credenciales:**  Al utilizar credenciales en sus scripts de CI/CD, asegúrese de que no se expongan accidentalmente en los registros de compilación.

    ```yaml
    # Inseguro:
    - run: echo "API_KEY=$API_KEY"

    # Seguro:
    - run: ./mi_script.sh  # mi_script.sh utiliza la variable de entorno API_KEY sin imprimirla
    ```

*   **No Loguear Información Sensible:**  Evite registrar información sensible (como contraseñas o claves API) en los registros de compilación.

## Testing de Seguridad

El testing de seguridad es una parte integral del proceso de desarrollo seguro.

*   **Herramientas:**  Utilizamos herramientas como `bandit` (para Python), `safety` (para Python) y `pip-audit` (para Python) para realizar análisis estático de seguridad (SAST) en nuestro código.

    ```bash
    # Bandit
    pip install bandit
    bandit -r .

    # Safety
    pip install safety
    safety check

    # pip-audit
    pip install pip-audit
    pip-audit
    ```

*   **Cómo Ejecutar:**  Integramos estas herramientas en nuestro proceso de CI/CD para que se ejecuten automáticamente en cada cambio de código.

*   **Qué Buscar:**  Buscamos vulnerabilidades comunes, como problemas de inyección, manejo inseguro de contraseñas y configuraciones de seguridad incorrectas.

*   **Análisis SAST:**  El análisis SAST (Static Application Security Testing) nos permite identificar vulnerabilidades en el código fuente sin necesidad de ejecutar la aplicación.

## Checklist de Seguridad para Contribuidores

Para garantizar la seguridad del proyecto, pedimos a todos los contribuyentes que sigan las siguientes pautas:

*   **No Incluir Secretos:**  Nunca incluya secretos (contraseñas, claves API, etc.) en su código.
*   **No Usar `shell=True`:**  Evite usar `shell=True` en las funciones `subprocess` de Python, ya que puede ser vulnerable a ataques de inyección de comandos.
*   **Validar Inputs:**  Siempre valide y limpie la entrada de usuario.
*   **Sin Hardcoded Passwords:**  No incluya contraseñas codificadas en el código.
*   **Revisar Cambios:**  Revise cuidadosamente sus cambios antes de enviarlos para detectar posibles problemas de seguridad.

## Vulnerabilidades Conocidas

Esta sección enumera las vulnerabilidades conocidas que han sido parcheadas en versiones anteriores del proyecto.

*   **CVE-2023-XXXX:**  Vulnerabilidad de inyección SQL en la versión 1.0.0.  Se corrigió en la versión 1.0.1.  Se recomienda actualizar a la versión 1.0.1 o posterior.
*   **CVE-2023-YYYY:**  Vulnerabilidad de cross-site scripting (XSS) en la versión 1.1.0.  Se corrigió en la versión 1.1.1.  Se recomienda actualizar a la versión 1.1.1 o posterior.

## Recursos de Seguridad

A continuación, se presentan algunos recursos útiles para aprender más sobre seguridad:

*   **OWASP Top 10:**  Las 10 vulnerabilidades web más críticas.
*   **Python Security Best Practices:**  Guía de buenas prácticas de seguridad para Python.
*   **CWE/SANS Top 25:**  Las 25 debilidades de software más peligrosas.

## Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad del proyecto {project_name}, no dude en ponerse en contacto con nosotros.

*   **Cómo Reportar:**  Envíe un correo electrónico a {contact_email} con una descripción detallada de su inquietud.
*   **Email de Seguridad:**  {contact_email}
*   **Contacto Directo:**  Puede ponerse en contacto con los mantenedores del proyecto directamente a través del repositorio de GitHub en {repository_url}.
```