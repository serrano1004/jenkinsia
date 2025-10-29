```markdown
# ¡Contribuye a {project_name}!

¡Bienvenido/a! Nos entusiasma que estés interesado/a en contribuir a {project_name}, un proyecto {tech_stack} dedicado a [breve descripción del proyecto]. Tu ayuda es fundamental para mejorar este proyecto para todos. ¡No importa si es corrigiendo errores, mejorando la documentación o añadiendo nuevas funcionalidades, tu contribución es valiosa!

## Código de Conducta

Nuestro objetivo es crear una comunidad abierta, inclusiva y respetuosa. Todos los contribuyentes, colaboradores y usuarios están obligados a adherirse a los siguientes valores:

*   **Respeto:** Trata a los demás con cortesía, empatía y consideración.
*   **Inclusión:** Aceptamos y valoramos las diferencias individuales.
*   **Colaboración:** Trabajamos juntos de manera constructiva para alcanzar nuestros objetivos comunes.

No toleramos ningún tipo de acoso, discriminación o comportamiento irrespetuoso. Si presencias o experimentas una violación de este código de conducta, por favor, repórtalo a [email del mantenedor].

## Formas de Contribuir

Hay muchas maneras de contribuir a {project_name}:

*   **Reportar Bugs:** Ayúdanos a identificar y solucionar errores.
*   **Sugerir Features:** Comparte tus ideas para mejorar el proyecto.
*   **Mejorar la Documentación:** Haz que el proyecto sea más accesible para todos.
*   **Escribir Tests:** Asegúrate de que el código funcione correctamente.
*   **Responder Preguntas en Issues:** Ayuda a otros usuarios a resolver sus problemas.
*   **Mantener Traducciones:** Haz que el proyecto esté disponible en más idiomas.

## Reportar Bugs

Para reportar un bug, sigue estos pasos:

1.  **Verifica si el bug ya ha sido reportado:** Busca en los issues existentes para evitar duplicados.
2.  **Describe el bug con detalle:** Incluye los pasos para reproducirlo, el comportamiento esperado y el comportamiento real.
3.  **Especifica el entorno:** Indica el sistema operativo, la versión de {project_name} y cualquier otra información relevante.

Utiliza el siguiente template para reportar bugs:

```markdown
## Bug Report

**Descripción:** [Describe el bug]

**Pasos para reproducir:**
1.  [Paso 1]
2.  [Paso 2]
3.  [Paso 3]

**Comportamiento esperado:** [Describe el comportamiento esperado]

**Comportamiento real:** [Describe el comportamiento real]

**Entorno:**
*   Sistema Operativo: [Ejemplo: Windows 10]
*   Versión de {project_name}: [Ejemplo: 1.2.3]
*   Otros: [Cualquier otra información relevante]
```

Reporta los bugs en la sección de [issues](link a la sección de issues del repo).

## Sugerir Features

Para sugerir una nueva funcionalidad, sigue estos pasos:

1.  **Describe la feature con detalle:** Explica qué hace la feature, por qué es útil y cómo se usaría.
2.  **Proporciona un caso de uso:** Describe un escenario en el que la feature sería beneficiosa.
3.  **Incluye ejemplos:** Muestra cómo se podría implementar la feature.

Utiliza el siguiente template para sugerir features:

```markdown
## Feature Request

**Descripción:** [Describe la feature]

**Caso de uso:** [Describe un escenario en el que la feature sería beneficiosa]

**Ejemplos:** [Muestra cómo se podría implementar la feature]
```

Abre un nuevo issue en la sección de [issues](link a la sección de issues del repo) con tu propuesta de feature.

## Configuración de Desarrollo

Para empezar a contribuir, sigue estos pasos:

1.  **Fork el repositorio:** Haz clic en el botón "Fork" en la esquina superior derecha de la página del repositorio.
2.  **Clona tu fork:**

    ```bash
    git clone [URL de tu fork]
    cd {project_name}
    ```
3.  **Instala las dependencias de desarrollo:**

    ```bash
    # Ejemplo para proyectos Python con pip:
    pip install -r requirements-dev.txt

    # Ejemplo para proyectos JavaScript/TypeScript con npm:
    npm install
    ```
4.  **Corre los tests localmente:**

    ```bash
    # Ejemplo para proyectos Python con pytest:
    pytest

    # Ejemplo para proyectos JavaScript/TypeScript con jest:
    npm test
    ```
5.  **Herramientas recomendadas:**
    *   Editor de código: VS Code, Sublime Text, etc.
    *   Linters y formatters: ESLint, Prettier, Black, etc.
6.  **Setup del IDE:** Configura tu IDE para que utilice las herramientas de linting y formatting.

## Flujo de Trabajo: Fork → Branch → PR

1.  **Fork el repositorio:** Ya lo hiciste en la sección anterior.
2.  **Clona tu fork:** También lo hiciste en la sección anterior.
3.  **Crea una rama con un nombre descriptivo:**

    ```bash
    git checkout -b feature/nueva-funcionalidad
    # o
    git checkout -b fix/correccion-de-bug
    ```
4.  **Haz tus cambios:** Implementa la funcionalidad o corrige el bug.
5.  **Haz commits con mensajes claros:**

    ```bash
    git add .
    git commit -m "feat: Añade nueva funcionalidad"
    ```
6.  **Sube tu rama a tu fork:**

    ```bash
    git push origin feature/nueva-funcionalidad
    ```
7.  **Crea un Pull Request:** Ve a la página de tu fork en GitHub y haz clic en el botón "Compare & pull request".
8.  **Responde a las revisiones:** Atiende el feedback de los revisores y realiza los cambios necesarios.
9.  **Merge:** Una vez que el PR sea aprobado, será mergeado a la rama principal.

## Guía de Estilo de Código

Sigue estas guías de estilo para mantener la coherencia del código:

**Python:**

*   **PEP 8:** Utiliza la guía de estilo PEP 8 para el código Python.
*   **Type hints:** Utiliza type hints para mejorar la legibilidad y mantenibilidad del código.
*   **Docstrings:** Escribe docstrings para documentar las funciones, clases y módulos.

```python
# Ejemplo de código Python bueno
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        La suma de a y b.
    """
    return a + b

# Ejemplo de código Python malo
def suma(a,b):
    return a+b
```

**JavaScript/TypeScript:**

*   **ESLint:** Utiliza ESLint para detectar errores y mantener la coherencia del código. Configuración recomendada: [Link a la config de ESLint].
*   **Prettier:** Utiliza Prettier para formatear el código automáticamente.
*   **Naming conventions:** Utiliza camelCase para nombres de variables y funciones, y PascalCase para nombres de clases.

```javascript
// Ejemplo de código JavaScript bueno
const nombreUsuario = "Juan Pérez";

function obtenerNombreCompleto(nombre, apellido) {
  return `${nombre} ${apellido}`;
}

// Ejemplo de código JavaScript malo
var NombreUsuario = "Juan Pérez";

function obtenernombrecompleto(nombre, apellido) {
  return nombre + " " + apellido;
}
```

## Testing

Utilizamos [Nombre del framework de testing] para realizar pruebas unitarias e integrales.

*   **Cómo correr tests:** Sigue las instrucciones en la sección de Configuración de Desarrollo.
*   **Cobertura esperada:** Apuntamos a una cobertura de al menos el 80%.
*   **Cómo escribir tests:** Escribe tests claros y concisos que cubran todos los casos de uso.

```python
# Ejemplo de test en Python con pytest
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
```

## Commits y Mensajes

Utilizamos la convención de [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) para los mensajes de commit.

*   **Tipos:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
*   **Ejemplos de mensajes buenos:**
    *   `feat: Añade soporte para la nueva API`
    *   `fix: Corrige bug al guardar el usuario`
    *   `docs: Actualiza la documentación de la API`
*   **Cómo hacer commits atómicos:** Cada commit debe representar un cambio lógico y completo.

## Pull Request Process

1.  **Asegúrate de estar actualizado/a con la rama principal:**

    ```bash
    git pull origin {main_branch}
    ```
2.  **Incluye una descripción clara del PR:** Explica qué cambios has realizado y por qué.
3.  **Referencia los issues relacionados:** Utiliza `#NúmeroDeIssue` para referenciar los issues que resuelve el PR.
4.  **Responde al feedback:** Atiende el feedback de los revisores y realiza los cambios necesarios.
5.  **Sé paciente con las revisiones:** Los revisores están ocupados, así que ten paciencia.

## Revisión de Código

Los revisores buscarán lo siguiente:

*   **Calidad del código:** El código debe ser legible, mantenible y eficiente.
*   **Cobertura de tests:** El código debe estar bien cubierto por tests.
*   **Cumplimiento de la guía de estilo:** El código debe seguir la guía de estilo.

## Documentación

Documenta tus cambios en el código utilizando docstrings y comentarios. Actualiza la documentación del proyecto si es necesario.

## Reconocimiento

Agradecemos a todos los que contribuyen a {project_name}. Reconocemos a los contribuyentes en la página de [contribuidores](link a la página de contribuidores) y en las notas de lanzamiento.

## Contacto y Preguntas

Si tienes alguna pregunta, no dudes en contactarnos:

*   Email: [email del mantenedor]
*   Discord/Slack: [link a la comunidad de Discord/Slack]
*   Discussions en GitHub: [link a la sección de discussions en GitHub]

¡Gracias por tu contribución!
```