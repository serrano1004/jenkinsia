import subprocess
import numpy as np
import re

# Inicializar listas para las características y etiquetas
X_real = []
y_real = []

# Función para obtener los datos de los commits
def obtener_datos_commits():
    log_output = subprocess.check_output("git log --pretty=format:'%H'", shell=True).decode().strip().split('\n')
    
    for commit in log_output:
        diff_output = subprocess.check_output(f"git diff --shortstat {commit}~1 {commit}", shell=True).decode()

        match = re.search(r'(\d+) insertion', diff_output)
        insertions = int(match.group(1)) if match else 0
        match = re.search(r'(\d+) deletion', diff_output)
        deletions = int(match.group(1)) if match else 0

        total_changes = insertions + deletions
        is_important_change = 1 if total_changes > 20 else 0
        
        X_real.append([total_changes, is_important_change])
        y_real.append(1 if is_important_change == 1 else 0)

    return np.array(X_real), np.array(y_real)

# Llamar a la función y guardar los resultados
X_real, y_real = obtener_datos_commits()

# Guardar en variables globales
def get_real_data():
    return X_real, y_real

print("Datos de los commits obtenidos.")
