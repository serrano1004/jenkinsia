# Guía de Despliegue - jenkinsia

Esta guía te ayudará a desplegar el proyecto en diferentes entornos.

## 🚀 Opciones de Despliegue

### ☁️ Despliegue en la Nube

#### Heroku
```bash
# Instalar Heroku CLI
heroku login
heroku create tu-app-name
git push heroku main
```

#### Railway
```bash
# Instalar Railway CLI
railway login
railway init
railway up
```

### 🖥️ Servidor Tradicional

#### Preparación del Servidor
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y dependencias
sudo apt install python3 python3-pip python3-venv -y

# Instalar Git
sudo apt install git -y
```

#### Clonar y Configurar
```bash
# Clonar repositorio
git clone <repository-url> /opt/jenkinsia
cd /opt/jenkinsia

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## ⚙️ Variables de Entorno

Configura las siguientes variables de entorno:

```bash
export ENV=production
export DATABASE_URL=your_database_url
export SECRET_KEY=your_secret_key
```

## 🔒 Consideraciones de Seguridad

- Usa HTTPS en producción
- Configura firewall adecuadamente
- Mantén las dependencias actualizadas
- Usa variables de entorno para secrets
- Implementa logging y monitoreo

## 📊 Monitoreo y Logging

### Logs
```bash
# Ver logs en tiempo real
tail -f /var/log/app.log
```

### Health Check
```bash
# Verificar que la aplicación esté corriendo
curl http://localhost:8080/health
```

## 🆘 Troubleshooting

### Problemas Comunes
- **Puerto ocupado**: Cambiar puerto en configuración
- **Permisos**: Verificar permisos de archivos y directorios
- **Dependencias**: Verificar que todas las dependencias estén instaladas
- **Variables de entorno**: Verificar que estén configuradas correctamente
