import subprocess

def main():

    seccion = "="*50 + "\n"
    n_sensores = [1,2,3,6,8]
    n_vehiculos = [15,15,35,50,50]
    
    for i in range(len(n_sensores)):
        print(seccion)
        print(f"PRUEBA {i+1}:\n") 
        print(f"Número de sensores: {n_sensores[i]}\n")
        print(f"Número de vehículos: {n_vehiculos[i]}\n") 

        print("Ejecutando sistema concurrente...\n")
        concurrente = subprocess.run(
            ["python",
                "monitorear_trafico.py",
                "--vehiculos",
                str(n_vehiculos[i]),
                "--sensores",
                str(n_sensores[i]),
                "--output",
                f"logs_concurrencia_prueba_{i+1}.txt"
            ],
            capture_output=True, text=True, check=True
        )
        print("Terminada la ejecución\n")

        print("Ejecutando sistema secuencial...\n")
        secuencial = subprocess.run(
            ["python",
                "secuencial_trafico.py",
                "--vehiculos",
                str(n_vehiculos[i]),
                "--sensores",
                str(n_sensores[i]),
                "--output",
                f"logs_secuencial_prueba_{i+1}.txt"
            ],
            capture_output=True, text=True, check=True
        )
        print("Terminada la ejecución\n")

        resultado_c = concurrente.stdout.strip()
        resultado_s = secuencial.stdout.strip()

        tiempo_c, promedio_c, total_c = resultado_c.split(", ")
        tiempo_s, promedio_s, total_s = resultado_s.split(", ")

        print(seccion)
        print("Resultados de concurrente")
        print(seccion)
        print(f"Tiempo: {tiempo_c}\n")
        print(f"Promedio de velocidad: {promedio_c}\n")
        print(f"Total de vehículos: {total_c}\n")

        print(seccion)
        print("Resultados de secuencial")
        print(seccion)
        print(f"Tiempo: {tiempo_s}\n")
        print(f"Promedio de velocidad: {promedio_s}\n")
        print(f"Total de vehículos: {total_s}\n")

        print("\n"*4)
        print(seccion)

        if float(tiempo_c) < float(tiempo_s):
            print("Solución CONCURRENTE demostró ser óptima.")
        else: 
            print("Solución SECUENCIAL demostró ser óptima.")
        
        print(seccion)
        print("\n"*4)

if __name__ == "__main__":
    main()