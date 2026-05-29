import subprocess
import os
import time
import glob

def count_csv_rows(csv_filename):
    """Cuenta cuántas filas de datos tiene el CSV (excluyendo cabecera)"""
    if not os.path.exists(csv_filename):
        return 0
    
    with open(csv_filename, 'r') as csvfile:
        return max(0, sum(1 for line in csvfile) - 1)

def compilar_java(project_path, java_file=None):
    """
    Compila todos los archivos Java necesarios
    
    Args:
        project_path: Ruta al directorio del proyecto
        java_file: (Opcional) Archivo principal, si se especifica compila todos
    """
    # Buscar todos los archivos .java en el directorio
    java_files = glob.glob(os.path.join(project_path, "*.java"))
    
    if not java_files:
        print(f"✗ No se encontraron archivos .java en {project_path}")
        return False
    
    print(f"Compilando {len(java_files)} archivo(s) Java...")
    for f in java_files:
        print(f"  - {os.path.basename(f)}")
    
    # Compilar todos los archivos juntos
    compile_command = ['javac', '-encoding', 'UTF-8'] + java_files
    
    result = subprocess.run(compile_command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"✗ Error de compilación:")
        print(result.stderr)
        return False
    
    print("✓ Compilación exitosa")
    return True

def limpiar_class_files(project_path):
    """Elimina todos los archivos .class generados en el proyecto"""
    class_files = glob.glob(os.path.join(project_path, "*.class"))
    
    if not class_files:
        print("  No hay archivos .class para limpiar")
        return
    
    print(f"  Limpiando {len(class_files)} archivo(s) .class...")
    for class_file in class_files:
        try:
            os.remove(class_file)
            print(f"    - Eliminado: {os.path.basename(class_file)}")
        except Exception as e:
            print(f"    ✗ Error al eliminar {class_file}: {e}")
    
    print("  ✓ Limpieza completada")

def ejecutar_hasta_100_muestras(project_path=".", java_file="ClientManager.java", csv_file="logAnalisisSafeThread.csv", target=100, limpiar_al_final=True):
    """
    Ejecuta el programa Java hasta alcanzar el número de muestras deseado
    
    Args:
        limpiar_al_final: Si es True, elimina los archivos .class al terminar
    """
    csv_path = os.path.join(project_path, csv_file)
    
    print(f"Proyecto en: {os.path.abspath(project_path)}")
    print(f"Archivo principal: {java_file}")
    print(f"CSV: {csv_path}")
    print(f"Objetivo: Al menos {target} muestras")
    
    # Compilar TODOS los archivos antes de empezar
    if not compilar_java(project_path, java_file):
        print("No se puede continuar sin compilar correctamente")
        return
    
    # Cambiar al directorio del proyecto para ejecutar
    original_dir = os.getcwd()
    os.chdir(project_path)
    
    try:
        # Verificar cuántas muestras ya existen
        muestras_actuales = count_csv_rows(csv_path)
        print(f"Muestras actuales: {muestras_actuales}")
        
        if muestras_actuales >= target:
            print(f"¡Ya hay suficientes muestras ({muestras_actuales})!")
            return
        
        ejecucion = 0
        while muestras_actuales < target:
            ejecucion += 1
            print(f"\nEjecución #{ejecucion} - Muestras: {muestras_actuales}/{target}")
            
            # Ejecutar el programa Java
            class_name = java_file.replace('.java', '')
            try:
                result = subprocess.run(['java', class_name], 
                                      capture_output=True, 
                                      text=True,
                                      timeout=30)
                
                if result.returncode == 0:
                    nuevas_muestras = count_csv_rows(csv_path)
                    if nuevas_muestras > muestras_actuales:
                        print(f"  ✓ Nuevas muestras: {nuevas_muestras - muestras_actuales}")
                        muestras_actuales = nuevas_muestras
                    else:
                        print(f"  ⚠ El programa se ejecutó pero no agregó nuevas muestras")
                        if result.stdout:
                            print(f"  Salida del programa: {result.stdout[:200]}")
                else:
                    print(f"  ✗ Error en ejecución (código: {result.returncode})")
                    if result.stderr:
                        print(f"  Error: {result.stderr[:200]}")
                    if result.stdout:
                        print(f"  Salida: {result.stdout[:200]}")
                    
            except subprocess.TimeoutExpired:
                print(f"  ✗ Timeout - El programa tardó más de 30 segundos")
            except FileNotFoundError:
                print(f"  ✗ No se encuentra el comando 'java'. ¿Tienes Java instalado?")
                break
            except Exception as e:
                print(f"  ✗ Error inesperado: {e}")
            
            time.sleep(0.5)
        
        if muestras_actuales >= target:
            print(f"\n✓ ¡Objetivo alcanzado! Total muestras: {muestras_actuales}")
        else:
            print(f"\n✗ No se pudo alcanzar el objetivo. Muestras: {muestras_actuales}")
            
    finally:
        # Volver al directorio original
        os.chdir(original_dir)
        
        # Limpiar archivos .class si se solicita
        if limpiar_al_final:
            print("\n🧹 Limpiando archivos .class...")
            limpiar_class_files(project_path)

if __name__ == "__main__":
    # Usando raw string para la ruta de Windows
    ruta_proyecto = r"C:\Users\USER\Desktop\DASP\DASP\patrones de concurrencia\1. Sección Crítica - Fiabilidad de Hilos\CriticalSectionSTExercise"
    
    ejecutar_hasta_100_muestras(
        project_path=ruta_proyecto,
        java_file="ClientManager.java",  # Clase principal
        csv_file="logAnalisisSafeThread.csv",
        target=100
    )

    # Usando raw string para la ruta de Windows
    ruta_proyecto = r"C:\Users\USER\Desktop\DASP\DASP\patrones de concurrencia\2. Sección Crítica - Inicialización Temprana\CriticalSectionEarlyInitExercise"
    
    ejecutar_hasta_100_muestras(
        project_path=ruta_proyecto,
        java_file="ClientManager.java",  # Clase principal
        csv_file="logAnalisisSafeThread.csv",
        target=100
    )