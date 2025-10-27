# jenkinsia

![CI/CD](https://img.shields.io/badge/CI%2FCD-Jenkins-blue)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)
![Python](https://img.shields.io/badge/Python-3.8+-green)

## 📝 Descripción

El objetivo del PoC que hemos desarrollado es integrar un modelo de Machine Learning en un pipeline de CI/CD utilizando Jenkins. Este modelo tiene como finalidad predecir la importancia de los cambios (commits) realizados en un repositorio de código, basándose en las inserciones y eliminaciones que estos contienen.

## 🚀 Características

- ## Recolección de Datos:: - detect_files.py: Este script se encarga de recolectar información sobre los commits en el repositorio de Git. Extrae datos de

## 📋 Requisitos Previos

- Python 3.8 o superior
- Pip para instalar dependencias
- Jenkins (para CI/CD)
- Git

## 🛠️ Instalación

### Opción 1: Instalación estándar
```bash
git clone <repository-url>
cd jenkinsia
pip install -r requirements.txt
```

## 🎯 Uso

### Uso Básico
```bash
python detect_files.py
```

### Pipeline de Jenkins
El pipeline se ejecuta automáticamente con cada commit y utiliza el modelo ML para evaluar la importancia de los cambios.

## 🏗️ Arquitectura

El sistema integra un modelo de Machine Learning en el pipeline de CI/CD:

```
Código → Jenkins Pipeline → Modelo ML → Evaluación → Despliegue
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. 🍴 Fork el proyecto
2. 🌟 Crea tu Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 📝 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la Branch (`git push origin feature/AmazingFeature`)
5. 🔃 Abre un Pull Request

### Estándares de código
- Sigue las convenciones de código del lenguaje
- Añade tests para nuevas funcionalidades
- Actualiza la documentación cuando sea necesario

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

- 🐛 [Reportar bugs](../../issues)
- 💡 [Solicitar features](../../issues)
- 📧 Contacta al equipo de desarrollo
