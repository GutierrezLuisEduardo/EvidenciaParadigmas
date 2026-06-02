import random
import time
import argparse

# ARGUMENTOS POR CONSOLA
parser = argparse.ArgumentParser(
    description="Sistema Monitor de Tráfico, Secuencial"
    )
parser.add_argument(
    '--vehiculos', type=int, default=10,
    help='Número de eventos/vehículos que genera cada sensor'
    )
parser.add_argument(
    '--sensores', type=int, default=4,
    help='Número de sensores')
parser.add_argument(
    '--output', type=str, default='log_secuencial.txt',
    help='Nombre del archivo de salida')

args = parser.parse_args()


datos_trafico = []

# SIMULACIÓN SECUENCIAL
def simular_sensor(sensor_id):
    for _ in range(args.vehiculos):
        evento = {
            "sensor": sensor_id,
            "vehiculos": random.randint(5, 50),
            "velocidad": random.randint(20, 100)
        }
        datos_trafico.append(evento)
        time.sleep(random.uniform(0.2, 1.0))


def calcular_promedio(datos):
    if not datos:
        return 0
    return sum(d["velocidad"] for d in datos) / len(datos)


def calcular_total_vehiculos(datos):
    return sum(d["vehiculos"] for d in datos)


def main():
    output_lines = []
    output_lines.append(f"Iniciando versión SECUENCIAL con \
        {args.sensores} sensores y {args.vehiculos} eventos por sensor.\n")
    
    inicio = time.time()

    # Ejecución secuencial
    for i in range(args.sensores):
        for _ in range(args.vehiculos):
            evento = {
                "sensor": i,
                "vehiculos": random.randint(5, 50),
                "velocidad": random.randint(20, 100)
            }
            datos_trafico.append(evento)
            output_lines.append(f"Sensor {i} generó: {evento}")
            time.sleep(random.uniform(0.2, 1.0))

    fin = time.time()
    tiempo_total = fin - inicio

    # Cálculos
    prom = calcular_promedio(datos_trafico)
    total = calcular_total_vehiculos(datos_trafico)

    # Preparando los resultados
    output_lines.append("\n" + "="*50)
    output_lines.append("RESULTADOS - VERSIÓN SECUENCIAL")
    output_lines.append("="*50)
    output_lines.append(f"Velocidad promedio: {prom:.2f} km/h")
    output_lines.append(f"Total de vehículos: {total}")
    output_lines.append(f"Tiempo total de ejecución: \
        {tiempo_total:.2f} segundos")

    # Guardar en archivo
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    # Retornar, como tripleta, los detalles de simulación
    return f"{tiempo_total}, {prom}, {total}"


if __name__ == "__main__":
    resultado = main()
    print(resultado)