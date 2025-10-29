```markdown
# ¡Contribuyendo a {project_name}! 👋

¡Bienvenido! Nos emociona que estés interesado en contribuir a {project_name}, un proyecto {tech_stack} open-source. Tu ayuda es valiosa para hacerlo aún mejor. No importa si eres un desarrollador experimentado o estás empezando, ¡todos son bienvenidos! Puedes contribuir de muchas maneras, desde reportar bugs y mejorar la documentación, hasta proponer nuevas funcionalidades y escribir código.

## Código de Conducta 🤝

Nuestro proyecto se rige por un código de conducta que promueve un ambiente respetuoso e inclusivo para todos los participantes. Valoramos la diversidad de opiniones y experiencias, y esperamos que todos se traten con cortesía y respeto. No toleramos ninguna forma de acoso o discriminación.

Si experimentas o presencias una violación de este código de conducta, por favor repórtalo a [email del mantenedor]. Tomaremos todas las denuncias en serio y actuaremos en consecuencia.

## Formas de Contribuir ✨

Hay muchas maneras de contribuir a {project_name}:

*   **Reportar Bugs:** Ayúdanos a encontrar y corregir errores en el código.
*   **Sugerir Features:** Propón nuevas funcionalidades que mejoren el proyecto.
*   **Mejorar la Documentación:** Haz que la documentación sea más clara y completa.
*   **Escribir Tests:** Asegura la calidad del código con pruebas automatizadas.
*   **Responder Preguntas en Issues:** Ayuda a otros usuarios resolviendo sus dudas.
*   **Contribuir con Traducciones:** Haz que el proyecto sea accesible a más personas.

## Reportar Bugs 🐛

Cuando reportes un bug, proporciona la mayor cantidad de información posible para que podamos reproducirlo y solucionarlo. Incluye los siguientes datos:

*   **Descripción del bug:** Explica claramente qué problema estás experimentando.
*   **Pasos para reproducir:** Describe los pasos exactos para reproducir el bug.
*   **Comportamiento esperado:** Describe cómo debería funcionar el programa.
*   **Comportamiento actual:** Describe lo que realmente está sucediendo.
*   **Entorno:** Indica el sistema operativo, la versión del lenguaje y las dependencias utilizadas.

Utiliza el siguiente formato para reportar el bug en un issue:

```markdown
## Descripción del Bug

[Describe el problema que estás experimentando.]

## Pasos para Reproducir

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

## Comportamiento Esperado

[Describe cómo debería funcionar el programa.]

## Comportamiento Actual

[Describe lo que realmente está sucediendo.]

## Entorno

*   Sistema Operativo: [Ejemplo: Windows 10]
*   Versión de Python: [Ejemplo: 3.9.7]
*   Dependencias: [Enumera las dependencias relevantes]
```

## Sugerir Features 💡

Cuando sugieras una nueva funcionalidad, describe claramente el problema que resuelve y cómo mejorará el proyecto. Incluye los siguientes datos:

*   **Descripción de la feature:** Explica la funcionalidad que propones.
*   **Caso de uso:** Describe cómo se utilizará la funcionalidad.
*   **Ejemplos:** Proporciona ejemplos de cómo se vería y funcionaría la funcionalidad.

Utiliza el siguiente formato para sugerir la feature en un issue:

```markdown
## Descripción de la Feature

[Describe la funcionalidad que propones.]

## Caso de Uso

[Describe cómo se utilizará la funcionalidad.]

## Ejemplos

[Proporciona ejemplos de cómo se vería y funcionaría la funcionalidad.]
```

## Configuración de Desarrollo ⚙️

Para empezar a contribuir, sigue estos pasos:

1.  **Haz un fork del repositorio:** Haz clic en el botón "Fork" en la parte superior derecha de la página del repositorio en GitHub.
2.  **Clona tu fork:** Clona tu fork del repositorio a tu máquina local:

    ```bash
    git clone {repository_url}
    cd {project_name}
    ```

3.  **Instala las dependencias de desarrollo:** Utiliza el gestor de paquetes adecuado para instalar las dependencias necesarias.

    *   **Python:**

        ```bash
        pip install -r requirements-dev.txt  # Asumiendo que tienes un archivo requirements-dev.txt
        ```

    *   **JavaScript/TypeScript:**

        ```bash
        npm install  # o yarn install
        ```

4.  **Corre los tests localmente:** Asegúrate de que los tests pasan antes de empezar a modificar el código.

    *   **Python:**

        ```bash
        pytest
        ```

    *   **JavaScript/TypeScript:**

        ```bash
        npm test  # o yarn test
        ```

5.  **Herramientas recomendadas:** Recomendamos utilizar un IDE como VS Code con las extensiones adecuadas para el lenguaje que estés utilizando.

    *   **Python:** Python extension, Pylance, Black formatter
    *   **JavaScript/TypeScript:** ESLint, Prettier, TypeScript extension

## Flujo de Trabajo: Fork → Branch → PR 🌳

El flujo de trabajo recomendado para contribuir es el siguiente:

1.  **Fork el repositorio.** (Ya realizado en la sección anterior).
2.  **Clona tu fork.** (Ya realizado en la sección anterior).
3.  **Crea una rama con un nombre descriptivo:** Crea una rama para tus cambios. Utiliza un nombre descriptivo que indique el propósito de la rama.

    ```bash
    git checkout -b feature/nueva-funcionalidad  # o fix/correccion-bug
    ```

4.  **Haz cambios:** Modifica el código para implementar la funcionalidad o corregir el bug.
5.  **Haz commits con mensajes claros:** Realiza commits con mensajes descriptivos que expliquen los cambios realizados.

    ```bash
    git add .
    git commit -m "feat: Agrega nueva funcionalidad para..."
    ```

6.  **Push a tu rama:** Sube tu rama a tu fork del repositorio.

    ```bash
    git push origin feature/nueva-funcionalidad
    ```

7.  **Crea un Pull Request:** Crea un pull request desde tu rama a la rama principal (`{main_branch}`) del repositorio original.
8.  **Responde a reviews:** Atiende los comentarios y sugerencias de los revisores.
9.  **Merge:** Una vez que el pull request sea aprobado, se fusionará a la rama principal.

## Guía de Estilo de Código 🎨

Es importante seguir una guía de estilo de código consistente para mantener la calidad y legibilidad del código.

*   **Python:**

    *   Sigue las convenciones de PEP 8.
    *   Utiliza type hints para mejorar la legibilidad y la seguridad del código.
    *   Escribe docstrings para documentar las funciones, clases y módulos.

    Ejemplo de código bueno:

    ```python
    def sumar(a: int, b: int) -> int:
        """Suma dos números enteros.

        Args:
            a: El primer número entero.
            b: El segundo número entero.

        Returns:
            La suma de a y b.
        """
        return a + b
    ```

    Ejemplo de código malo:

    ```python
    def sum(a,b):
        return a+b
    ```

*   **JavaScript/TypeScript:**

    *   Utiliza ESLint con la configuración recomendada para el proyecto.
    *   Utiliza Prettier para formatear el código automáticamente.
    *   Sigue las convenciones de nomenclatura del lenguaje.

    Ejemplo de código bueno:

    ```typescript
    function sumar(a: number, b: number): number {
        return a + b;
    }
    ```

    Ejemplo de código malo:

    ```javascript
    function sum(a,b){
        return a+b;
    }
    ```

## Testing 🧪

Utilizamos [Framework de Testing] para realizar pruebas automatizadas. Para correr los tests, utiliza el siguiente comando:

```bash
pytest  # o npm test / yarn test
```

Esperamos que el código tenga una cobertura de tests alta. Escribe tests para todas las funcionalidades nuevas y para las correcciones de bugs.

Ejemplo de test:

```python
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
```

## Commits y Mensajes 📝

Utilizamos Conventional Commits para estructurar los mensajes de commit. Los tipos de commit más comunes son:

*   `feat`: Agrega una nueva funcionalidad.
*   `fix`: Corrige un bug.
*   `docs`: Modifica la documentación.
*   `style`: Cambios en el estilo del código (formato, etc.).
*   `refactor`: Refactoriza el código sin cambiar la funcionalidad.
*   `test`: Agrega o modifica tests.
*   `chore`: Tareas de mantenimiento.

Ejemplos de mensajes de commit buenos:

*   `feat: Agrega la funcionalidad de autenticación de usuarios`
*   `fix: Corrige el bug que causaba el error 500 en la página de inicio`

Realiza commits atómicos que se centren en una sola tarea. Esto facilita la revisión del código y la reversión de cambios.

## Pull Request Process 🚀

Para crear un pull request exitoso, sigue estos consejos:

*   Asegúrate de estar actualizado con la rama `{main_branch}`.
*   Incluye una descripción clara del problema que resuelve el pull request y cómo lo soluciona.
*   Referencia los issues relacionados.
*   Responde a los comentarios y sugerencias de los revisores.
*   Sé paciente con el proceso de revisión.

## Revisión de Código 👀

Los revisores buscarán lo siguiente:

*   Que el código sea claro y fácil de entender.
*   Que el código siga la guía de estilo.
*   Que el código tenga tests adecuados.
*   Que el código resuelva el problema de manera efectiva.

Recibe el feedback con una mente abierta y utiliza las sugerencias para mejorar tu código.

## Documentación 📚

Documenta todos los cambios que realices en el código. Utiliza docstrings para documentar las funciones, clases y módulos. Actualiza el README y otros documentos relevantes.

## Reconocimiento 🏆

Agradecemos a todos los que contribuyen a {project_name}. Reconocemos a los contribuidores de las siguientes maneras:

*   Mencionando sus nombres en las notas de la versión.
*   Agregándolos a la lista de contribuidores en el README.

Lista de contribuidores:

*   [Lista de contribuidores actuales]

## Contacto y Preguntas 💬

Si tienes alguna pregunta, no dudes en contactarnos:

*   Email: [email del mantenedor]
*   Discord/Slack: [Enlace a la comunidad]
*   Discussions en GitHub: [Enlace a la sección de Discussions]

¡Gracias por tu interés en contribuir a {project_name}!
```