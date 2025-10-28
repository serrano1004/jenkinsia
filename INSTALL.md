# Guía de Instalación - jenkinsia

Esta guía te ayudará a configurar y ejecutar **jenkinsia** en tu máquina local.

## 📋 Requisitos del Sistema

- **Python**: 3.8 o superior

## 🛠️ Instalación Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/serrano1004/jenkinsia.git
cd jenkinsia
```

### 2. Configurar Entorno Virtual (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## ✅ Verificar Instalación

Ejecuta lo siguiente para verificar que todo funciona:
```bash
python --version
# Ejecutar script principal o tests
```

---
*Generado automáticamente por [AutoDoc](https://github.com/serrano1004/AutoDoc)*