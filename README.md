```markdown
# jenkinsia [![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml) [![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/serrano1004/jenkinsia)

Una aplicación Python para la gestión y automatización de tareas en Jenkins.

## Descripción General

Jenkinsia es una aplicación Python diseñada para simplificar la interacción con servidores Jenkins.  Su objetivo principal es proporcionar una interfaz más amigable y automatizada para la gestión de trabajos, la monitorización de builds y la administración general de Jenkins.  La aplicación se enfoca en ofrecer herramientas que faciliten la vida de los desarrolladores y administradores de sistemas que utilizan Jenkins en su flujo de trabajo diario.

La necesidad de Jenkinsia surge de la complejidad inherente a la interfaz web de Jenkins, especialmente cuando se trata de tareas repetitivas o la gestión de múltiples instancias.  Jenkinsia busca resolver este problema proporcionando una capa de abstracción que permite a los usuarios interactuar con Jenkins de manera más eficiente a través de scripts y comandos.

Jenkinsia está dirigida a desarrolladores, administradores de sistemas, ingenieros de DevOps y cualquier persona que utilice Jenkins para la integración continua y la entrega continua (CI/CD).  Ofrece una alternativa a la interfaz web tradicional, permitiendo la automatización de tareas y la integración con otros sistemas y herramientas.

## Características Clave

*   🚀 **Automatización de Tareas:** Automatiza tareas repetitivas en Jenkins a través de scripts.
*   📊 **Monitorización de Builds:** Monitoriza el estado de los builds y recibe notificaciones.
*   ⚙️ **Gestión de Trabajos:** Crea, actualiza y elimina trabajos de Jenkins fácilmente.
*   🔗 **Integración con APIs:** Se integra con la API de Jenkins para un control total.
*   🛡️ **Autenticación Segura:** Soporta autenticación segura mediante tokens y credenciales.
*   📝 **Configuración Simplificada:** Configuración sencilla a través de archivos YAML.
*   📚 **Documentación Completa:** Documentación detallada para facilitar el uso y la personalización.
*   🤝 **Extensible:** Arquitectura modular que permite la extensión con plugins y scripts personalizados.

## Requisitos Previos

Para utilizar Jenkinsia, necesitas tener instalado lo siguiente:

*   **Sistema Operativo:** Compatible con Linux, macOS y Windows.
*   **Python:** Versión 3.7 o superior.
*   **Jenkins:** Una instancia de Jenkins en ejecución.
*   **Pip:** El gestor de paquetes de Python.
*   **Requests:** La librería HTTP de Python (se instalará automáticamente con Jenkinsia).

Tabla de Requisitos:

| Requisito      | Versión Mínima |
| -------------- | -------------- |
| Sistema Operativo | Linux/macOS/Windows |
| Python         | 3.7            |
| Jenkins        | 2.0            |

## Instalación Rápida

Sigue estos pasos para instalar Jenkinsia rápidamente:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/serrano1004/jenkinsia.git
    ```
2.  **Navega al directorio del proyecto:**
    ```bash
    cd jenkinsia
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install .
    ```
4.  **Verifica la instalación:**
    ```bash
    jenkinsia --version
    ```

Para una instalación más detallada y opciones avanzadas, consulta el archivo [INSTALL.md](INSTALL.md).

## Guía Rápida de Uso

Aquí tienes un ejemplo básico de cómo usar Jenkinsia para obtener información sobre un trabajo de Jenkins:

1.  **Configura las credenciales de Jenkins:**

    Crea un archivo `config.yaml` con la siguiente estructura:

    ```yaml
    jenkins_url: "http://tu-servidor-jenkins:8080"
    username: "tu_usuario"
    password: "tu_contraseña"
    ```

2.  **Ejecuta el comando para obtener información del trabajo:**

    ```bash
    jenkinsia job info --job-name mi_trabajo
    ```

    Salida esperada:

    ```
    Nombre del trabajo: mi_trabajo
    URL: http://tu-servidor-jenkins:8080/job/mi_trabajo/
    Estado: SUCCESS
    ```

Este es solo un ejemplo básico. Jenkinsia ofrece muchas más funcionalidades para la gestión y automatización de tareas en Jenkins.

## Arquitectura del Proyecto

```
+-----------------+    +-----------------+    +-----------------+
| Cliente (CLI)   |    |  API de Jenkins |    | Servidor Jenkins|
+-----------------+    +-----------------+    +-----------------+
        |                 |                 |
        |  Solicitud HTTP  |  Respuesta HTTP |
        |----------------->|----------------->|
        |                 |                 |
        |  Analiza datos   |  Gestiona Jobs  |
        |  Muestra info    |  Ejecuta Builds |
        |                 |                 |
+-----------------+    +-----------------+    +-----------------+

```

*   **Cliente (CLI):** Interfaz de línea de comandos que permite a los usuarios interactuar con Jenkinsia.
*   **API de Jenkins:** Capa de abstracción que facilita la comunicación con el servidor Jenkins a través de la API REST.
*   **Servidor Jenkins:** Instancia de Jenkins que ejecuta los trabajos y proporciona la información necesaria.

El flujo de datos principal es el siguiente:

1.  El usuario ejecuta un comando en la CLI de Jenkinsia.
2.  La CLI envía una solicitud HTTP a la API de Jenkins.
3.  La API de Jenkins se comunica con el servidor Jenkins.
4.  El servidor Jenkins procesa la solicitud y devuelve una respuesta.
5.  La API de Jenkins analiza la respuesta y la devuelve a la CLI.
6.  La CLI muestra la información al usuario.

## Detalles Técnicos

Jenkinsia utiliza la librería `requests` de Python para realizar las solicitudes HTTP a la API de Jenkins.  La decisión de utilizar `requests` se basa en su simplicidad, flexibilidad y amplia documentación.  El algoritmo principal es la gestión de la autenticación y la construcción de las URLs correctas para cada solicitud a la API de Jenkins.

Las decisiones arquitectónicas se centraron en la modularidad y la extensibilidad.  La API de Jenkins se diseñó como una capa de abstracción para facilitar la integración con diferentes versiones de Jenkins y para permitir la adición de nuevas funcionalidades.

## Ejemplos de Uso

1.  **Obtener información de un build específico:**

    ```bash
    jenkinsia build info --job-name mi_trabajo --build-number 123
    ```

    Salida esperada:

    ```
    Número de build: 123
    Resultado: SUCCESS
    Duración: 120 segundos
    ```

2.  **Lanzar un nuevo build de un trabajo:**

    ```bash
    jenkinsia job build --job-name mi_trabajo
    ```

    Salida esperada:

    ```
    Build lanzado con éxito.
    Número de build: 124
    ```

3.  **Obtener la lista de todos los trabajos en Jenkins:**

    ```bash
    jenkinsia job list
    ```

    Salida esperada:

    ```
    - mi_trabajo
    - otro_trabajo
    - trabajo_de_prueba
    ```

4.  **Crear un nuevo trabajo de tipo 'FreeStyleProject':**

    ```bash
    jenkinsia job create --job-name nuevo_trabajo --type FreeStyleProject --config config.xml
    ```
    Donde `config.xml` contiene la configuración XML del trabajo.

    Salida esperada:

    ```
    Trabajo 'nuevo_trabajo' creado con éxito.
    ```

5.  **Eliminar un trabajo existente:**

    ```bash
    jenkinsia job delete --job-name trabajo_a_eliminar
    ```

    Salida esperada:

    ```
    Trabajo 'trabajo_a_eliminar' eliminado con éxito.
    ```

## Configuración

Jenkinsia se configura a través de un archivo `config.yaml`.  Las variables de entorno importantes son:

*   `JENKINS_URL`: La URL del servidor Jenkins.
*   `JENKINS_USERNAME`: El nombre de usuario de Jenkins.
*   `JENKINS_PASSWORD`: La contraseña del usuario de Jenkins.
*   `JENKINS_TOKEN`: El token de API de Jenkins (alternativo a usuario/contraseña).

Puedes encontrar más detalles sobre la configuración en la documentación.

## Troubleshooting Común

1.  **Error de autenticación:**

    *   Causa: Credenciales incorrectas en `config.yaml`.
    *   Solución: Verifica que el nombre de usuario y la contraseña sean correctos.  Si utilizas un token, asegúrate de que sea válido.
    *   Comando de diagnóstico: `jenkinsia job list` (debería devolver un error de autenticación).

2.  **Error de conexión:**

    *   Causa: El servidor Jenkins no está accesible.
    *   Solución: Verifica que la URL del servidor Jenkins sea correcta y que el servidor esté en ejecución.
    *   Comando de diagnóstico: `ping tu-servidor-jenkins`

3.  **Error de permiso:**

    *   Causa: El usuario no tiene permisos suficientes para realizar la acción.
    *   Solución: Asigna los permisos necesarios al usuario en Jenkins.
    *   Comando de diagnóstico: Verifica los logs de Jenkins para ver los errores de permiso.

## Contribuciones

Si encuentras un bug, por favor, repórtalo a través de los [issues](https://github.com/serrano1004/jenkinsia/issues) en GitHub.  Si tienes alguna sugerencia para mejorar Jenkinsia, puedes proponerla a través de los mismos issues.  Para contribuir con código, consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md).  Por favor, sigue el [código de conducta](CODE_OF_CONDUCT.md) al contribuir.

## Licencia y Créditos

Jenkinsia está licenciado bajo la [Licencia MIT](LICENSE).  Agradecemos a la comunidad de Python y a los desarrolladores de Jenkins por su trabajo.  Jenkinsia se inspira en otras herramientas de automatización y gestión de Jenkins.

## Contacto y Soporte

Para cualquier pregunta o problema, puedes contactarnos a través de:

*   Email: [tu_email@example.com](mailto:tu_email@example.com)
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [Enlace a la documentación]
*   Community links: [Enlace a la comunidad]
```