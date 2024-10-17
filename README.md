# Objetivo
El objetivo del PoC que hemos desarrollado es integrar un modelo de Machine Learning en un pipeline de CI/CD utilizando Jenkins. Este modelo tiene como finalidad predecir la importancia de los cambios (commits) realizados en un repositorio de código, basándose en las inserciones y eliminaciones que estos contienen.

# Funcionamiento
## Recolección de Datos:

 - detection.py: Este script se encarga de recolectar información sobre los commits en el repositorio de Git. Extrae datos de inserciones y eliminaciones de cada commit mediante comandos de Git, almacenando estos datos en matrices que se utilizan para entrenar el modelo.
Entrenamiento del Modelo:

Los datos recolectados se utilizan para entrenar un clasificador (en este caso, un árbol de decisión de scikit-learn) que puede predecir si un nuevo cambio es importante o no.

## Predicción:

 - predict.py: Este script se encarga de predecir si un nuevo commit es importante, utilizando el modelo previamente entrenado. Se obtiene información del último commit, calculando sus inserciones y eliminaciones, y se pasa esta información al modelo para hacer la predicción.

## ¿Por Qué se Ha Hecho?
La implementación de este PoC responde a la necesidad de:

 - Mejorar la Calidad del Código: Automatizar la identificación de cambios importantes puede ayudar a los equipos de desarrollo a enfocarse en las áreas del código que requieren atención, mejorando así la calidad general del software.

 - Optimizar el Proceso de Revisión: Facilitar a los revisores el enfoque en los cambios significativos, reduciendo el tiempo de revisión y aumentando la eficiencia del equipo.

 - Integración de IA en CI/CD: Mostrar cómo se puede integrar Machine Learning en un proceso de entrega continua (CI/CD) para ayudar a tomar decisiones más informadas basadas en datos.

# Posibles Usos y Ejemplos Reales
## Monitoreo de Repositorios:

Un equipo de desarrollo podría utilizar este PoC para monitorizar un repositorio de código de un proyecto grande. Cada vez que se realiza un nuevo commit, el sistema podría predecir si el cambio es crítico, ayudando a priorizar revisiones y pruebas.

## Alertas Automáticas:

Si el sistema determina que un commit es importante (por ejemplo, cambios en funciones clave o en módulos críticos), podría enviar alertas automáticas a los miembros del equipo o integrar esta funcionalidad con un sistema de gestión de incidencias para registrar un seguimiento.

## Integración en Flujos de Trabajo:

Este modelo se podría integrar en herramientas de gestión de proyectos como Jira o Trello, donde los commits importantes podrían automáticamente crear tareas o tickets para que los revisores evalúen esos cambios.

## Análisis de Impacto:

La solución podría ampliarse para analizar el impacto de los cambios en otras partes del sistema, ayudando a los desarrolladores a entender las implicaciones de sus commits en el comportamiento general del software.

## Soporte para Decisiones de Despliegue:

Antes de realizar un despliegue en producción, el sistema podría evaluar automáticamente los últimos cambios y decidir si es seguro proceder basándose en el análisis de los commits realizados.

# Conclusión
El PoC desarrollado es una base sólida que demuestra cómo la inteligencia artificial y el aprendizaje automático pueden ser utilizados en el ciclo de vida del desarrollo de software para mejorar la calidad y la eficiencia. La implementación de tales sistemas no solo optimiza los procesos existentes, sino que también ayuda a los equipos a tomar decisiones más informadas y basadas en datos, lo cual es crucial en entornos de desarrollo ágiles y dinámicos.