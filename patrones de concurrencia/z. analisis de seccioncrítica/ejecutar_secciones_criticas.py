import subprocess
import os
import time
import glob

def compilar_java(project_path):
    """Compila todos los archivos Java en el directorio"""
    java_files = glob.glob(os.path.join(project_path, "*.java"))
    
    if not java_files:
        print(f"✗ No se encontraron archivos .java en {project_path}")
        return False
    
    print(f"Compilando {len(java_files)} archivo(s) Java...")
    for f in java_files:
        print(f"  - {os.path.basename(f)}")
    
    result = subprocess.run(['javac', '-encoding', 'UTF-8'] + java_files,
                            capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"✗ Error de compilación:\n{result.stderr}")
        return False
    
    print("✓ Compilación exitosa")
    return True

def limpiar_class_files(project_path):
    """Elimina todos los archivos .class generados"""
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

def ejecutar_n_veces(project_path, java_file="ClientManager.java",
                     veces=100, limpiar_al_final=True):
    """
    Ejecuta el programa Java un número fijo de veces.
    
    Args:
        project_path: Ruta al directorio del proyecto
        java_file: Nombre del archivo .java principal (sin ruta)
        veces: Número de ejecuciones a realizar
        limpiar_al_final: Si es True, elimina los archivos .class al terminar
    """
    csv_path = os.path.join(project_path, "logAnalisisSafeThread.csv")
    
    print(f"Proyecto en: {os.path.abspath(project_path)}")
    print(f"Archivo principal: {java_file}")
    print(f"Se ejecutará {veces} vez/veces")
    
    # Compilar antes de empezar
    if not compilar_java(project_path):
        print("No se puede continuar sin compilar correctamente")
        return
    
    original_dir = os.getcwd()
    os.chdir(project_path)
    
    class_name = java_file.replace('.java', '')
    
    try:
        for i in range(1, veces + 1):
            print(f"\nEjecución {i}/{veces}")
            
            try:
                result = subprocess.run(['java', class_name],
                                      capture_output=True,
                                      text=True,
                                      timeout=30)
                
                if result.returncode == 0:
                    print(f"  ✓ Ejecución {i} completada")
                    if result.stdout:
                        print(f"  Salida: {result.stdout[:200]}")
                else:
                    print(f"  ✗ Error en ejecución (código: {result.returncode})")
                    if result.stderr:
                        print(f"  Error: {result.stderr[:200]}")
                    if result.stdout:
                        print(f"  Salida: {result.stdout[:200]}")
                        
            except subprocess.TimeoutExpired:
                print(f"  ✗ Timeout - El programa tardó más de 30 segundos")
            except FileNotFoundError:
                print(f"  ✗ No se encuentra 'java'. ¿Tienes Java instalado?")
                break
            except Exception as e:
                print(f"  ✗ Error inesperado: {e}")
            
            time.sleep(0.5)  # Pequeña pausa entre ejecuciones
        
        print(f"\n✓ Se completaron {veces} ejecuciones.")
        
    finally:
        os.chdir(original_dir)
        if limpiar_al_final:
            print("\n🧹 Limpiando archivos .class...")
            limpiar_class_files(project_path)

if __name__ == "__main__":
    # Ejemplo: ejecutar 100 veces el programa en una ruta específica
    ruta_proyecto = r"C:\Users\Daniel_Dedalus\Desktop\DASP\DASP\patrones de concurrencia\1. Sección Crítica - Inicialización Temprana\CriticalSectionEarlyInitExercise"
    
    ejecutar_n_veces(
        project_path=ruta_proyecto,
        java_file="ClientManager.java",
        veces=100,
        limpiar_al_final=True
    )