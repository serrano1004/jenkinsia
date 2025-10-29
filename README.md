```markdown
# jenkinsia

Una aplicación Python para automatizar tareas de Jenkins.

[![CI/CD Status](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml/badge.svg)](https://github.com/serrano1004/jenkinsia/actions/workflows/main.yml)
![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Project Status](https://img.shields.io/badge/status-active-success.svg)

## Descripción General

Jenkinsia es una aplicación Python diseñada para simplificar y automatizar interacciones con servidores Jenkins.  Esta herramienta permite a los usuarios gestionar trabajos, obtener información de builds y realizar otras tareas comunes de Jenkins de manera programática y eficiente.

El proyecto surge de la necesidad de automatizar tareas repetitivas en Jenkins, como el despliegue de aplicaciones, la ejecución de pruebas y la monitorización de builds.  A menudo, estas tareas se realizan manualmente a través de la interfaz web de Jenkins, lo que puede ser tedioso y propenso a errores. Jenkinsia proporciona una interfaz de línea de comandos (CLI) y una API Python para automatizar estas tareas, ahorrando tiempo y reduciendo errores.

Jenkinsia resuelve el problema de la gestión manual de Jenkins al proporcionar una herramienta automatizada y programable.  Esto permite a los usuarios integrar Jenkins con otros sistemas y flujos de trabajo, creando así una solución de automatización más completa. Está dirigida a desarrolladores, ingenieros de DevOps y administradores de sistemas que utilizan Jenkins para la integración continua y la entrega continua (CI/CD).

## Características Clave

*   🚀 **Gestión de trabajos:** Crea, actualiza y elimina trabajos de Jenkins de forma programática.
*   📊 **Monitorización de builds:** Obtén información detallada sobre el estado de los builds, incluyendo logs y resultados de pruebas.
*   ⚙️ **Automatización de despliegues:**  Despliega aplicaciones automáticamente en diferentes entornos.
*   🔑 **Gestión de credenciales:**  Almacena y gestiona credenciales de forma segura para acceder a Jenkins.
*   🔗 **Integración con otros sistemas:**  Integra Jenkins con otras herramientas y sistemas mediante la API Python.

## Requisitos Previos

*   **Sistema Operativo:**  Compatible con Linux, macOS y Windows.
*   **Python:**  Versión 3.6 o superior.
*   **Jenkins:**  Un servidor Jenkins en ejecución y accesible.
*   **pip:**  El gestor de paquetes de Python.
*   **Librerías Python:**  `requests`, `python-jenkins`.

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

El siguiente ejemplo muestra cómo obtener información sobre un trabajo de Jenkins:

```python
import jenkins
import os

JENKINS_URL = os.environ.get('JENKINS_URL', 'http://localhost:8080')
JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'password')
JOB_NAME = 'mi-trabajo'

server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)

try:
    job_info = server.get_job_info(JOB_NAME)
    print(f"Información del trabajo '{JOB_NAME}':")
    print(f"  Descripción: {job_info['description']}")
    print(f"  URL: {job_info['url']}")
except jenkins.NotFoundException:
    print(f"El trabajo '{JOB_NAME}' no se encontró.")
except Exception as e:
    print(f"Error al obtener información del trabajo: {e}")
```

Este script se conecta al servidor Jenkins, obtiene información sobre el trabajo especificado y la imprime en la consola.  Si el trabajo no existe, se mostrará un mensaje de error.

## Arquitectura del Proyecto

```
+-------------------+     +-------------------+     +-------------------+
|  Cliente (Usuario | --> |  jenkinsia.py     | --> |  Servidor Jenkins |
|  o script)        |     |  (Lógica Python)  |     |  (API Jenkins)    |
+-------------------+     +-------------------+     +-------------------+
         |                    |                    |
         |                    |  - requests        |                    |
         |                    |  - python-jenkins  |                    |
         |                    |                    |
         |                    |  Lee config        |                    |
         |                    |  de .env o args   |                    |
         |                    +------------------->
```

El diagrama muestra el flujo de datos principal. El cliente (un usuario o un script) interactúa con `jenkinsia.py`, que contiene la lógica principal de la aplicación. `jenkinsia.py` utiliza las librerías `requests` y `python-jenkins` para comunicarse con el servidor Jenkins a través de su API. La configuración se lee desde variables de entorno o argumentos de línea de comandos.

Los componentes clave son:

*   **Cliente:** El usuario o script que utiliza Jenkinsia.
*   **jenkinsia.py:** El script principal de Python que implementa la lógica de la aplicación.
*   **Servidor Jenkins:** El servidor Jenkins que se gestiona.
*   **Librerías:** `requests` y `python-jenkins` para la comunicación con la API de Jenkins.

## Detalles Técnicos

Jenkinsia utiliza la librería `python-jenkins` para interactuar con la API REST de Jenkins.  Esta librería proporciona una interfaz Python para la mayoría de las funciones de la API de Jenkins, simplificando el desarrollo.

Se eligió `python-jenkins` debido a su facilidad de uso y su amplia cobertura de la API de Jenkins.  También se utiliza la librería `requests` para realizar solicitudes HTTP directas a la API de Jenkins en casos donde `python-jenkins` no proporciona una función específica.

Las decisiones arquitectónicas se centraron en la simplicidad y la facilidad de uso.  La aplicación se diseñó para ser fácil de instalar, configurar y utilizar.  También se hizo hincapié en la modularidad, para que sea fácil agregar nuevas funcionalidades en el futuro.

## Ejemplos de Uso

1.  **Crear un nuevo trabajo:**

    ```python
    import jenkins
    import os

    JENKINS_URL = os.environ.get('JENKINS_URL', 'http://localhost:8080')
    JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
    JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'password')
    JOB_NAME = 'nuevo-trabajo'
    JOB_CONFIG = """
    <?xml version='1.1' encoding='UTF-8'?>
    <project>
      <actions/>
      <description>Trabajo creado desde Jenkinsia</description>
      <keepDependencies>false</keepDependencies>
      <properties/>
      <scm class="hudson.scm.NullSCM"/>
      <canRoam>true</canRoam>
      <disabled>false</disabled>
      <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
      <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
      <triggers/>
      <concurrentBuild>false</concurrentBuild>
      <builders/>
      <publishers/>
      <buildWrappers/>
    </project>
    """

    server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)

    try:
        server.create_job(JOB_NAME, JOB_CONFIG)
        print(f"Trabajo '{JOB_NAME}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el trabajo: {e}")
    ```

    Este script crea un nuevo trabajo en Jenkins con la configuración especificada.

2.  **Obtener el estado de un build:**

    ```python
    import jenkins
    import os

    JENKINS_URL = os.environ.get('JENKINS_URL', 'http://localhost:8080')
    JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
    JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'password')
    JOB_NAME = 'mi-trabajo'
    BUILD_NUMBER = 1

    server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)

    try:
        build_info = server.get_build_info(JOB_NAME, BUILD_NUMBER)
        print(f"Estado del build #{BUILD_NUMBER} del trabajo '{JOB_NAME}':")
        print(f"  Resultado: {build_info['result']}")
        print(f"  URL: {build_info['url']}")
    except jenkins.NotFoundException:
        print(f"El build #{BUILD_NUMBER} del trabajo '{JOB_NAME}' no se encontró.")
    except Exception as e:
        print(f"Error al obtener información del build: {e}")
    ```

    Este script obtiene el estado de un build específico de un trabajo en Jenkins.

3.  **Disparar un build:**

    ```python
    import jenkins
    import os

    JENKINS_URL = os.environ.get('JENKINS_URL', 'http://localhost:8080')
    JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
    JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'password')
    JOB_NAME = 'mi-trabajo'

    server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)

    try:
        server.build_job(JOB_NAME)
        print(f"Build disparado para el trabajo '{JOB_NAME}'.")
    except Exception as e:
        print(f"Error al disparar el build: {e}")
    ```

    Este script dispara un nuevo build para un trabajo en Jenkins.

## Configuración

Las siguientes variables de entorno son importantes para configurar Jenkinsia:

*   `JENKINS_URL`: La URL del servidor Jenkins.  Valor por defecto: `http://localhost:8080`.
*   `JENKINS_USER`: El nombre de usuario para acceder a Jenkins.  Valor por defecto: `admin`.
*   `JENKINS_PASSWORD`: La contraseña o token API para acceder a Jenkins.  Valor por defecto: `password`.

Estas variables se pueden configurar en el archivo `.env` o como variables de entorno del sistema.

Para obtener más detalles sobre la configuración, consulta la documentación completa.

## Troubleshooting Común

1.  **Error de conexión:**

    *   **Causa probable:** El servidor Jenkins no está en ejecución o la URL es incorrecta.
    *   **Solución:** Verifica que el servidor Jenkins esté en ejecución y que la variable de entorno `JENKINS_URL` esté configurada correctamente.
    *   **Comando de diagnóstico:** `ping <JENKINS_URL>`

2.  **Error de autenticación:**

    *   **Causa probable:** El nombre de usuario o la contraseña son incorrectos.
    *   **Solución:** Verifica que las variables de entorno `JENKINS_USER` y `JENKINS_PASSWORD` estén configuradas correctamente. Asegúrate de que el usuario tenga los permisos necesarios en Jenkins.
    *   **Comando de diagnóstico:**  Verifica las credenciales en la interfaz web de Jenkins.

3.  **Trabajo no encontrado:**

    *   **Causa probable:** El trabajo especificado no existe en Jenkins.
    *   **Solución:** Verifica que el nombre del trabajo sea correcto y que el trabajo exista en Jenkins.
    *   **Comando de diagnóstico:**  Verifica la existencia del trabajo en la interfaz web de Jenkins.

## Contribuciones

Si encuentras un bug, por favor, repórtalo a través de las [issues](https://github.com/serrano1004/jenkinsia/issues) en GitHub. Si quieres sugerir una nueva característica, puedes abrir una nueva issue o enviar un pull request.

Consulta el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más información sobre cómo contribuir al proyecto.

Por favor, respeta el [Código de Conducta](CODE_OF_CONDUCT.md) al participar en el proyecto.

## Licencia y Créditos

Este proyecto está licenciado bajo la licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

Agradecimientos a la comunidad de Python y a los desarrolladores de las librerías `requests` y `python-jenkins`.

Inspirado en la necesidad de automatizar tareas repetitivas en Jenkins.

## Contacto y Soporte

*   Email de contacto: serrano1004@example.com
*   Issues en GitHub: [https://github.com/serrano1004/jenkinsia/issues](https://github.com/serrano1004/jenkinsia/issues)
*   Documentación adicional: [ENLACE A LA DOCUMENTACIÓN]
*   Community links: [ENLACE A LA COMUNIDAD]
```