```markdown
# jenkinsia

Una aplicación Python para simplificar las tareas de CI/CD con Jenkins.

[![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Stable-green.svg)](https://www.repostatus.org/#stable)

## Descripción General

Jenkinsia es una aplicación escrita en Python diseñada para facilitar la interacción con Jenkins, un servidor de automatización de código abierto.  Su objetivo principal es simplificar la configuración, gestión y ejecución de pipelines de CI/CD (Integración Continua/Entrega Continua), permitiendo a los desarrolladores y equipos de operaciones centrarse en la creación de software de alta calidad en lugar de lidiar con la complejidad de la infraestructura de CI/CD.

Este proyecto nace de la necesidad de automatizar tareas repetitivas y propensas a errores en el flujo de trabajo de desarrollo.  Muchas veces, configurar trabajos en Jenkins, monitorearlos y gestionar sus dependencias puede ser un proceso tedioso y consumir mucho tiempo. Jenkinsia busca eliminar esta fricción, proporcionando una interfaz intuitiva y herramientas que permiten a los usuarios definir, ejecutar y monitorizar sus pipelines de manera eficiente.

Jenkinsia resuelve el problema de la complejidad en la gestión de CI/CD al abstraer las complejidades de la API de Jenkins y proporcionar una capa de abstracción que simplifica las interacciones.  Esto reduce la curva de aprendizaje para los nuevos usuarios y aumenta la productividad de los usuarios experimentados. La audiencia objetivo de Jenkinsia son desarrolladores, ingenieros de DevOps y administradores de sistemas que buscan una forma más fácil y eficiente de gestionar sus pipelines de CI/CD con Jenkins.

## Características Clave

*   ⚙️ **Configuración Simplificada de Pipelines:** Define tus pipelines en archivos YAML y despliégalos con un solo comando.
*   📊 **Monitorización en Tiempo Real:** Visualiza el estado de tus builds y pruebas en tiempo real a través de una interfaz web intuitiva.
*   🔔 **Notificaciones Personalizables:** Recibe notificaciones sobre el estado de tus builds a través de correo electrónico, Slack o cualquier otro servicio de mensajería.
*   🛡️ **Seguridad Integrada:** Gestiona los permisos y el acceso a tus pipelines de forma segura con autenticación y autorización basadas en roles.
*   🔌 **Extensible:** Añade nuevas funcionalidades a Jenkinsia a través de plugins y extensiones.
*   🔗 **Integración con Git:** Automatiza la ejecución de tus pipelines con cada commit a tu repositorio Git.
*   🔍 **Logs centralizados:** Accede a los logs de tus builds desde un único lugar para facilitar la resolución de problemas.
*   ⏱️ **Programación de Jobs:** Define horarios para la ejecución automática de tus pipelines.

## Requisitos Previos

*   **Sistema Operativo:** Compatible con Linux, macOS y Windows.
*   **Python:** Versión 3.7 o superior.
*   **Jenkins:** Una instancia de Jenkins en ejecución y accesible.
*   **Pip:** El gestor de paquetes de Python.
*   **Acceso a la API de Jenkins:** Necesitarás un token de API de Jenkins con los permisos adecuados.

Tabla de requisitos:

| Requisito   | Versión Mínima | Notas                                  |
| :---------- | :------------- | :------------------------------------- |
| Python      | 3.7            | Recomendado 3.8 o superior             |
| Jenkins     | 2.0            | Con plugin API Remote Access habilitado |
| Pip         | 20.0           | Para la instalación de dependencias    |

## Instalación Rápida

1.  Clona el repositorio:

    ```bash
    git clone https://github.com/serrano1004/jenkinsia.git
    cd jenkinsia
    ```

2.  Crea un entorno virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
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

1.  Configura las variables de entorno:

    ```bash
    export JENKINS_URL="http://tu-jenkins-url:8080"
    export JENKINS_USER="tu_usuario"
    export JENKINS_PASSWORD="tu_contraseña" # o JENKINS_TOKEN
    ```

2.  Ejecuta un comando básico:

    ```bash
    python jenkinsia.py list_jobs
    ```

3.  Salida esperada (ejemplo):

    ```
    Available Jenkins Jobs:
    - job1
    - job2
    - job3
    ```

Caso de uso común: Listar todos los jobs en Jenkins.

## Arquitectura del Proyecto

```
+---------------------+     +---------------------+     +---------------------+
|  Línea de Comandos  | --> |  Capa de Abstracción | --> |   API de Jenkins    |
|  (jenkinsia.py)     |     |  (funciones Python)  |     |   (HTTP Requests)   |
+---------------------+     +---------------------+     +---------------------+
         |                      |                      |
         |                      |                      |
+---------------------+     +---------------------+
| Archivos de Config. |     |  Manejo de Errores  |
|  (YAML, .env)       |     +---------------------+
+---------------------+
```

El flujo principal de datos es el siguiente: El usuario interactúa con la aplicación a través de la línea de comandos (jenkinsia.py).  Esta interacción es procesada por la capa de abstracción, que contiene funciones Python diseñadas para simplificar las llamadas a la API de Jenkins.  Finalmente, la capa de abstracción realiza peticiones HTTP a la API de Jenkins para ejecutar las acciones solicitadas. Los archivos de configuración (YAML, .env) almacenan información como la URL de Jenkins, las credenciales y la configuración de los jobs. El manejo de errores se realiza en la capa de abstracción para proporcionar mensajes de error claros y concisos al usuario.

Componentes clave:

*   `jenkinsia.py`:  Script principal que interpreta los comandos del usuario.
*   Capa de abstracción: Conjunto de funciones que simplifican la interacción con la API de Jenkins.
*   Archivos de configuración: Almacenan la configuración de la aplicación y los jobs.

## Detalles Técnicos

Jenkinsia utiliza la librería `requests` de Python para realizar peticiones HTTP a la API de Jenkins.  La decisión de usar `requests` se basa en su simplicidad, popularidad y robustez.  Para la gestión de la configuración, se utilizan archivos YAML y la librería `PyYAML` para su lectura y escritura.

Las decisiones arquitectónicas se centraron en la simplicidad y la facilidad de uso.  Se optó por una arquitectura modular que permite añadir nuevas funcionalidades a través de plugins y extensiones.

Requisitos de rendimiento: Jenkinsia está diseñada para ser ligera y eficiente.  El tiempo de respuesta de los comandos depende principalmente de la velocidad de la API de Jenkins.

## Ejemplos de Uso

1.  **Crear un nuevo job:**

    ```bash
    python jenkinsia.py create_job --config job_config.yaml
    ```

    Donde `job_config.yaml` contiene la configuración del job en formato YAML.

    Ejemplo de `job_config.yaml`:

    ```yaml
    job_name: my_new_job
    description: "A simple job created with jenkinsia"
    script: |
      echo "Hello, world!"
    ```

    Salida esperada:

    ```
    Job 'my_new_job' created successfully.
    ```

2.  **Ejecutar un job existente:**

    ```bash
    python jenkinsia.py build_job --job my_existing_job
    ```

    Salida esperada:

    ```
    Job 'my_existing_job' triggered successfully. Build number: 123
    ```

3.  **Obtener el estado de un job:**

    ```bash
    python jenkinsia.py get_job_status --job my_existing_job
    ```

    Salida esperada:

    ```
    Job 'my_existing_job' status: SUCCESS
    Last build: 123
    Result: SUCCESS
    ```

## Configuración

Las siguientes variables de entorno son importantes para la configuración de Jenkinsia:

*   `JENKINS_URL`:  La URL de tu instancia de Jenkins.
*   `JENKINS_USER`:  Tu nombre de usuario de Jenkins.
*   `JENKINS_PASSWORD`: Tu contraseña de Jenkins (no recomendado, usa `JENKINS_TOKEN` en su lugar).
*   `JENKINS_TOKEN`: Tu token de API de Jenkins.

Puedes configurar estas variables en un archivo `.env` en la raíz del proyecto.

Ejemplo de `.env`:

```
JENKINS_URL=http://tu-jenkins-url:8080
JENKINS_USER=tu_usuario
JENKINS_TOKEN=tu_token
```

Para más detalles sobre la configuración, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de conexión a Jenkins:**

    *   Causa probable: La URL de Jenkins es incorrecta o Jenkins no está en ejecución.
    *   Solución: Verifica la URL de Jenkins y asegúrate de que Jenkins esté en ejecución.

    Comando de diagnóstico:

    ```bash
    ping tu-jenkins-url
    ```

2.  **Error de autenticación:**

    *   Causa probable: El nombre de usuario o la contraseña/token de Jenkins son incorrectos.
    *   Solución: Verifica tus credenciales de Jenkins y asegúrate de que tengan los permisos adecuados.

    Comando de diagnóstico:

    ```bash
    curl -v -u tu_usuario:tu_contraseña http://tu-jenkins-url:8080/api/json
    ```

3.  **Job no encontrado:**

    *   Causa probable: El nombre del job es incorrecto o el job no existe.
    *   Solución: Verifica el nombre del job y asegúrate de que exista en Jenkins.

    Comando de diagnóstico:

     ```bash
     python jenkinsia.py list_jobs
     ```

## Contribuciones

Las contribuciones son bienvenidas!

*   Para reportar bugs, abre un issue en GitHub.
*   Para sugerir features, abre un issue en GitHub.
*   Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

Por favor, respeta nuestro [Código de Conducta](CODE_OF_CONDUCT.md).

## Licencia y Créditos

Este proyecto está licenciado bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

Agradecimientos especiales a la comunidad de Jenkins por su excelente trabajo.

Inspirado en [otros proyectos de automatización de CI/CD](https://example.com/otros-proyectos).

## Contacto y Soporte

*   Email de contacto: [tu_email@example.com](mailto:tu_email@example.com)
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [https://example.com/jenkinsia/docs](https://example.com/jenkinsia/docs)
*   Community links: [https://example.com/jenkinsia/community](https://example.com/jenkinsia/community)
```