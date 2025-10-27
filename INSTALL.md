# Guía de Instalación - jenkinsia

## 📋 Requisitos del Sistema

- **Python**: 3.8 o superior
- **Pip**: Para gestión de paquetes Python
- **Git**: Para clonar el repositorio

## 🛠️ Instalación Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone <repository-url>
cd jenkinsia
```

### 2. Configurar Entorno Virtual (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración Inicial
```bash
# Crear archivo de configuración (si es necesario)
cp .env.example .env

# Editar configuración según tus necesidades
nano .env
```

### 5. Verificar Instalación
```bash
# Verificar que todo funciona correctamente
python --version
pip list
```

## 🚀 Siguiente Paso

Una vez completada la instalación, consulta el [README.md](README.md) para instrucciones de uso.

## ❓ Problemas Comunes

### Error de permisos
```bash
# Si tienes problemas de permisos con pip:
pip install --user -r requirements.txt
```

### Versión de Python incorrecta
```bash
# Verificar versión de Python
python --version
# o
python3 --version
```
