import subprocess
import os
import time
import glob

def count_csv_rows(csv_filename):
    """Cuenta cuántas filas de datos tiene el CSV (excluyendo cabecera)"""
    if not os.path.exists(csv_filename):
        return 0
    
    with open(csv_filename, 'r') as csvfile:
        # Restar 1 por la cabecera
        return max(0, sum(1 for line in csvfile) - 1)

def compilar_todos_java():
    """Compila todos los archivos .java en el directorio actual"""
    java_files = glob.glob("*.java")
    
    if not java_files:
        print(f"✗ No se encontraron archivos .java en el directorio actual")
        print(f"  Directorio actual: {os.getcwd()}")
        return False
    
    print(f"Archivos Java encontrados: {', '.join(java_files)}")
    print(f"Compilando todos los archivos...")
    
    # Compilar todos los archivos .java juntos
    result = subprocess.run(['javac'] + java_files, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"✗ Error de compilación:")
        print(result.stderr)
        return False
    
    print("✓ Compilación exitosa")
    return True

def ejecutar_hasta_100_muestras():
    csv_file = "logAnalisisSafeThread.csv"
    target = 100
    
    print(f"Objetivo: Al menos {target} muestras en {csv_file}")
    print(f"Directorio de trabajo: {os.getcwd()}")
    
    # Compilar todos los Java files antes de empezar
    if not compilar_todos_java():
        print("No se puede continuar sin compilar correctamente")
        return
    
    # Verificar cuántas muestras ya existen
    muestras_actuales = count_csv_rows(csv_file)
    print(f"Muestras actuales: {muestras_actuales}")
    
    if muestras_actuales >= target:
        print(f"¡Ya hay suficientes muestras ({muestras_actuales})!")
        return
    
    ejecucion = 0
    while muestras_actuales < target:
        ejecucion += 1
        print(f"\nEjecución #{ejecucion} - Muestras: {muestras_actuales}/{target}")
        
        # Ejecutar el programa Java (la clase principal es ClientManager)
        try:
            result = subprocess.run(['java', 'ClientManager'], 
                                  capture_output=True, 
                                  text=True,
                                  timeout=30)
            
            if result.returncode == 0:
                nuevas_muestras = count_csv_rows(csv_file)
                if nuevas_muestras > muestras_actuales:
                    nuevas = nuevas_muestras - muestras_actuales
                    print(f"  ✓ Nuevas muestras: {nuevas}")
                    muestras_actuales = nuevas_muestras
                else:
                    print(f"  ⚠ El programa se ejecutó pero no agregó nuevas muestras")
                    if result.stdout:
                        print(f"  Salida: {result.stdout[:200]}")
            else:
                print(f"  ✗ Error en ejecución (código: {result.returncode})")
                if result.stderr:
                    print(f"  Error: {result.stderr[:300]}")
                if result.stdout:
                    print(f"  Salida: {result.stdout[:200]}")
                
        except subprocess.TimeoutExpired:
            print(f"  ✗ Timeout - El programa tardó más de 30 segundos")
        except FileNotFoundError:
            print(f"  ✗ No se encuentra el comando 'java'")
            print(f"  Verifica que Java esté instalado y en el PATH")
            break
        except Exception as e:
            print(f"  ✗ Error inesperado: {e}")
        
        # Pequeña pausa entre ejecuciones
        time.sleep(0.5)
    
    if muestras_actuales >= target:
        print(f"\n✓ ¡Objetivo alcanzado! Total muestras: {muestras_actuales}")
    else:
        print(f"\n✗ No se pudo alcanzar el objetivo. Muestras: {muestras_actuales}")

if __name__ == "__main__":
    ejecutar_hasta_100_muestras()