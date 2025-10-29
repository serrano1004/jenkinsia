```markdown
# jenkinsia [![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)  [![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/serrano1004/jenkinsia)

Una aplicación Python simple para automatizar tareas de Jenkins.

## Descripción General

Jenkinsia es una aplicación Python diseñada para interactuar con un servidor Jenkins, automatizando tareas comunes y simplificando la gestión de pipelines.  Esta herramienta busca facilitar la vida de los desarrolladores y administradores de sistemas que trabajan con Jenkins, proporcionando una interfaz más accesible y automatizada para realizar operaciones repetitivas.

El proyecto nace de la necesidad de tener una herramienta que permita interactuar con Jenkins desde la línea de comandos o scripts, sin tener que depender de la interfaz web o APIs complejas.  Se enfoca en ofrecer una solución sencilla y eficiente para la gestión de trabajos, la obtención de información sobre el estado de las construcciones y la ejecución de pipelines.

Jenkinsia resuelve el problema de la complejidad inherente a la gestión de Jenkins a través de su interfaz web o APIs.  Permite a los usuarios automatizar tareas como el lanzamiento de trabajos, la verificación de estados y la obtención de logs, todo ello desde la comodidad de la línea de comandos.  Está dirigida a desarrolladores, administradores de sistemas, ingenieros de DevOps y cualquier persona que trabaje con Jenkins y busque una forma más eficiente de interactuar con él.

## Características Clave

*   🚀 **Lanzamiento de Trabajos:** Inicia trabajos de Jenkins con un simple comando.
*   📊 **Monitorización de Construcciones:** Obtén el estado actual de cualquier construcción en tiempo real.
*   📜 **Obtención de Logs:** Descarga los logs de las construcciones para su análisis.
*   ⚙️ **Gestión de Pipelines:** Automatiza la ejecución y el seguimiento de pipelines complejos.
*   🔒 **Autenticación Segura:** Utiliza credenciales para acceder a tu servidor Jenkins de forma segura.

## Requisitos Previos

Para utilizar Jenkinsia, necesitas lo siguiente:

*   **Sistema Operativo:** Compatible con cualquier sistema operativo que soporte Python (Windows, Linux, macOS).
*   **Python:** Versión 3.7 o superior.
*   **Pip:** El gestor de paquetes de Python (generalmente incluido con Python).
*   **Servidor Jenkins:** Acceso a un servidor Jenkins en ejecución.
*   **Credenciales de Jenkins:** Un usuario con los permisos necesarios para interactuar con el servidor Jenkins.

## Instalación Rápida

Sigue estos sencillos pasos para instalar Jenkinsia:

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
    pip install -r requirements.txt
    ```
4.  **Verifica la instalación:**
    ```bash
    python jenkinsia.py --version
    ```

Para una instalación más detallada, consulta el archivo [INSTALL.md](INSTALL.md).

## Guía Rápida de Uso

Aquí tienes un ejemplo básico de cómo utilizar Jenkinsia para lanzar un trabajo:

1.  **Configura las variables de entorno:**
    ```bash
    export JENKINS_URL="http://tu-servidor-jenkins:8080"
    export JENKINS_USER="tu_usuario"
    export JENKINS_PASSWORD="tu_contraseña"
    ```
2.  **Ejecuta el script para lanzar un trabajo:**
    ```bash
    python jenkinsia.py --job "nombre-del-trabajo" --action build
    ```

    Salida esperada:
    ```
    Iniciando la construcción del trabajo 'nombre-del-trabajo'...
    Construcción iniciada con éxito.
    ```

Este es un caso de uso común para lanzar trabajos automáticamente desde scripts o cron jobs.

## Arquitectura del Proyecto

```
+---------------------+     +---------------------+     +---------------------+
|   Línea de Comandos  | --> |     jenkinsia.py    | --> |   Servidor Jenkins  |
+---------------------+     +---------------------+     +---------------------+
         |                      |          |                      |         |
         | Parámetros del usuario |          |  Lógica principal  |         |  API REST
         |                      |          |                      |         |
         v                      v          v                      v         v
+---------------------+     +---------------------+     +---------------------+
|   Entrada del Usuario |     |  Procesamiento Python|     |  Respuesta de Jenkins|
+---------------------+     +---------------------+     +---------------------+
```

*   **Línea de Comandos:**  La interfaz principal donde el usuario interactúa con la aplicación.
*   **`jenkinsia.py`:** El script principal de Python que procesa los comandos del usuario, se autentica con el servidor Jenkins y realiza las acciones solicitadas.
*   **Servidor Jenkins:** El sistema de integración continua que recibe las solicitudes y ejecuta los trabajos.

El flujo de datos principal es el siguiente: el usuario introduce un comando en la línea de comandos, `jenkinsia.py` procesa este comando y lo traduce en una solicitud a la API REST de Jenkins, y finalmente, el servidor Jenkins responde con el resultado de la operación.

## Detalles Técnicos

Jenkinsia utiliza la biblioteca `requests` de Python para interactuar con la API REST de Jenkins. La decisión de utilizar `requests` se basa en su simplicidad, flexibilidad y amplia documentación.  El script principal (`jenkinsia.py`) analiza los argumentos de la línea de comandos utilizando el módulo `argparse` de Python.

Se ha optado por una arquitectura modular para facilitar la extensión y el mantenimiento del código.  Las funciones relacionadas con la autenticación, la gestión de trabajos y la obtención de información se han separado en módulos independientes.

El rendimiento no es un requisito crítico para esta aplicación, ya que se espera que se utilice para automatizar tareas que no requieren una respuesta inmediata. Sin embargo, se han tomado medidas para optimizar el rendimiento, como el uso de sesiones HTTP persistentes para reducir la sobrecarga de la autenticación.

## Ejemplos de Uso

Aquí tienes algunos ejemplos de cómo puedes utilizar Jenkinsia:

1.  **Lanzar un trabajo con parámetros:**

    ```bash
    python jenkinsia.py --job "mi-trabajo" --action build --params "param1=valor1,param2=valor2"
    ```

    Salida esperada:

    ```
    Iniciando la construcción del trabajo 'mi-trabajo' con los parámetros: param1=valor1, param2=valor2
    Construcción iniciada con éxito.
    ```

2.  **Obtener el estado de la última construcción:**

    ```bash
    python jenkinsia.py --job "mi-trabajo" --action status
    ```

    Salida esperada:

    ```
    El estado de la última construcción del trabajo 'mi-trabajo' es: SUCCESS
    ```

3.  **Descargar los logs de una construcción específica:**

    ```bash
    python jenkinsia.py --job "mi-trabajo" --action logs --build 123 > build_123.log
    ```

    Esto guardará los logs de la construcción número 123 en el archivo `build_123.log`.

## Configuración

Jenkinsia se configura principalmente a través de variables de entorno:

*   `JENKINS_URL`: La URL del servidor Jenkins (ej: `http://localhost:8080`).
*   `JENKINS_USER`: El nombre de usuario para autenticarse en Jenkins.
*   `JENKINS_PASSWORD`: La contraseña o el token de API para autenticarse en Jenkins.

Puedes configurar estas variables de entorno en tu shell o en un archivo `.env`. Para más detalles, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de autenticación:**

    *   Causa probable: Credenciales incorrectas.
    *   Solución: Verifica que las variables de entorno `JENKINS_USER` y `JENKINS_PASSWORD` estén configuradas correctamente. Asegúrate de que el usuario tenga los permisos necesarios en Jenkins.
    *   Comando de diagnóstico: Verifica las credenciales directamente en la interfaz web de Jenkins.

2.  **Error al conectar con el servidor Jenkins:**

    *   Causa probable: La URL del servidor Jenkins es incorrecta o el servidor no está accesible.
    *   Solución: Verifica que la variable de entorno `JENKINS_URL` esté configurada correctamente y que el servidor Jenkins esté en ejecución y accesible desde tu máquina.
    *   Comando de diagnóstico: Intenta acceder a la URL del servidor Jenkins desde tu navegador.

3.  **Error al lanzar un trabajo:**

    *   Causa probable: El trabajo no existe o el usuario no tiene permisos para lanzarlo.
    *   Solución: Verifica que el nombre del trabajo sea correcto y que el usuario tenga los permisos necesarios para lanzarlo en Jenkins.
    *   Comando de diagnóstico: Verifica la existencia del trabajo y los permisos del usuario en la interfaz web de Jenkins.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un bug, tienes una sugerencia de mejora o quieres añadir una nueva característica, por favor, sigue estos pasos:

1.  Reporta el bug o sugiere la mejora creando un nuevo "issue" en GitHub.
2.  Si quieres contribuir con código, crea un "fork" del repositorio, realiza tus cambios y envía un "pull request".

Consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más detalles sobre cómo contribuir.  Por favor, revisa nuestro código de conducta antes de contribuir.

## Licencia y Créditos

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

Agradecimientos especiales a la comunidad de Python y a los desarrolladores de la biblioteca `requests`.

## Contacto y Soporte

Si tienes alguna pregunta o necesitas ayuda, puedes contactarnos a través de:

*   Email: [tu_email@example.com](mailto:tu_email@example.com)
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)

Documentación adicional disponible en [https://github.com/serrano1004/jenkinsia](https://github.com/serrano1004/jenkinsia).
```
