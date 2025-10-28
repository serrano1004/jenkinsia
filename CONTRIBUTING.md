```markdown
# ¡Bienvenido/a al proyecto {project_name}! 👋

¡Gracias por tu interés en contribuir! Este proyecto es de todos y cada aporte, por pequeño que sea, es valiosísimo. Ya sea corrigiendo errores, mejorando la documentación o añadiendo nuevas funcionalidades, ¡tu ayuda es bienvenida! Si no sabes por dónde empezar, echa un vistazo a la sección de "Formas de Contribuir".

## Código de Conducta

Nuestro proyecto se basa en el respeto y la inclusión. Nos comprometemos a proporcionar un entorno amigable y seguro para todos los contribuidores, independientemente de su origen, género, identidad de género, orientación sexual, habilidades, etnia, religión, nivel de experiencia o cualquier otra característica.

Esperamos que todos los participantes sean considerados y respetuosos en sus interacciones. No toleraremos ninguna forma de acoso, discriminación o comportamiento ofensivo.

Si presencias o experimentas alguna violación de este código de conducta, por favor, repórtalo a [email protected] (reemplaza con el email real del mantenedor). Todas las denuncias serán investigadas y se tomarán las medidas apropiadas.

## Formas de Contribuir

Hay muchas formas de contribuir al proyecto {project_name}:

*   **Reportar Bugs:** Ayuda a identificar y corregir errores en el código.
*   **Sugerir Features:** Propón nuevas funcionalidades para mejorar el proyecto.
*   **Mejorar la Documentación:** Haz que la documentación sea más clara, completa y accesible.
*   **Escribir Tests:** Asegura la calidad del código con pruebas automatizadas.
*   **Responder Preguntas en Issues:** Ayuda a otros usuarios resolviendo sus dudas.
*   **Mantener Traducciones:** Contribuye a que el proyecto sea accesible a un público más amplio traduciendo la documentación y la interfaz.

## Reportar Bugs

Cuando reportes un bug, por favor, incluye la siguiente información:

*   **Descripción del problema:** Explica claramente qué sucedió y qué esperabas que sucediera.
*   **Pasos para reproducir el bug:** Proporciona instrucciones detalladas para que podamos reproducir el bug en nuestro entorno.
*   **Entorno:** Indica el sistema operativo, la versión del lenguaje de programación y cualquier otra información relevante.
*   **Código de error (si aplica):** Incluye el código de error completo.

Puedes reportar bugs creando un nuevo issue en el repositorio: [issues page]({repository_url}/issues)

```markdown
## Bug Report

**Descripción del problema:**

[Describe el problema aquí]

**Pasos para reproducir:**

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

**Entorno:**

*   Sistema Operativo: [Ejemplo: Windows 10]
*   Versión de {tech_stack}: [Ejemplo: Python 3.9]

**Código de error (si aplica):**

```
[Pega el código de error aquí]
```
```

## Sugerir Features

Cuando sugieras una nueva feature, por favor, incluye la siguiente información:

*   **Descripción de la feature:** Explica claramente qué hace la nueva feature.
*   **Caso de uso:** Describe cómo se utilizaría la nueva feature.
*   **Ejemplos:** Proporciona ejemplos concretos de cómo funcionaría la nueva feature.

Puedes sugerir features creando un nuevo issue en el repositorio: [issues page]({repository_url}/issues)

```markdown
## Feature Request

**Descripción de la feature:**

[Describe la feature aquí]

**Caso de uso:**

[Describe cómo se utilizaría la feature]

**Ejemplos:**

[Proporciona ejemplos concretos de cómo funcionaría la feature]
```

## Configuración de Desarrollo

Para contribuir al proyecto, necesitarás configurar un entorno de desarrollo local.

1.  **Fork el repositorio:** Haz clic en el botón "Fork" en la parte superior derecha de la página del repositorio en GitHub.
2.  **Clona tu fork:** Clona el repositorio a tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/{project_name}.git
    cd {project_name}
    ```
3.  **Instala las dependencias de desarrollo:** Dependiendo del stack tecnológico, el proceso varía.  Aquí hay ejemplos:

    *   **Python:**

        ```bash
        python -m venv .venv
        source .venv/bin/activate  # En Linux/macOS
        .venv/Scripts/activate  # En Windows
        pip install -r requirements-dev.txt # o requirements.txt si no hay un archivo separado para dev
        ```

    *   **JavaScript/TypeScript (con npm):**

        ```bash
        npm install
        ```

    *   **JavaScript/TypeScript (con yarn):**

        ```bash
        yarn install
        ```

4.  **Corre los tests localmente:** (Ver sección "Testing" para más detalles)
5.  **Herramientas recomendadas:** Recomendamos utilizar un IDE como VS Code, PyCharm o IntelliJ IDEA. VS Code ofrece excelentes extensiones para {tech_stack}.

## Flujo de Trabajo: Fork → Branch → PR

El flujo de trabajo recomendado para contribuir es el siguiente:

1.  **Fork el repositorio** (ya hecho en la sección anterior).
2.  **Clona tu fork** (ya hecho en la sección anterior).
3.  **Crea una rama con un nombre descriptivo:**

    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```

    o

    ```bash
    git checkout -b fix/correccion-de-bug
    ```
4.  **Haz tus cambios:** Implementa la nueva funcionalidad o corrige el bug.
5.  **Haz commits con mensajes claros:** (Ver sección "Commits y Mensajes" para más detalles)

    ```bash
    git add .
    git commit -m "feat: Agrega nueva funcionalidad"
    ```
6.  **Sube tu rama a tu fork:**

    ```bash
    git push origin feature/nueva-funcionalidad
    ```
7.  **Crea un Pull Request:** Ve a la página de tu fork en GitHub y haz clic en el botón "Compare & pull request".
8.  **Responde a las revisiones:** Atiende el feedback de los revisores y realiza los cambios necesarios.
9.  **Merge:** Una vez que el Pull Request sea aprobado, será mergeado a la rama principal.

## Guía de Estilo de Código

Para mantener la consistencia del código, te pedimos que sigas las siguientes guías de estilo:

*   **Python:**
    *   Sigue las convenciones de PEP 8: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
    *   Utiliza type hints para mejorar la legibilidad del código.
    *   Escribe docstrings para documentar las funciones y clases.

    ```python
    # Ejemplo de código bueno
    def suma(a: int, b: int) -> int:
        """
        Suma dos números enteros.

        Args:
            a: El primer número.
            b: El segundo número.

        Returns:
            La suma de a y b.
        """
        return a + b

    # Ejemplo de código malo
    def suma(a, b):
        return a+b
    ```

*   **JavaScript/TypeScript:**
    *   Utiliza ESLint con la configuración del proyecto para linting.
    *   Utiliza Prettier para formatear el código.
    *   Sigue las convenciones de nomenclatura del proyecto.

    ```javascript
    // Ejemplo de código bueno
    const nombreUsuario = "Juan Pérez"; // camelCase

    // Ejemplo de código malo
    const NombreUsuario = "Juan Pérez"; // PascalCase
    ```

*   **Otros lenguajes:** Sigue las convenciones del lenguaje y las guías de estilo específicas del proyecto.

## Testing

Utilizamos [pytest (reemplaza si usas otro)] como framework de testing.

Para correr los tests, ejecuta el siguiente comando:

```bash
pytest
```

Esperamos que el código tenga una cobertura de al menos el 80%.

Para escribir tests, sigue los siguientes ejemplos:

```python
# Ejemplo de test en Python (pytest)
def test_suma():
    assert suma(2, 3) == 5
```

## Commits y Mensajes

Utilizamos Conventional Commits: [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)

Los tipos de commits más comunes son:

*   `feat`: Agrega una nueva funcionalidad.
*   `fix`: Corrige un bug.
*   `docs`: Cambios en la documentación.
*   `style`: Cambios en el estilo del código (sin afectar la funcionalidad).
*   `refactor`: Refactorización del código (sin afectar la funcionalidad).
*   `test`: Agrega o modifica tests.
*   `chore`: Tareas de mantenimiento.

Ejemplos de mensajes de commit:

*   `feat: Agrega soporte para múltiples idiomas`
*   `fix: Corrige error al guardar datos`
*   `docs: Actualiza la documentación de la API`

Es importante hacer commits atómicos, es decir, que cada commit represente un cambio lógico y completo. Esto facilita la revisión del código y la resolución de problemas.

## Pull Request Process

Antes de crear un Pull Request, asegúrate de:

*   Estar actualizado con la rama {main_branch} (main/master):

    ```bash
    git fetch origin {main_branch}
    git rebase origin/{main_branch}
    ```
*   Incluir una descripción clara del cambio que estás proponiendo.
*   Referenciar los issues relacionados.
*   Responder al feedback de los revisores.
*   Ser paciente con el proceso de revisión.

Tips para un Pull Request exitoso:

*   Escribe código limpio y legible.
*   Asegúrate de que los tests pasen.
*   Sigue las guías de estilo del código.
*   Escribe mensajes de commit claros y descriptivos.

## Revisión de Código

Los revisores buscarán lo siguiente:

*   Que el código sea correcto y funcional.
*   Que el código sea legible y fácil de entender.
*   Que el código siga las guías de estilo del proyecto.
*   Que los tests pasen.
*   Que la documentación esté actualizada.

Recibe el feedback de los revisores con una mentalidad abierta y constructiva. Utiliza el feedback para mejorar tu código y aprender nuevas técnicas.

## Documentación

Documenta tus cambios en el código utilizando docstrings y comentarios. Actualiza la documentación del proyecto (README, etc.) si es necesario.

```python
# Ejemplo de docstring
def saludar(nombre: str) -> str:
    """
    Saluda a una persona.

    Args:
        nombre: El nombre de la persona.

    Returns:
        Un saludo personalizado.
    """
    return f"Hola, {nombre}!"
```

## Reconocimiento

Valoramos mucho las contribuciones de la comunidad. Reconoceremos a los contribuidores de las siguientes maneras:

*   Mencionándolos en las notas de la versión.
*   Añadiéndolos a la lista de contribuidores en el README.

Lista de contribuidores: [Enlace a la lista de contribuidores (si existe)]

## Contacto y Preguntas

Si tienes alguna pregunta o necesitas ayuda, puedes contactarnos a través de:

*   Email: [email protected] (reemplaza con el email real del mantenedor)
*   Discord/Slack community: [Enlace a la comunidad]
*   Discussions en GitHub: [Enlace a las discussions]

¡Gracias nuevamente por tu interés en contribuir!
```