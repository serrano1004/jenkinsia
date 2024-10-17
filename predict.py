from sklearn.tree import DecisionTreeClassifier
import numpy as np
import subprocess
import re
from detect_files import get_real_data  # Importar la función que devuelve los datos

# Obtener los datos reales
X_real, y_real = get_real_data()

# Crear y entrenar el modelo
model = DecisionTreeClassifier()
model.fit(X_real, y_real)

# Función para obtener inserciones y eliminaciones del último commit
def obtener_inserciones_deletions():
    try:
        # Obtener el último commit
        last_commit_hash = subprocess.check_output("git log -1 --pretty=format:'%H'", shell=True).decode().strip()
        diff_output = subprocess.check_output(f"git diff --shortstat {last_commit_hash}~1 {last_commit_hash}", shell=True).decode()
        
        # Extraer inserciones y eliminaciones
        match = re.search(r'(\d+) insertion', diff_output)
        insertions = int(match.group(1)) if match else 0
        match = re.search(r'(\d+) deletion', diff_output)
        deletions = int(match.group(1)) if match else 0
        
        return insertions, deletions
    except subprocess.CalledProcessError as e:
        print("Error al obtener datos del último commit:", e)
        return 0, 0  # Retornar valores por defecto en caso de error

# Función para predecir si un nuevo commit es importante
def predecir_nuevo_commit(insertions, deletions):
    total_cambios = insertions + deletions
    is_importante = 1 if total_cambios > 20 else 0
    nuevo_cambio = np.array([[total_cambios, is_importante]])
    
    # Realizar la predicción
    prediccion = model.predict(nuevo_cambio)
    return prediccion[0]

# Obtener inserciones y eliminaciones del último commit
nuevo_insertions, nuevo_deletions = obtener_inserciones_deletions()

# Realizar la predicción
resultado = predecir_nuevo_commit(nuevo_insertions, nuevo_deletions)
print("Predicción para el nuevo cambio:", resultado)  # Imprimir resultado
