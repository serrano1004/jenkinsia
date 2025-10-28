```markdown
# jenkinsia

Una aplicación Python para simplificar la gestión de pipelines en Jenkins.

[![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://github.com/serrano1004/jenkinsia)

## Descripción General

Jenkinsia es una aplicación Python diseñada para facilitar la interacción con servidores Jenkins.  Su objetivo principal es simplificar la creación, gestión y monitorización de pipelines de integración continua y entrega continua (CI/CD). Proporciona una interfaz de línea de comandos (CLI) intuitiva y fácil de usar que permite a los usuarios realizar tareas comunes en Jenkins sin necesidad de navegar por la interfaz web.

Esta herramienta surge de la necesidad de automatizar y agilizar las tareas repetitivas asociadas con la gestión de Jenkins.  Muchos desarrolladores y equipos de operaciones dedican una cantidad significativa de tiempo a configurar y mantener pipelines en Jenkins, lo que puede ser propenso a errores y consumir mucho tiempo. Jenkinsia busca reducir esta carga de trabajo al proporcionar una forma sencilla y eficiente de interactuar con Jenkins desde la línea de comandos.

El problema que resuelve Jenkinsia es la complejidad inherente a la gestión de pipelines en Jenkins, especialmente para aquellos que no están familiarizados con la interfaz web o que prefieren trabajar desde la línea de comandos.  Al proporcionar una herramienta CLI intuitiva, Jenkinsia permite a los usuarios realizar tareas como crear trabajos, disparar builds, obtener información sobre el estado de los builds y gestionar plugins de forma rápida y sencilla. La audiencia objetivo de Jenkinsia son desarrolladores, ingenieros de DevOps y administradores de sistemas que utilizan Jenkins para la automatización de sus procesos de CI/CD.

## Características Clave

*   🚀 **Creación de Trabajos:** Define y crea trabajos de Jenkins mediante archivos de configuración YAML.
*   ⚙️ **Gestión de Pipelines:** Inicia, detiene y monitoriza pipelines de Jenkins con comandos sencillos.
*   📊 **Información de Builds:** Obtén información detallada sobre el estado de los builds, incluyendo logs y resultados de pruebas.
*   🔌 **Gestión de Plugins:** Instala, desinstala y actualiza plugins de Jenkins desde la línea de comandos.
*   🛡️ **Autenticación Segura:** Soporte para múltiples métodos de autenticación, incluyendo tokens de API y credenciales.
*   📜 **Configuración Flexible:** Personaliza Jenkinsia mediante archivos de configuración y variables de entorno.
*   🔎 **Búsqueda Inteligente:** Encuentra trabajos y plugins rápidamente mediante la funcionalidad de búsqueda integrada.
*   📦 **Empaquetado y Distribución:** Disponible como paquete PyPI para una fácil instalación y actualización.
*   🤝 **Integración Continua:** Diseñado para integrarse perfectamente con otros sistemas y herramientas de CI/CD.

## Requisitos Previos

Para utilizar Jenkinsia, necesitarás lo siguiente:

*   **Sistema Operativo:** Linux, macOS o Windows.
*   **Python:** Versión 3.7 o superior.
*   **Jenkins:** Un servidor Jenkins en funcionamiento (versión 2.0 o superior recomendada).
*   **Pip:** El gestor de paquetes de Python.
*   **Acceso a la API de Jenkins:** Asegúrate de tener acceso a la API de Jenkins con las credenciales necesarias.

Es recomendable utilizar un entorno virtual de Python para aislar las dependencias del proyecto.

## Instalación Rápida

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/serrano1004/jenkinsia.git
    cd jenkinsia
    ```

2.  **Crea un entorno virtual (opcional pero recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate  # En Windows
    ```

3.  **Instala Jenkinsia:**

    ```bash
    pip install .
    ```

4.  **Verifica la instalación:**

    ```bash
    jenkinsia --version
    ```

Para obtener instrucciones de instalación más detalladas, consulta el archivo [INSTALL.md](INSTALL.md).

## Guía Rápida de Uso

Este ejemplo muestra cómo obtener información sobre un trabajo específico en Jenkins:

1.  **Configura las credenciales de Jenkins:**

    Puedes configurar las credenciales de Jenkins mediante variables de entorno:

    ```bash
    export JENKINS_URL="http://tu-servidor-jenkins:8080"
    export JENKINS_USERNAME="tu_usuario"
    export JENKINS_PASSWORD="tu_contraseña"
    ```

2.  **Ejecuta el comando para obtener información del trabajo:**

    ```bash
    jenkinsia job info mi_trabajo
    ```

3.  **Salida esperada:**

    ```
    Nombre: mi_trabajo
    URL: http://tu-servidor-jenkins:8080/job/mi_trabajo/
    Estado: SUCCESS
    Último build: #123
    ```

Este es un caso de uso común para obtener rápidamente información sobre el estado de un trabajo.

## Arquitectura del Proyecto

```
+-----------------+      +-----------------+      +-----------------+
|  Interfaz CLI   |----->|  Lógica Central |----->|  Servidor Jenkins|
+-----------------+      +-----------------+      +-----------------+
        |                 |         |          |
        |                 |         |          |  API REST
        |                 |         |          |
        v                 v         v          v
+-----------------+      +-----------------+      +-----------------+
|  Entrada Usuario|      |  Procesamiento  |      |  Datos Jenkins  |
+-----------------+      +-----------------+      +-----------------+
```

*   **Interfaz CLI:** Proporciona la interfaz de línea de comandos para interactuar con Jenkinsia.  Recibe los comandos del usuario y los pasa a la lógica central. (Python)
*   **Lógica Central:** Contiene la lógica principal de la aplicación, incluyendo la gestión de la configuración, la autenticación y la comunicación con el servidor Jenkins. (Python)
*   **Servidor Jenkins:** El servidor Jenkins al que se conecta Jenkinsia para realizar las operaciones solicitadas. (Java)
*   **Entrada Usuario:** Representa la entrada del usuario a través de la CLI.
*   **Procesamiento:** La lógica de negocio que transforma la entrada del usuario en acciones sobre el servidor Jenkins.
*   **Datos Jenkins:** La información que reside en el servidor Jenkins y que es accedida y manipulada por Jenkinsia.

El flujo de datos principal es el siguiente: el usuario introduce un comando en la CLI, la CLI pasa el comando a la lógica central, la lógica central se comunica con el servidor Jenkins a través de la API REST, el servidor Jenkins procesa la solicitud y devuelve una respuesta, la lógica central procesa la respuesta y la muestra al usuario a través de la CLI.

## Detalles Técnicos

Jenkinsia utiliza la biblioteca `requests` de Python para comunicarse con la API REST de Jenkins. Se ha elegido esta biblioteca por su facilidad de uso y su amplia compatibilidad.  Las decisiones arquitectónicas se basan en la necesidad de mantener la aplicación simple, modular y fácil de mantener. Se ha utilizado un diseño orientado a objetos para facilitar la reutilización del código y la extensibilidad.

El patrón principal utilizado es el patrón Fachada, donde la lógica central actúa como una fachada que simplifica la interacción con la API de Jenkins.

Las dependencias críticas incluyen `requests` para la comunicación HTTP y `PyYAML` para la gestión de archivos de configuración YAML.  `Requests` se eligió por su simplicidad y madurez, mientras que `PyYAML` se eligió por su capacidad para leer y escribir archivos YAML de forma sencilla.

Jenkinsia está diseñado para ser eficiente y consumir pocos recursos. Los requisitos de rendimiento se centran en minimizar el tiempo de respuesta de la CLI y reducir el consumo de memoria.

## Ejemplos de Uso

1.  **Crear un trabajo desde un archivo YAML:**

    Crea un archivo llamado `job.yaml` con la siguiente configuración:

    ```yaml
    name: mi_nuevo_trabajo
    description: Este es un trabajo de prueba
    builders:
      - shell: echo "¡Hola, mundo!"
    ```

    Luego, ejecuta el siguiente comando:

    ```bash
    jenkinsia job create job.yaml
    ```

    Salida esperada:

    ```
    Trabajo 'mi_nuevo_trabajo' creado exitosamente.
    ```

2.  **Disparar un build de un trabajo existente:**

    ```bash
    jenkinsia job build mi_trabajo
    ```

    Salida esperada:

    ```
    Build disparado para el trabajo 'mi_trabajo'.
    ```

3.  **Obtener los logs de un build específico:**

    ```bash
    jenkinsia build logs mi_trabajo 123
    ```

    Salida esperada:

    ```
    [INFO] Ejecutando el build #123
    [INFO] ¡Hola, mundo!
    [INFO] Build finalizado con éxito.
    ```

## Configuración

Jenkinsia se puede configurar mediante variables de entorno y archivos de configuración.

*   **Variables de Entorno:**
    *   `JENKINS_URL`: La URL del servidor Jenkins.
    *   `JENKINS_USERNAME`: El nombre de usuario para autenticarse en Jenkins.
    *   `JENKINS_PASSWORD`: La contraseña para autenticarse en Jenkins.
    *   `JENKINS_TOKEN`: El token de API para autenticarse en Jenkins (alternativo a usuario/contraseña).

*   **Archivos de Configuración:**

    Puedes crear un archivo de configuración llamado `config.yaml` en el directorio de inicio del usuario para personalizar el comportamiento de Jenkinsia.

    Para obtener más detalles sobre las opciones de configuración, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de autenticación:**

    *   Causa probable: Credenciales incorrectas o falta de permisos en Jenkins.
    *   Solución: Verifica las credenciales y asegúrate de que el usuario tiene los permisos necesarios para acceder a la API de Jenkins.
    *   Comando de diagnóstico: `jenkinsia --debug job info mi_trabajo`

2.  **Error de conexión:**

    *   Causa probable: El servidor Jenkins no está accesible o la URL es incorrecta.
    *   Solución: Verifica que el servidor Jenkins está en funcionamiento y que la URL es correcta.
    *   Comando de diagnóstico: `ping tu-servidor-jenkins`

3.  **Error de plugin:**

    *   Causa probable: El plugin no está instalado o está desactualizado.
    *   Solución: Instala o actualiza el plugin en el servidor Jenkins.
    *   Comando de diagnóstico: `jenkinsia plugin info mi_plugin`

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un bug, tienes una sugerencia o quieres contribuir con código, por favor, sigue estos pasos:

1.  Reporta bugs mediante las [issues de GitHub](https://github.com/serrano1004/jenkinsia/issues).
2.  Sugiere nuevas funcionalidades mediante las [issues de GitHub](https://github.com/serrano1004/jenkinsia/issues).
3.  Consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más información sobre cómo contribuir con código.

Por favor, respeta el [Código de Conducta](CODE_OF_CONDUCT.md) al participar en la comunidad.

## Licencia y Créditos

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

Agradecemos a la comunidad de código abierto por su inspiración y apoyo.

## Contacto y Soporte

*   Email de contacto: [tu_email@example.com](mailto:tu_email@example.com)
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [https://github.com/serrano1004/jenkinsia/wiki](https://github.com/serrano1004/jenkinsia/wiki)
```