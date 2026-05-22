# Evidencia Demonstración - Paradigmas de programación
## Planteamiento
### Contexto
En entornos urbanos con alto flujo vehicular, los sistemas de monitoreo de tráfico requieren procesar múltiples fuentes de información en tiempo real. Cámaras, sensores de velocidad y detectores de presencia generan datos de manera simultánea. Un sistema secuencial puede provocar retrasos en el análisis de eventos críticos como congestiones, accidentes o saturación de intersecciones.

Se implementará en python, utilizando herramientas nativas, un sistema de simulación para el monitorio de tráfico inteligente, utilizando mecanismso para mejorar el procesamiento de múltiples eventos simultáneos. 

### Alcance
El proyecto contempla:
- Simular múltiples sensores de trágico que generen datos simultáneamente
- Procesar, utilizando mecanismos de concurrencia, determinados eventos de entrada
- Generar alertas básicas de congestión
- Comparar la solución concurrente/paralela con una solución secuencial
- Medir tiempos de ejecución

El proyecto no contempla:
- Integración con hardware real ni bases de datos
- Interfaces avanzadas
- Comunicación distribuida entre múltiples equipos

## Paradigmas a utilizar
### Programación Concurrente
Para la gestión de los múltiples sensores que generan eventos y producen información simultáneamente (procesarlos en tiempo real), buscando evitar bloqueo del sistema principal. Cada sensor representará una tarea independiente.

Se utilizará:
- `threading`
- `queue`
- Bloqueos simples para sincronización

### Programación Paralela
Para llevar a cabo cálculos estadísticos sobre grandes conjuntos de datos de tráfico, en paralelo, buscando reducir el tiempo de procesamiento a través del aprovechamiento de múltiples núcleos del procesador.

Se utilizará:
- `multiprocessing`
- División de carga de trabajo entre procesos.

## Modelos
### Explicar la lógica, paradigma y arquitectura de la solución
La arquitectura propuesta sigue un modelo productor-consumidor, útil para separar a los procesos que producen datos, de aquellos que les consumen datos.  Bajo este patrón, se acopla el intercambio de información que se da entre distintos ciclos que corren a ritmo distinto.

#### Flujo lógico
1. Los sensores generan eventos de tráfico.
2. Cada sensor trabaja concurrentemente.
3. Los eventos se almacenan en una cola compartida.
4. Un consumidor central procesa los eventos.
5. Los datos acumulados se envían a procesos paralelos.
6. Los procesos calculan métricas de tráfico.
7. El sistema genera reportes y alertas.

#### Paradigma Concurrente
Cada sensor representa un hilo independiente que produce información de manera simultánea.

Ejemplo:
- Sensor A detecta 20 vehículos.
- Sensor B detecta 35 vehículos.
- Sensor C detecta reducción de velocidad.

Todos los eventos son generados al mismo tiempo y administrados mediante una cola compartida.

#### Paradigma Paralelo
Una vez recolectados los datos, el sistema divide el análisis estadístico entre varios procesos.

Cada proceso calcula tanto el promedio de velocidad, como la cantidad de vehículos, índices de congestión, y máximos y mínimos.

#### Arquitectura General
- Capa de generación de eventos.
- Cola compartida.
- Procesador concurrente.
- Motor paralelo de análisis.
- Generador de resultados.

### Diagramas
#### Diagrama de arquitectura
![](./Diagramas/Diagrama_secuencia.png)

#### Modelo productor-consumidor
![](./Diagramas/Diagrama_secuencia_2.png)

## Implementación
### Código
Dentro del archivo `monitorear_trafico.py`

## Pruebas
### Descripción
- Correcta ejecución concurrente de sensores.
- Correcta sincronización mediante colas.
- Procesamiento paralelo funcional.
- Reducción de tiempos respecto a una solución secuencial.

### Implementación y Documentación

#### Escenario de prueba
Se simularon 4 sensores y 10 eventos por sensor, esperando 40 eventos; y se evaluó el tiempo total de ejecución, eventos procesados correctamente y consistencia de resultados.

#### Evidencia esperada

Salida parcial:

```text
Sensor 0 generó: {'sensor': 0, 'vehiculos': 32, 'velocidad': 71}
Sensor 1 generó: {'sensor': 1, 'vehiculos': 50, 'velocidad': 99}
Sensor 2 generó: {'sensor': 2, 'vehiculos': 47, 'velocidad': 92}
Sensor 3 generó: {'sensor': 3, 'vehiculos': 18, 'velocidad': 78}
Procesando evento: {'sensor': 0, 'vehiculos': 32, 'velocidad': 71}
Procesando evento: {'sensor': 1, 'vehiculos': 50, 'velocidad': 99}
Procesando evento: {'sensor': 2, 'vehiculos': 47, 'velocidad': 92}
Procesando evento: {'sensor': 3, 'vehiculos': 18, 'velocidad': 78}
```
