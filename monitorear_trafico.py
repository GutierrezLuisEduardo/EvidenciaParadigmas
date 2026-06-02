import threading
import multiprocessing
import queue
import random
import time
import argparse

# ARGUMENTOS POR CONSOLA
parser = argparse.ArgumentParser(
    description="Sistema Monitor de Tráfico, Concurrente y Paralelo"
    )
parser.add_argument(
    '--vehiculos', type=int, default=10,
    help='Número de eventos/vehículos que genera cada sensor'
    )
parser.add_argument(
    '--sensores', type=int, default=4,
    help='Número de sensores')
parser.add_argument(
    '--output', type=str, default='log_concurrente.txt',
    help='Nombre del archivo de salida')

args = parser.parse_args()

# VARIABLES GLOBALES
cola_eventos = queue.Queue()
datos_trafico = []
output_lines = []

# PARTE CONCURRENTE
def sensor(sensor_id):
    for _ in range(args.vehiculos):
        evento = {
            "sensor": sensor_id,
            "vehiculos": random.randint(5, 50),
            "velocidad": random.randint(20, 100)
        }
        cola_eventos.put(evento)
        time.sleep(random.uniform(0.2, 1.0))


def consumidor():
    while True:
        try:
            evento = cola_eventos.get(timeout=8)
            datos_trafico.append(evento)
            output_lines.append(
                
                str(evento)
                )
            cola_eventos.task_done()
        except:
            break


# PARTE PARALELA
def calcular_promedio(datos):
    if not datos:
        return 0
    return sum(d["velocidad"] for d in datos) / len(datos)


def calcular_total_vehiculos(datos):
    return sum(d["vehiculos"] for d in datos)


# FUNCIÓN PRINCIPAL
def main():
    inicio = time.time()

    output_lines.append(
        f"Iniciando simulación con {args.sensores} sensores y "
        + f"{args.vehiculos} eventos por sensor.\n"
    )

    # Iniciar sensores
    sensores = []
    for i in range(args.sensores):
        hilo = threading.Thread(target=sensor, args=(i,))
        sensores.append(hilo)
        hilo.start()

    hilo_consumidor = threading.Thread(target=consumidor)
    hilo_consumidor.start()

    # Esperar a que terminen los sensores
    for hilo in sensores:
        hilo.join()

    cola_eventos.join()
    hilo_consumidor.join()

    output_lines.append(
        f"Datos recolectados: {len(datos_trafico)} eventos\n"
    )

    # Procesamiento paralelo
    with multiprocessing.Pool(processes=2) as pool:
        velocidad_promedio = pool.apply(
            calcular_promedio, (datos_trafico,)
        )

        total_vehiculos = pool.apply(
            calcular_total_vehiculos, (datos_trafico,)
        )

    fin = time.time()
    tiempo_total = fin - inicio

    # Resultados finales
    output_lines.append("="*50)
    output_lines.append("RESULTADOS FINALES")
    output_lines.append("="*50)
    output_lines.append(f"Velocidad promedio: {velocidad_promedio:.2f} km/h")
    output_lines.append(f"Total de vehículos: {total_vehiculos}")
    output_lines.append(f"Tiempo total de ejecución: {tiempo_total:.2f} segundos")

    # Guardar todo en archivo
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))

    # Retornar, como tripleta, los detalles de simulación
    return f"{tiempo_total}, {velocidad_promedio}, {total_vehiculos}"


# EJECUCIÓN
if __name__ == "__main__":
    resultado = main()
    print(resultado)