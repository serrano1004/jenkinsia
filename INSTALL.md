```markdown
# Guía Completa de Instalación - jenkinsia

Esta guía te guiará a través del proceso de instalación de jenkinsia en los sistemas operativos Windows, macOS y Linux. Cubre todos los pasos necesarios, desde la instalación de los requisitos previos hasta la verificación de la instalación y la solución de problemas comunes.

**Tabla de Contenidos**

*   [Requisitos Previos Detallados](#requisitos-previos-detallados)
    *   [Windows](#windows)
    *   [macOS](#macos)
    *   [Linux](#linux)
*   [Instalación Paso a Paso](#instalación-paso-a-paso)
    *   [Paso 1: Clonar el Repositorio](#paso-1-clonar-el-repositorio)
    *   [Paso 2: Crear y Activar un Entorno Virtual (venv)](#paso-2-crear-y-activar-un-entorno-virtual-venv)
    *   [Paso 3: Instalar Dependencias](#paso-3-instalar-dependencias)
    *   [Paso 4: Configuración Inicial](#paso-4-configuración-inicial)
    *   [Paso 5: Verificación de Instalación](#paso-5-verificación-de-instalación)
*   [Tests de Verificación Completa](#tests-de-verificación-completa)
    *   [Test 1: Verificar la versión de Python](#test-1-verificar-la-versión-de-python)
    *   [Test 2: Verificar la instalación de las dependencias](#test-2-verificar-la-instalación-de-las-dependencias)
    *   [Test 3: Ejecutar un script de prueba básico](#test-3-ejecutar-un-script-de-prueba-básico)
*   [Configuración Avanzada](#configuración-avanzada)
    *   [5.1 Usar en Diferentes Ubicaciones](#51-usar-en-diferentes-ubicaciones)
    *   [5.2 Integración con IDEs](#52-integración-con-ides)
    *   [5.3 Entorno de Producción](#53-entorno-de-producción)
    *   [5.4 Usar con Docker](#54-usar-con-docker)
*   [🐛 Solución de Problemas](#🐛-solución-de-problemas)
    *   [Problema 1: Error de versión de Python](#problema-1-error-de-versión-de-python)
    *   [Problema 2: Permiso denegado al instalar paquetes](#problema-2-permiso-denegado-al-instalar-paquetes)
    *   [Problema 3: Módulo no encontrado (ModuleNotFoundError)](#problema-3-módulo-no-encontrado-modulenotfounderror)
    *   [Problema 4: Error al crear el entorno virtual](#problema-4-error-al-crear-el-entorno-virtual)
    *   [Problema 5: Problemas con pip](#problema-5-problemas-con-pip)
    *   [Problema 6: Problemas de dependencias cíclicas](#problema-6-problemas-de-dependencias-cíclicas)
*   [Configuración de Entorno Virtual](#configuración-de-entorno-virtual)
*   [Próximos Pasos Después de la Instalación](#próximos-pasos-después-de-la-instalación)
*   [Tips y Mejores Prácticas](#tips-y-mejores-prácticas)
*   [Soporte](#soporte)

## Requisitos Previos Detallados

A continuación, se detallan los requisitos previos para la instalación de jenkinsia en cada sistema operativo.

### Windows

a) **Requisitos de Sistema**

*   **Versión mínima del SO:** Windows 10
*   **RAM recomendada:** 4 GB
*   **Espacio en disco:** 200 MB
*   **Conexión a Internet:** Necesaria para descargar dependencias.

b) **Software Requerido**

*   **Python:**
    *   **Versión mínima requerida:** 3.8
    *   **Cómo instalar:**
        1.  Descargar el instalador desde [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
        2.  Ejecutar el instalador.
        3.  Asegurarse de marcar la casilla "Add Python to PATH" durante la instalación.
    *   **Comando de verificación:**
        ```bash
        python --version
        ```
    *   **Qué hacer si no está disponible:** Volver a ejecutar el instalador y asegurarse de marcar la casilla "Add Python to PATH". Si sigue sin funcionar, agregar manualmente la ruta de Python al PATH del sistema.

c) **Herramientas Opcionales**

*   **Visual Studio Code:** Un editor de código muy popular con excelente soporte para Python.
    *   **Para qué sirve:** Facilita la edición, depuración y gestión del código.
    *   **Cómo instalar:** Descargar desde [https://code.visualstudio.com/](https://code.visualstudio.com/) y seguir las instrucciones de instalación.
*   **Git:** Un sistema de control de versiones.
    *   **Para qué sirve:** Permite gestionar cambios en el código y colaborar con otros desarrolladores.
    *   **Cómo instalar:** Descargar desde [https://git-scm.com/downloads](https://git-scm.com/downloads) y seguir las instrucciones de instalación.

### macOS

a) **Requisitos de Sistema**

*   **Versión mínima del SO:** macOS 10.15 (Catalina)
*   **RAM recomendada:** 4 GB
*   **Espacio en disco:** 200 MB
*   **Conexión a Internet:** Necesaria para descargar dependencias.

b) **Software Requerido**

*   **Python:**
    *   **Versión mínima requerida:** 3.8
    *   **Cómo instalar:**
        1.  Utilizar Homebrew (recomendado):
            ```bash
            brew install python
            ```
        2.  Si no tienes Homebrew, puedes instalarlo desde [https://brew.sh/](https://brew.sh/).
    *   **Comando de verificación:**
        ```bash
        python3 --version
        ```
    *   **Qué hacer si no está disponible:** Instalar Homebrew si no lo tienes y luego usarlo para instalar Python.

c) **Herramientas Opcionales**

*   **Visual Studio Code:** Un editor de código muy popular con excelente soporte para Python.
    *   **Para qué sirve:** Facilita la edición, depuración y gestión del código.
    *   **Cómo instalar:** Descargar desde [https://code.visualstudio.com/](https://code.visualstudio.com/) y seguir las instrucciones de instalación.
*   **Git:** Un sistema de control de versiones.
    *   **Para qué sirve:** Permite gestionar cambios en el código y colaborar con otros desarrolladores.
    *   **Cómo instalar:** Generalmente viene preinstalado. Verificar con `git --version`. Si no está, instalar con `brew install git`.

### Linux

a) **Requisitos de Sistema**

*   **Versión mínima del SO:** Cualquier distribución Linux moderna (Ubuntu, Debian, Fedora, etc.)
*   **RAM recomendada:** 4 GB
*   **Espacio en disco:** 200 MB
*   **Conexión a Internet:** Necesaria para descargar dependencias.

b) **Software Requerido**

*   **Python:**
    *   **Versión mínima requerida:** 3.8
    *   **Cómo instalar:**
        *   **Ubuntu/Debian:**
            ```bash
            sudo apt update
            sudo apt install python3 python3-pip
            ```
        *   **Fedora:**
            ```bash
            sudo dnf install python3 python3-pip
            ```
    *   **Comando de verificación:**
        ```bash
        python3 --version
        ```
    *   **Qué hacer si no está disponible:** Utilizar el gestor de paquetes de tu distribución para instalar Python 3 y pip.

c) **Herramientas Opcionales**

*   **Visual Studio Code:** Un editor de código muy popular con excelente soporte para Python.
    *   **Para qué sirve:** Facilita la edición, depuración y gestión del código.
    *   **Cómo instalar:** Descargar desde [https://code.visualstudio.com/](https://code.visualstudio.com/) y seguir las instrucciones de instalación.
*   **Git:** Un sistema de control de versiones.
    *   **Para qué sirve:** Permite gestionar cambios en el código y colaborar con otros desarrolladores.
    *   **Cómo instalar:**
        *   **Ubuntu/Debian:** `sudo apt install git`
        *   **Fedora:** `sudo dnf install git`

## Instalación Paso a Paso

Sigue estos pasos para instalar jenkinsia en tu sistema.

### Paso 1: Clonar el Repositorio

Clona el repositorio de jenkinsia desde GitHub.

```bash
git clone https://github.com/serrano1004/jenkinsia.git
cd jenkinsia
```

**Qué esperar:** Se descargará el código fuente del proyecto a tu máquina.

**Cómo verificar éxito:** Comprueba que la carpeta `jenkinsia` se ha creado y contiene los archivos del proyecto.

### Paso 2: Crear y Activar un Entorno Virtual (venv)

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.

```bash
python3 -m venv venv
```

*   **Windows:**
    ```bash
    venv\Scripts\activate
    ```
*   **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

**Qué esperar:** Se creará una carpeta llamada `venv` que contendrá el entorno virtual. El prompt de tu terminal cambiará para indicar que el entorno virtual está activado (por ejemplo, `(venv) $`).

**Cómo verificar éxito:** El prompt de tu terminal debe mostrar el nombre del entorno virtual entre paréntesis.

### Paso 3: Instalar Dependencias

Instala las dependencias del proyecto utilizando `pip`.

```bash
pip install -r requirements.txt
```

**Tiempo estimado:** Depende de la velocidad de tu conexión a Internet y la cantidad de dependencias.

**Qué hace:** Descarga e instala todas las librerías y paquetes listados en el archivo `requirements.txt`.

### Paso 4: Configuración Inicial

Dependiendo de la estructura del proyecto, este paso puede variar. En este ejemplo genérico, asumimos que no hay una configuración inicial compleja. Si jenkinsia requiere variables de entorno o archivos de configuración, este es el lugar para definirlos.

Por ejemplo, si requiriera una variable de entorno `API_KEY`:

```bash
export API_KEY="tu_api_key" # macOS/Linux
set API_KEY="tu_api_key" # Windows
```

### Paso 5: Verificación de Instalación

Verifica que la instalación se ha completado correctamente ejecutando un comando básico del proyecto (si existe). Asumimos que jenkinsia tiene un script principal llamado `main.py`.

```bash
python main.py --version # o algún comando similar específico del proyecto
```

**Salida esperada:** Debería mostrar la versión del proyecto o un mensaje de confirmación de que la instalación es correcta.

**Qué hacer si falla:** Revisar los pasos anteriores, especialmente la instalación de dependencias y la configuración del entorno virtual. Consultar la sección de solución de problemas.

## Tests de Verificación Completa

Estos tests verifican la correcta instalación y funcionamiento de jenkinsia.

### Test 1: Verificar la versión de Python

Verifica que la versión de Python utilizada es la correcta.

```bash
python3 --version
```

**Qué debería mostrar:** Una versión igual o superior a 3.8.

**Qué hacer si falla:** Asegurarse de que Python 3.8 o superior está instalado y que está en el PATH del sistema.

### Test 2: Verificar la instalación de las dependencias

Verifica que todas las dependencias listadas en `requirements.txt` están instaladas.  Un script simple en Python puede ayudar:

```python
# verify_dependencies.py
import importlib

with open("requirements.txt", "r") as f:
    dependencies = [line.strip() for line in f if line.strip()]

missing_dependencies = []
for dep in dependencies:
    try:
        # Extraer el nombre del paquete del string (ej: requests==2.28.1 -> requests)
        package_name = dep.split("==")[0] if "==" in dep else dep
        importlib.import_module(package_name)
    except ImportError:
        missing_dependencies.append(dep)

if missing_dependencies:
    print("Las siguientes dependencias no están instaladas:")
    for dep in missing_dependencies:
        print(f"- {dep}")
else:
    print("Todas las dependencias están instaladas correctamente.")
```

Ejecutar:

```bash
python verify_dependencies.py
```

**Qué debería mostrar:** "Todas las dependencias están instaladas correctamente." o una lista de las dependencias faltantes.

**Qué hacer si falla:**  Re-ejecutar `pip install -r requirements.txt`. Si persisten los problemas, revisar la sección de solución de problemas.

### Test 3: Ejecutar un script de prueba básico

Si jenkinsia incluye scripts de prueba, ejecutarlos para asegurar que todo funciona correctamente.  Este paso es altamente dependiente de la estructura del proyecto.  Asumimos que existe una carpeta "tests" con un script llamado "test_basic.py".

```bash
python -m unittest tests/test_basic.py
```

**Qué debería mostrar:** Un reporte de las pruebas ejecutadas y si pasaron o fallaron.

**Qué hacer si falla:** Analizar los errores reportados por las pruebas y corregir cualquier problema en la instalación o configuración.

## Configuración Avanzada

### 5.1 Usar en Diferentes Ubicaciones

Para acceder a `jenkinsia` desde cualquier ubicación en tu sistema, puedes agregar su directorio al PATH del sistema.

*   **Windows:**
    1.  Buscar "Editar las variables de entorno del sistema" en el menú de inicio.
    2.  Hacer clic en "Variables de entorno".
    3.  Seleccionar la variable "Path" y hacer clic en "Editar".
    4.  Agregar la ruta al directorio de `jenkinsia` (ejemplo: `C:\Users\tu_usuario\jenkinsia`).
*   **macOS/Linux:**
    1.  Editar el archivo `~/.bashrc` o `~/.zshrc` (dependiendo de tu shell).
    2.  Agregar la siguiente línea:
        ```bash
        export PATH="$PATH:/ruta/a/jenkinsia"
        ```
    3.  Ejecutar `source ~/.bashrc` o `source ~/.zshrc` para aplicar los cambios.

### 5.2 Integración con IDEs

*   **Visual Studio Code:**
    *   **Extensiones recomendadas:** Python, Pylance.
    *   **Configuración en settings.json:**
        ```json
        {
            "python.pythonPath": "/ruta/a/venv/bin/python",
            "python.linting.pylintEnabled": true
        }
        ```
    *   **Debug setup:** Crear un archivo `launch.json` para configurar la depuración.
*   **PyCharm / WebStorm:**
    *   **Interpreter/SDK configuration:** Configurar el intérprete de Python para que apunte al entorno virtual.
    *   **Run configurations:** Crear configuraciones de ejecución para ejecutar y depurar el código.

### 5.3 Entorno de Producción

El entorno de producción requiere una configuración más robusta y segura.

*   **Diferencias con desarrollo:** No usar el servidor de desarrollo.  Usar un servidor web como Gunicorn o uWSGI.
*   **Checklist de configuración:**
    *   Configurar un servidor web.
    *   Configurar un proceso manager (ej: systemd, Supervisor).
    *   Configurar un servidor de base de datos (si aplica).
    *   Configurar un firewall.
    *   Configurar un sistema de logging.
*   **Consideraciones de seguridad:**
    *   Usar HTTPS.
    *   Configurar contraseñas seguras.
    *   Limitar el acceso a los recursos.
    *   Monitorear la seguridad del sistema.

### 5.4 Usar con Docker

Si el proyecto es compatible con Docker, puedes usar un `Dockerfile` para construir una imagen y ejecutar jenkinsia en un contenedor.

```dockerfile
# Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

```bash
docker build -t jenkinsia .
docker run -it jenkinsia
```

## 🐛 Solución de Problemas

Aquí hay algunos problemas comunes que puedes encontrar durante la instalación y sus soluciones.

#### Problema 1: Error de versión de Python

a) **Problema:** El sistema utiliza una versión de Python diferente a la requerida (3.8 o