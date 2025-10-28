```markdown
# SECURITY.md

La seguridad de {project_name} es de suma importancia. Nos tomamos en serio la protección de los datos de nuestros usuarios y la integridad de nuestro sistema.

Este documento describe cómo reportar vulnerabilidades de seguridad, las prácticas de seguridad recomendadas para el proyecto, vulnerabilidades conocidas y recursos adicionales para mantener {project_name} seguro.

## Reportar Vulnerabilidades de Seguridad

Creemos que la divulgación responsable de vulnerabilidades de seguridad ayuda a mejorar la seguridad general de {project_name}. Si descubre una vulnerabilidad de seguridad, le agradecemos que nos la informe de manera responsable.

**Por favor, NO cree un issue público en el repositorio.** En su lugar, envíe un correo electrónico a: {contact_email}

En su informe, incluya la siguiente información:

*   Una descripción detallada de la vulnerabilidad.
*   Pasos para reproducir la vulnerabilidad.
*   El componente o sistema afectado.
*   Posibles impactos de la vulnerabilidad.
*   Cualquier información adicional que pueda ser útil para comprender y resolver la vulnerabilidad.

Nuestro equipo de seguridad responderá a su informe en un plazo de 3 días hábiles para acusar recibo y comenzar a investigar el problema. Trabajaremos con usted para comprender y solucionar la vulnerabilidad lo más rápido posible.

**Proceso de Divulgación Responsable:**

Una vez que recibamos su informe, nuestro equipo de seguridad:

1.  Acusará recibo de su informe en un plazo de 3 días hábiles.
2.  Investigará la vulnerabilidad y determinará su impacto.
3.  Trabajará con usted para comprender y solucionar la vulnerabilidad.
4.  Le informará sobre el progreso de la resolución.
5.  Una vez que la vulnerabilidad se haya solucionado, le daremos crédito por su informe (a menos que prefiera permanecer anónimo).
6.  Divulgaremos públicamente la vulnerabilidad una vez que se haya solucionado y haya transcurrido un tiempo razonable para que los usuarios actualicen sus sistemas.

## Prácticas de Seguridad

Para garantizar la seguridad de {project_name}, seguimos varias prácticas de seguridad recomendadas:

### 3.1 Gestión de Dependencias

*   **Verificación de Dependencias:** Es crucial verificar las dependencias de su proyecto en busca de vulnerabilidades conocidas.  Utilice herramientas como `pip-audit` (para Python) o `npm audit` (para Node.js) para identificar y abordar estas vulnerabilidades.

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

    ```bash
    # Ejemplo con npm audit
    npm audit
    ```

*   **Mantenimiento Actualizado:** Mantenga las dependencias de su proyecto actualizadas con las últimas versiones para corregir vulnerabilidades conocidas.

    ```bash
    # Ejemplo con pip
    pip install --upgrade -r requirements.txt
    ```

    ```bash
    # Ejemplo con npm
    npm update
    ```

*   **Alertas de Vulnerabilidades:** Configure alertas de vulnerabilidades para recibir notificaciones cuando se descubran nuevas vulnerabilidades en sus dependencias.  GitHub y otros proveedores de repositorios ofrecen esta funcionalidad.

### 3.2 Manejo de Secretos

*   **Nunca Hardcodear Secretos:** Nunca incluya contraseñas, claves API u otra información confidencial directamente en su código.

    **INSEGURO:**

    ```python
    api_key = "YOUR_API_KEY"
    ```

    **SEGURO:**

    ```python
    import os
    api_key = os.environ.get("API_KEY")
    ```

*   **Variables de Entorno:** Utilice variables de entorno para almacenar información confidencial.  Estas variables se pueden configurar en su sistema operativo o en su entorno de implementación.

*   **.env en .gitignore:** Asegúrese de agregar el archivo `.env` a su archivo `.gitignore` para evitar que se suba al repositorio.

*   **Herramientas para Detectar Leaks:** Utilice herramientas como `git-secrets` o `trufflehog` para detectar secretos accidentalmente comprometidos en su repositorio.

### 3.3 Validación de Entrada

*   **Validar Entrada de Usuario:** Siempre valide la entrada del usuario para evitar ataques de inyección y otros problemas de seguridad.

    **INSEGURO:**

    ```python
    import os
    user_input = input("Ingrese un nombre de archivo: ")
    os.system("cat " + user_input) # Vulnerable a inyección de comandos
    ```

    **SEGURO:**

    ```python
    import os
    import shlex
    user_input = input("Ingrese un nombre de archivo: ")
    safe_input = shlex.quote(user_input) # Escapa la entrada para seguridad
    os.system("cat " + safe_input)
    ```

    O, mejor aún, use funciones seguras para la manipulación de archivos:

    ```python
    with open(user_input, 'r') as f:
        content = f.read()
        print(content)
    ```

*   **Prevenir Inyección:**  Evite el uso de concatenación de cadenas para construir consultas SQL o comandos del sistema operativo. Utilice consultas parametrizadas o funciones de escape para prevenir ataques de inyección.

### 3.4 Gestión de Acceso

*   **Principio de Mínimo Privilegio:** Otorgue a los usuarios solo los permisos que necesitan para realizar sus tareas.

*   **SSH Keys vs HTTPS:** Utilice claves SSH para autenticar las conexiones a su servidor en lugar de contraseñas.  Siempre use HTTPS para cifrar la comunicación entre su cliente y servidor.

*   **Permisos de Archivos:** Configure los permisos de archivos correctamente para evitar que usuarios no autorizados accedan a información confidencial.

## 4. Seguridad en CI/CD

*   **Secrets en Jenkins/GitHub Actions:** Almacene la información confidencial (credenciales, claves API) de forma segura en su sistema de CI/CD (por ejemplo, Jenkins, GitHub Actions). Utilice las funcionalidades de gestión de secretos que ofrecen estas plataformas.

*   **Cómo Usar Credentials:** Acceda a las credenciales almacenadas en su sistema de CI/CD utilizando las variables de entorno o las funciones proporcionadas por la plataforma.

    ```yaml
    # Ejemplo en GitHub Actions
    steps:
      - name: Ejecutar script con credenciales
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          python myscript.py --api-key "$API_KEY"
    ```

*   **No Loguear Información Sensible:** Evite registrar información sensible (contraseñas, claves API) en los registros de su sistema de CI/CD.  Utilice el enmascaramiento de registros o la eliminación de información sensible para evitar la exposición accidental.

## 5. Testing de Seguridad

*   **Herramientas:** Utilice herramientas de análisis estático de código (SAST) y análisis dinámico de código (DAST) para identificar vulnerabilidades de seguridad en su código. Algunas herramientas útiles son `bandit` (para Python), `safety` (para Python) y `pip-audit` (para Python).

    ```bash
    # Ejemplo con bandit
    bandit -r myproject/
    ```

    ```bash
    # Ejemplo con safety
    safety check
    ```

    ```bash
    # Ejemplo con pip-audit
    pip-audit
    ```

*   **Cómo Ejecutar:** Ejecute estas herramientas de forma regular como parte de su proceso de desarrollo.

*   **Qué Buscar:** Busque vulnerabilidades comunes como inyección SQL, cross-site scripting (XSS), desbordamiento de búfer y vulnerabilidades de autenticación.

*   **Análisis SAST:** Implemente análisis SAST en su canalización de CI/CD para detectar problemas de seguridad en las primeras etapas del ciclo de vida del desarrollo.

## 6. Checklist de Seguridad para Contribuidores

*   **No Incluir Secretos:** No incluya contraseñas, claves API u otra información confidencial en su código.
*   **No Usar shell=True:** Evite usar `shell=True` en las funciones `subprocess` de Python, ya que puede ser vulnerable a ataques de inyección de comandos.
*   **Validar Inputs:** Valide la entrada del usuario para evitar ataques de inyección y otros problemas de seguridad.
*   **Sin Hardcoded Passwords:** No incluya contraseñas codificadas en su código.
*   **Revisar Cambios:** Revise cuidadosamente los cambios de código antes de fusionarlos en la rama principal.

## 7. Vulnerabilidades Conocidas

| CVE | Descripción | Versiones Afectadas | Solución | Fecha de Solución |
|---|---|---|---|---|
| CVE-XXXX-YYYY | Vulnerabilidad de ejemplo parcheada en la versión X.X.X.  Permitía la ejecución remota de código. | < X.X.X | Actualizar a la versión X.X.X o superior. | 2023-10-26 |

Esta tabla se actualizará a medida que se descubran y solucionen nuevas vulnerabilidades.

## 8. Recursos de Seguridad

*   [OWASP Top 10](https://owasp.org/top10/): Lista de las 10 vulnerabilidades de seguridad web más críticas.
*   [Python Security Best Practices](https://wiki.python.org/moin/WebProgramming#Security): Guía de buenas prácticas de seguridad para el desarrollo de aplicaciones Python.
*   [CWE/SANS Top 25](https://cwe.mitre.org/top25/): Lista de los 25 errores de software más peligrosos.

## 9. Soporte

Si tiene alguna pregunta o inquietud sobre la seguridad de {project_name}, no dude en ponerse en contacto con nosotros.

*   **Cómo Reportar:** Envíe un correo electrónico a: {contact_email}
*   **Email de Seguridad:** {contact_email}
*   **Contacto Directo:** Póngase en contacto con el equipo de desarrollo a través del repositorio en {repository_url}.
```