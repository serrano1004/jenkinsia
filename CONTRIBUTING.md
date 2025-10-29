```markdown
# ¡Contribuyendo a {project_name}! 👋

¡Bienvenido! Nos emociona que estés interesado en contribuir a {project_name}. Tu ayuda es invaluable para mejorar este proyecto y hacerlo aún mejor. Ya sea que encuentres un bug, quieras sugerir una nueva característica o simplemente mejorar la documentación, ¡tu contribución es bienvenida!

## Código de Conducta 🤝

Nuestro objetivo es crear una comunidad acogedora y respetuosa para todos. Nos comprometemos a proporcionar un entorno libre de acoso para todos, independientemente de su edad, tamaño corporal, discapacidad, etnia, identidad y expresión de género, nivel de experiencia, educación, estatus socioeconómico, nacionalidad, apariencia personal, raza, religión o identidad y orientación sexual.

**Valores Clave:**

*   Respeto mutuo y cortesía.
*   Empatía hacia otros miembros de la comunidad.
*   Apertura a diferentes perspectivas y experiencias.

No toleramos ningún tipo de acoso. Esto incluye comentarios ofensivos relacionados con los atributos mencionados anteriormente, intimidación, acoso deliberado, fotografías o grabaciones de acoso, interrupción sostenida de conversaciones, contacto físico inapropiado y atención sexual no deseada.

Si experimentas o presencias una violación de este código de conducta, por favor, repórtalo a [email protected]. Todos los reportes serán investigados y se tomarán las medidas apropiadas.

## Formas de Contribuir ✨

Hay muchas maneras de contribuir a {project_name}:

*   **Reportar Bugs:** Ayuda a mejorar la estabilidad del proyecto identificando y reportando errores.
*   **Sugerir Features:** Comparte tus ideas para nuevas funcionalidades y mejoras.
*   **Mejorar la Documentación:** Haz que el proyecto sea más accesible y fácil de entender.
*   **Escribir Tests:** Asegura la calidad del código con pruebas unitarias y de integración.
*   **Responder Preguntas en Issues:** Ayuda a otros usuarios resolviendo sus dudas.
*   **Mantener Traducciones:** Expande el alcance del proyecto a diferentes idiomas.

## Reportar Bugs 🐛

Para reportar un bug, por favor, sigue estos pasos:

1.  **Verifica si el bug ya ha sido reportado:** Busca en los issues existentes para evitar duplicados.
2.  **Crea un nuevo issue:** Describe el bug de la forma más clara y detallada posible.
3.  **Incluye la siguiente información:**
    *   Una descripción clara y concisa del bug.
    *   Pasos para reproducir el bug.
    *   El comportamiento esperado y el comportamiento real.
    *   Tu entorno (sistema operativo, versión de {tech_stack}, etc.).
    *   Cualquier información adicional que pueda ser útil.

**Ejemplo de Título de Issue:** "Bug: El botón 'Guardar' no funciona en el formulario de configuración"

**Template de Issue (Bug Report):**

```markdown
## Descripción del Bug

[Describe el bug de forma clara y concisa]

## Pasos para Reproducir

1.  [Paso 1]
2.  [Paso 2]
3.  [Paso 3]

## Comportamiento Esperado

[Describe el comportamiento que esperabas]

## Comportamiento Actual

[Describe el comportamiento que realmente ocurre]

## Entorno

*   Sistema Operativo: [Ejemplo: Windows 10]
*   Versión de {tech_stack}: [Ejemplo: Python 3.9]
*   Otros: [Cualquier información adicional relevante]

## Información Adicional

[Cualquier información adicional que pueda ser útil]
```

## Sugerir Features 💡

Para sugerir una nueva característica, por favor, sigue estos pasos:

1.  **Verifica si la característica ya ha sido sugerida:** Busca en los issues existentes para evitar duplicados.
2.  **Crea un nuevo issue:** Describe la característica de la forma más clara y detallada posible.
3.  **Incluye la siguiente información:**
    *   Una descripción clara y concisa de la característica.
    *   El caso de uso de la característica.
    *   Ejemplos de cómo se podría usar la característica.
    *   Cualquier beneficio que la característica pueda aportar.

**Ejemplo de Título de Issue:** "Feature Request: Agregar soporte para la autenticación de dos factores"

**Template de Issue (Feature Request):**

```markdown
## Descripción de la Característica

[Describe la característica de forma clara y concisa]

## Caso de Uso

[Describe cómo se usaría la característica]

## Ejemplos

[Proporciona ejemplos de cómo se podría usar la característica]

## Beneficios

[Describe los beneficios que la característica aportaría]

## Información Adicional

[Cualquier información adicional relevante]
```

## Configuración de Desarrollo ⚙️

Para configurar tu entorno de desarrollo, sigue estos pasos:

1.  **Fork el repositorio:** Haz clic en el botón "Fork" en la parte superior derecha de la página del repositorio en GitHub.
2.  **Clona tu fork:**

    ```bash
    git clone {repository_url}
    cd {project_name}
    ```

3.  **Instala las dependencias de desarrollo:**

    ```bash
    # Ejemplo para un proyecto Python
    pip install -r requirements-dev.txt

    # Ejemplo para un proyecto JavaScript/TypeScript
    npm install
    ```

4.  **Corre los tests localmente:** (Ver sección de Testing)

**Herramientas Recomendadas:**

*   **Editor de Código:** VS Code, Sublime Text, Atom
*   **Extensiones:** ESLint, Prettier (para JavaScript/TypeScript), Python extension (para Python)
*   **Entorno Virtual:** virtualenv, conda (para Python)

**Setup del IDE (VS Code):**

1.  Instala las extensiones recomendadas.
2.  Configura ESLint y Prettier para que se ejecuten al guardar el archivo.
3.  Configura un entorno virtual para aislar las dependencias del proyecto.

## Flujo de Trabajo: Fork → Branch → PR 🌳

Para contribuir con código, sigue este flujo de trabajo:

1.  **Fork el repositorio:** (Ya realizado en la configuración)
2.  **Clona tu fork:** (Ya realizado en la configuración)
3.  **Crea una rama con un nombre descriptivo:**

    ```bash
    git checkout -b feature/nueva-caracteristica
    # o
    git checkout -b fix/correccion-bug
    ```

4.  **Haz tus cambios:** Implementa la nueva característica o corrige el bug.
5.  **Haz commits con mensajes claros y concisos:**

    ```bash
    git add .
    git commit -m "feat: Agrega soporte para la autenticación de dos factores"
    ```

6.  **Sube tu rama a tu fork:**

    ```bash
    git push origin feature/nueva-caracteristica
    ```

7.  **Crea un Pull Request:** Ve a tu fork en GitHub y haz clic en el botón "Compare & pull request".
8.  **Responde a las revisiones:** Implementa los cambios sugeridos por los revisores.
9.  **¡Merge!:** Una vez que tu Pull Request sea aprobado, será mergeado al branch principal.

## Guía de Estilo de Código 🎨

Es importante seguir una guía de estilo de código consistente para mantener la calidad del proyecto.

**Python:**

*   Sigue las convenciones de PEP 8.
*   Utiliza type hints para mejorar la legibilidad y la mantenibilidad del código.
*   Escribe docstrings para documentar las funciones y las clases.

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
def suma(a,b):
    return a+b
```

**JavaScript/TypeScript:**

*   Utiliza ESLint para linting y Prettier para formateo.
*   Sigue las convenciones de naming del proyecto.
*   Escribe comentarios claros y concisos.

```javascript
// Ejemplo de código bueno
const nombreUsuario = "Juan Pérez";

function saludarUsuario(nombre: string): string {
  return `Hola, ${nombre}!`;
}

// Ejemplo de código malo
var a = "Juan Pérez";

function b(c) {
  return "Hola, " + c + "!";
}
```

## Testing ✅

Utilizamos `pytest` (ejemplo) para realizar pruebas en {project_name}.

*   **Para correr los tests:**

    ```bash
    pytest
    ```

*   **Cobertura esperada:** Nos esforzamos por mantener una cobertura de al menos el 80%.
*   **Cómo escribir tests:** Escribe tests unitarios para cada función y clase.  Asegúrate de que los tests cubran todos los casos de uso posibles.
*   **Ejemplo de test:**

    ```python
    # Ejemplo de test en Python (con pytest)
    def test_suma():
        assert suma(2, 3) == 5
        assert suma(-1, 1) == 0
        assert suma(0, 0) == 0
    ```

## Commits y Mensajes 📝

Utilizamos Conventional Commits para mantener un historial de commits limpio y consistente.

*   **Tipos:**
    *   `feat`: Agrega una nueva característica.
    *   `fix`: Corrige un bug.
    *   `docs`: Cambios en la documentación.
    *   `style`: Cambios en el estilo del código (formato, linting, etc.).
    *   `refactor`: Refactorización del código.
    *   `test`: Agrega o modifica tests.
    *   `chore`: Tareas de mantenimiento.

*   **Ejemplos de mensajes buenos:**

    ```
    feat: Agrega soporte para la autenticación de dos factores
    fix: Corrige un bug en el formulario de configuración
    docs: Actualiza la documentación para la nueva versión
    ```

*   **Commits atómicos:** Haz commits pequeños y enfocados en una sola tarea.
*   **Importancia:** Un historial de commits limpio facilita la revisión del código y la comprensión de los cambios.

## Pull Request Process 📤

1.  **Asegúrate de estar actualizado con la rama principal:**

    ```bash
    git checkout {main_branch}
    git pull origin {main_branch}
    git checkout tu-rama
    git merge {main_branch}
    ```

2.  **Incluye una descripción clara y concisa del Pull Request:** Describe los cambios que has realizado y por qué.
3.  **Referencia los issues relacionados:** Utiliza `#issue-number` para referenciar los issues que tu Pull Request resuelve.
4.  **Responde al feedback:** Implementa los cambios sugeridos por los revisores.
5.  **Sé paciente:** La revisión del código puede tomar tiempo.

**Tips para un Pull Request exitoso:**

*   Sigue la guía de estilo de código.
*   Escribe tests unitarios para tu código.
*   Haz commits pequeños y enfocados.
*   Escribe mensajes de commit claros y concisos.
*   Responde al feedback de los revisores.

## Revisión de Código 👀

La revisión de código es un proceso importante para asegurar la calidad del proyecto.

*   **Criterios de aceptación:** El código debe ser claro, conciso, bien documentado y seguir la guía de estilo.
*   **Qué busca el revisor:** El revisor buscará bugs, errores de diseño, problemas de rendimiento y oportunidades de mejora.
*   **Cómo recibir feedback:** Agradece el feedback y trata de entender las sugerencias del revisor.
*   **Cómo hacer follow-up:** Implementa los cambios sugeridos por el revisor y responde a sus preguntas.

## Documentación 📝

Es importante documentar todos los cambios que realices en el código.

*   **Cómo documentar cambios:** Escribe docstrings para las funciones y las clases.
*   **Dónde documentar:** Documenta los cambios en el código, en la documentación del proyecto y en el README.
*   **Ejemplos en docstrings:**

    ```python
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
    ```

*   **README updates:** Actualiza el README con cualquier cambio importante en el proyecto.

## Reconocimiento 🏆

Agradecemos a todos los que contribuyen a {project_name}.

*   **Cómo se reconoce a los contribuidores:** Los contribuidores son mencionados en el README y en las notas de lanzamiento.
*   **Lista de contribuidores:** (Se actualizará automáticamente con las contribuciones)
*   **Credits en release notes:** Los contribuidores son mencionados en las notas de lanzamiento de cada nueva versión.

## Contacto y Preguntas ❓

Si tienes alguna pregunta, no dudes en contactarnos.

*   **Email:** [email protected]
*   **Discord/Slack:** [Enlace a la comunidad]
*   **Discussions en GitHub:** [Enlace a las discussions]
*   **Email del mantenedor:** [email protected]

¡Gracias por contribuir a {project_name}!
```