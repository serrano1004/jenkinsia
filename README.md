```markdown
# jenkinsia

Una aplicación Python simple para automatizar tareas de Jenkins.

[![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://img.shields.io/badge/status-stable-brightgreen.svg)

## Descripción General

Jenkinsia es una aplicación Python diseñada para simplificar y automatizar interacciones con servidores Jenkins.  Permite a los usuarios ejecutar jobs, obtener información del estado de la build y gestionar parámetros de manera programática.  Esta herramienta facilita la integración continua y la entrega continua (CI/CD) al proporcionar una interfaz de línea de comandos (CLI) intuitiva y una API para interactuar con Jenkins.

El proyecto nace de la necesidad de automatizar tareas repetitivas en Jenkins, como el despliegue de aplicaciones, la ejecución de pruebas y la gestión de configuraciones.  Al automatizar estas tareas, se reduce el riesgo de errores humanos, se acelera el ciclo de desarrollo y se mejora la eficiencia general del proceso de CI/CD.

Jenkinsia resuelve el problema de la gestión manual de tareas en Jenkins, permitiendo a los usuarios definir y ejecutar flujos de trabajo complejos de forma programática.  La audiencia objetivo incluye desarrolladores, ingenieros de DevOps, administradores de sistemas y cualquier persona que utilice Jenkins para la automatización de procesos.

## Características Clave

*   🚀 **Ejecución de Jobs:** Inicia jobs de Jenkins con parámetros definidos.
*   📊 **Estado de Builds:** Obtén información detallada sobre el estado de las builds, incluyendo logs y resultados.
*   ⚙️ **Gestión de Parámetros:** Define y gestiona parámetros de jobs de manera programática.
*   🔗 **API REST:** Proporciona una API REST para integración con otras herramientas y sistemas.
*   🐍 **Interfaz de Línea de Comandos (CLI):** Interfaz CLI intuitiva para facilitar el uso desde la terminal.

## Requisitos Previos

*   **Sistema Operativo:** Compatible con Linux, macOS y Windows.
*   **Python:** Versión 3.7 o superior.
*   **Jenkins:** Un servidor Jenkins en funcionamiento.
*   **Requests:** Biblioteca Python para realizar solicitudes HTTP.
*   **Click:** Biblioteca Python para crear interfaces de línea de comandos.

## Instalación Rápida

1.  Clona el repositorio:

    ```bash
    git clone https://github.com/serrano1004/jenkinsia.git
    ```

2.  Navega al directorio del proyecto:

    ```bash
    cd jenkinsia
    ```

3.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4.  Verifica la instalación:

    ```bash
    python jenkinsia.py --help
    ```

Para una instalación más detallada, consulta el archivo [INSTALL.md](INSTALL.md).

## Guía Rápida de Uso

Ejemplo básico de uso para ejecutar un job en Jenkins:

```bash
python jenkinsia.py execute-job --job-name "mi-job" --parameter "param1=valor1" --parameter "param2=valor2" --jenkins-url "http://mi-jenkins.com" --username "mi_usuario" --password "mi_password"
```

Este comando ejecuta el job "mi-job" en el servidor Jenkins especificado, pasando los parámetros "param1" y "param2".

Salida esperada:

```
Job 'mi-job' ejecutado correctamente.
Build URL: http://mi-jenkins.com/job/mi-job/123
```

Caso de uso común: Automatizar el despliegue de una aplicación después de una confirmación exitosa en el repositorio de código.

## Arquitectura del Proyecto

```
+---------------------+    +---------------------+    +---------------------+
| Interfaz de Usuario |    |  Lógica Principal   |    |    Servidor Jenkins  |
| (CLI / API)         |    |   (jenkinsia.py)    |    |                     |
+---------------------+    +---------------------+    +---------------------+
         |                     |          |          |          |
         |  Comandos / Solicitudes |          |          |          |
         --------------------->|          |          |          |
                              |  Solicitudes HTTP  |--------->|  Ejecución de Jobs |
                              |          |          |<---------|  Estado de Builds  |
                              |  Respuesta HTTP   |<---------|                     |
         |                     |          |          |          |
         |  Resultados / Datos  |<---------------------|          |          |
         ---------------------|          |          |          |
```

Componentes clave:

*   **Interfaz de Usuario (CLI/API):**  Proporciona la forma en que los usuarios interactúan con Jenkinsia.
*   **Lógica Principal (jenkinsia.py):**  Contiene la lógica principal de la aplicación, incluyendo la gestión de parámetros, la ejecución de jobs y la obtención de información del estado de la build. Utiliza la librería `requests` para comunicarse con el servidor Jenkins.
*   **Servidor Jenkins:**  El sistema de automatización de código abierto al que Jenkinsia se conecta para ejecutar tareas.

## Detalles Técnicos

Jenkinsia utiliza la librería `requests` para realizar solicitudes HTTP al servidor Jenkins.  La elección de `requests` se basa en su simplicidad y facilidad de uso para interactuar con APIs REST. La aplicación se basa en el patrón de diseño Command-Line Interface (CLI) para proporcionar una interfaz intuitiva para los usuarios.

Las decisiones arquitectónicas se centraron en la simplicidad y la facilidad de uso.  Se priorizó la legibilidad del código y la facilidad de mantenimiento.

## Ejemplos de Uso

1.  **Obtener el estado de la última build de un job:**

    ```bash
    python jenkinsia.py get-build-status --job-name "mi-job" --jenkins-url "http://mi-jenkins.com" --username "mi_usuario" --password "mi_password"
    ```

    Salida esperada:

    ```
    Estado de la última build de 'mi-job': SUCCESS
    ```

2.  **Ejecutar un job con múltiples parámetros:**

    ```bash
    python jenkinsia.py execute-job --job-name "mi-job" --parameter "param1=valor1" --parameter "param2=valor2" --parameter "param3=valor3" --jenkins-url "http://mi-jenkins.com" --username "mi_usuario" --password "mi_password"
    ```

    Salida esperada:

    ```
    Job 'mi-job' ejecutado correctamente.
    Build URL: http://mi-jenkins.com/job/mi-job/456
    ```

3.  **Obtener los logs de una build específica:**

    ```bash
    python jenkinsia.py get-build-logs --job-name "mi-job" --build-number 123 --jenkins-url "http://mi-jenkins.com" --username "mi_usuario" --password "mi_password"
    ```

    Salida esperada:

    ```
    [Jenkins] $ /bin/bash /tmp/hudson12345.sh
    [Jenkins] Building in workspace /var/lib/jenkins/workspace/mi-job
    [Jenkins] ... (logs de la build) ...
    [Jenkins] Finished: SUCCESS
    ```

## Configuración

*   **Variables de entorno:**
    *   `JENKINS_URL`: URL del servidor Jenkins.
    *   `JENKINS_USERNAME`: Nombre de usuario para autenticación en Jenkins.
    *   `JENKINS_PASSWORD`: Contraseña o token de API para autenticación en Jenkins.

*   **Archivos de configuración:** No se utiliza actualmente.  La configuración se realiza a través de variables de entorno y parámetros de línea de comandos.

*   **Opciones de personalización:**  Se pueden personalizar los parámetros de los jobs y la configuración de la conexión al servidor Jenkins.

Para más detalles sobre la configuración, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de autenticación:**

    *   Causa probable: Credenciales incorrectas.
    *   Solución: Verifica que el nombre de usuario y la contraseña sean correctos.  Si utilizas un token de API, asegúrate de que tenga los permisos necesarios.
    *   Comando de diagnóstico: Verifica las variables de entorno `JENKINS_USERNAME` y `JENKINS_PASSWORD`.

2.  **Error de conexión al servidor Jenkins:**

    *   Causa probable: El servidor Jenkins no está accesible.
    *   Solución: Verifica que el servidor Jenkins esté en funcionamiento y que la URL sea correcta.
    *   Comando de diagnóstico: Utiliza `ping` o `curl` para verificar la conectividad al servidor Jenkins.

3.  **Job no encontrado:**

    *   Causa probable: El nombre del job es incorrecto.
    *   Solución: Verifica que el nombre del job sea correcto y que el job exista en el servidor Jenkins.
    *   Comando de diagnóstico: Utiliza la API de Jenkins para listar los jobs disponibles.

## Contribuciones

¡Las contribuciones son bienvenidas!

*   Para reportar bugs, crea un nuevo issue en GitHub.
*   Para sugerir features, crea un nuevo issue en GitHub.
*   Consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más información sobre cómo contribuir.

Por favor, revisa nuestro código de conducta antes de contribuir.

## Licencia y Créditos

Este proyecto está licenciado bajo la licencia MIT.

[LICENSE](LICENSE)

Agradecimientos a la comunidad de Python y a los desarrolladores de Jenkins por sus excelentes herramientas y recursos.

## Contacto y Soporte

*   Email de contacto: [tu_email@example.com](mailto:tu_email@example.com)
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [Enlace a la documentación]
*   Community links: [Enlace a la comunidad]
```