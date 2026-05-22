import threading, multiprocessing, queue, random, time

cola_eventos = queue.Queue()
datos_trafico = []

# PARTE CONCURRENTE

def sensor(sensor_id):
    for _ in range(10):
        evento = {
            "sensor": sensor_id,
            "vehiculos": random.randint(5, 50),
            "velocidad": random.randint(20, 100)
        }

        cola_eventos.put(evento)
        print(f"Sensor {sensor_id} generó: {evento}")
        time.sleep(random.uniform(0.2, 1))


def consumidor():
    while True:
        try:
            evento = cola_eventos.get(timeout=5)
            datos_trafico.append(evento)
            print(f"Procesando evento: {evento}")
            cola_eventos.task_done()
        except:
            break

# PARTE PARALELA

def calcular_promedio(datos):
    promedio = sum(d["velocidad"] for d in datos) / len(datos)
    return promedio


def calcular_total_vehiculos(datos):
    total = sum(d["vehiculos"] for d in datos)
    return total


if __name__ == "__main__":

    sensores = []

    for i in range(4):
        hilo = threading.Thread(target=sensor, args=(i,))
        sensores.append(hilo)
        hilo.start()

    hilo_consumidor = threading.Thread(target=consumidor)
    hilo_consumidor.start()

    for hilo in sensores:
        hilo.join()

    cola_eventos.join()
    hilo_consumidor.join()

    print(f"\nDatos recolectados: {datos_trafico}")

    # Procesamiento paralelo
    with multiprocessing.Pool(processes=2) as pool:
        resultado_promedio = pool.apply(
            calcular_promedio,
            args=(datos_trafico,)
        )

        resultado_total = pool.apply(
            calcular_total_vehiculos,
            args=(datos_trafico,)
        )

    print("\nRESULTADOS")
    print(f"Velocidad promedio: {resultado_promedio}")
    print(f"Total de vehículos: {resultado_total}")
