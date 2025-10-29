```markdown
# jenkinsia

Una aplicación Python para la automatización de tareas en Jenkins.

[![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)](https://github.com/serrano1004/jenkinsia)

## Descripción General

`jenkinsia` es una aplicación Python diseñada para simplificar y automatizar interacciones con servidores Jenkins.  Esta herramienta facilita la gestión de trabajos (jobs), la obtención de información sobre el estado de las construcciones (builds), y la ejecución de tareas comunes a través de una interfaz de línea de comandos (CLI) o una API programática.

El proyecto nace de la necesidad de automatizar tareas repetitivas en Jenkins, como el despliegue de aplicaciones, la ejecución de pruebas automatizadas y la gestión de configuraciones.  Permite a los usuarios interactuar con Jenkins de manera más eficiente, reduciendo errores manuales y acelerando el ciclo de desarrollo.

`jenkinsia` resuelve el problema de la interacción manual y repetitiva con la interfaz web de Jenkins, ofreciendo una alternativa programática y automatizable.  Está dirigida a desarrolladores, ingenieros de DevOps y administradores de sistemas que utilizan Jenkins como su plataforma de integración continua y entrega continua (CI/CD).

## Características Clave

*   🚀 **Gestión de Jobs:** Crea, actualiza y elimina jobs en Jenkins desde la línea de comandos.
*   📊 **Estado de Builds:** Obtén información detallada sobre el estado de las construcciones, incluyendo logs y resultados de pruebas.
*   ⚙️ **Automatización de Tareas:** Ejecuta tareas comunes como el despliegue de aplicaciones y la ejecución de pruebas.
*   🔗 **Integración con API:** Interactúa con `jenkinsia` a través de una API programática para integrarla en tus flujos de trabajo existentes.
*   🔒 **Autenticación Segura:** Admite múltiples métodos de autenticación para acceder a tu servidor Jenkins de forma segura.

## Requisitos Previos

Para utilizar `jenkinsia`, necesitas lo siguiente:

*   **Sistema Operativo:** Linux, macOS, o Windows.
*   **Python:** Versión 3.7 o superior.
*   **pip:** El gestor de paquetes de Python.
*   **Acceso a un servidor Jenkins:** Con las credenciales necesarias para la autenticación.
*   **Conocimientos básicos de la línea de comandos.**

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
    python jenkinsia.py --version
    ```

Para una instalación más detallada, consulta el archivo [INSTALL.md](INSTALL.md).

## Guía Rápida de Uso

El siguiente ejemplo muestra cómo obtener el estado de un job específico en Jenkins:

```bash
python jenkinsia.py --url <URL_JENKINS> --username <USUARIO> --password <PASSWORD> get_job_status <NOMBRE_DEL_JOB>
```

Donde:

*   `<URL_JENKINS>` es la URL de tu servidor Jenkins.
*   `<USUARIO>` es tu nombre de usuario en Jenkins.
*   `<PASSWORD>` es tu contraseña en Jenkins.
*   `<NOMBRE_DEL_JOB>` es el nombre del job del que quieres obtener el estado.

La salida esperada será un mensaje indicando el estado del job, por ejemplo:

```
El job 'mi_job' está en estado: SUCCESS
```

Este es un caso de uso común para monitorizar el estado de las construcciones en Jenkins.

## Arquitectura del Proyecto

```
+---------------------+     +---------------------+     +---------------------+
|   Interfaz CLI/API  | --> |   Lógica Principal  | --> |  Servidor Jenkins   |
| (jenkinsia.py)      |     | (funciones, clases) |     | (API de Jenkins)    |
+---------------------+     +---------------------+     +---------------------+
         |                      |                      |
         |                      |                      |
         V                      V                      V
+---------------------+     +---------------------+     +---------------------+
|  Entrada del Usuario|     |   Procesamiento de  |     |  Respuesta de Jenkins|
| (comandos, datos)   |     |   Solicitudes       |     | (JSON, XML)         |
+---------------------+     +---------------------+     +---------------------+
```

*   **Interfaz CLI/API (jenkinsia.py):**  Proporciona la interfaz para interactuar con la aplicación, ya sea a través de la línea de comandos o mediante una API programática. Recibe la entrada del usuario y la pasa a la lógica principal.
*   **Lógica Principal:** Contiene las funciones y clases que implementan la lógica principal de la aplicación.  Procesa las solicitudes, se comunica con el servidor Jenkins y formatea la respuesta.
*   **Servidor Jenkins:** El servidor Jenkins al que se conecta la aplicación a través de su API.  Recibe las solicitudes, las procesa y devuelve la respuesta en formato JSON o XML.

El flujo de datos principal es el siguiente: el usuario introduce un comando a través de la CLI o la API, la lógica principal procesa la solicitud y se comunica con el servidor Jenkins, y el servidor Jenkins devuelve la respuesta que se formatea y se muestra al usuario.

## Detalles Técnicos

`jenkinsia` utiliza la biblioteca `requests` de Python para comunicarse con la API de Jenkins.  La autenticación se realiza mediante el protocolo HTTP Basic Authentication o a través de tokens de API.

Las decisiones arquitectónicas se basan en la necesidad de mantener la aplicación modular y fácil de extender.  Se han utilizado patrones de diseño como el patrón de fachada para simplificar la interacción con la API de Jenkins.

La elección de `requests` se debe a su simplicidad y popularidad en la comunidad de Python.  Los requisitos de rendimiento no son críticos para la mayoría de los casos de uso, pero se han optimizado las consultas a la API de Jenkins para minimizar la latencia.

## Ejemplos de Uso

1.  **Obtener información sobre un job:**

    ```bash
    python jenkinsia.py --url <URL_JENKINS> --username <USUARIO> --password <PASSWORD> get_job_info <NOMBRE_DEL_JOB>
    ```

    Salida esperada:

    ```json
    {
      "name": "mi_job",
      "url": "https://<URL_JENKINS>/job/mi_job/",
      "description": "Descripción del job"
    }
    ```

2.  **Lanzar un build de un job:**

    ```bash
    python jenkinsia.py --url <URL_JENKINS> --username <USUARIO> --password <PASSWORD> build_job <NOMBRE_DEL_JOB>
    ```

    Salida esperada:

    ```
    Build lanzado para el job 'mi_job'.
    ```

3.  **Obtener los logs de la última construcción de un job:**

    ```bash
    python jenkinsia.py --url <URL_JENKINS> --username <USUARIO> --password <PASSWORD> get_job_logs <NOMBRE_DEL_JOB>
    ```

    Salida esperada:

    ```
    [INFO] Iniciando la construcción...
    [INFO] Ejecutando pruebas...
    [INFO] Desplegando la aplicación...
    [INFO] Construcción finalizada con éxito.
    ```

## Configuración

`jenkinsia` se puede configurar a través de variables de entorno y un archivo de configuración.

*   **Variables de entorno:**
    *   `JENKINS_URL`: URL del servidor Jenkins.
    *   `JENKINS_USERNAME`: Nombre de usuario de Jenkins.
    *   `JENKINS_PASSWORD`: Contraseña de Jenkins.

*   **Archivo de configuración:**
    Puedes crear un archivo `config.ini` con la siguiente estructura:

    ```ini
    [jenkins]
    url = <URL_JENKINS>
    username = <USUARIO>
    password = <PASSWORD>
    ```

    Para usar el archivo de configuración, especifica la ruta en la línea de comandos:

    ```bash
    python jenkinsia.py --config config.ini get_job_status <NOMBRE_DEL_JOB>
    ```

Para obtener más detalles sobre la configuración, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de autenticación:**

    *   Causa probable: Credenciales incorrectas.
    *   Solución: Verifica que el nombre de usuario y la contraseña sean correctos.  Asegúrate de que el usuario tenga los permisos necesarios para acceder a la API de Jenkins.
    *   Comando de diagnóstico:  Verifica las credenciales directamente en la interfaz web de Jenkins.

2.  **Error de conexión:**

    *   Causa probable: No se puede acceder al servidor Jenkins.
    *   Solución: Verifica que el servidor Jenkins esté en funcionamiento y que la URL sea correcta.  Asegúrate de que no haya firewalls bloqueando la conexión.
    *   Comando de diagnóstico:  Utiliza `ping` o `curl` para verificar la conectividad al servidor Jenkins.

3.  **Error de "Job not found":**

    *   Causa probable: El job especificado no existe.
    *   Solución: Verifica que el nombre del job sea correcto.  Asegúrate de que el job exista en el servidor Jenkins.
    *   Comando de diagnóstico:  Lista todos los jobs disponibles en el servidor Jenkins a través de la API.

## Contribuciones

Si deseas contribuir a `jenkinsia`, por favor sigue estas pautas:

*   Reporta bugs a través de las [issues](https://github.com/serrano1004/jenkinsia/issues) de GitHub.
*   Sugiere nuevas características a través de las [issues](https://github.com/serrano1004/jenkinsia/issues) de GitHub.
*   Consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más información sobre cómo contribuir con código.
*   Respeta el [Código de Conducta](CODE_OF_CONDUCT.md).

## Licencia y Créditos

`jenkinsia` está licenciado bajo la [Licencia MIT](LICENSE).

Agradecimientos a la comunidad de Python y a los desarrolladores de Jenkins por su excelente trabajo.  Este proyecto se inspira en la necesidad de automatizar tareas repetitivas en Jenkins.

## Contacto y Soporte

Para obtener soporte, puedes contactarnos a través de:

*   Email: example@example.com
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [ENLACE A LA DOCUMENTACIÓN]
*   Community links: [ENLACE A LA COMUNIDAD]
```