import threading
import time
import random

# Constantes
NUM_RENOS = 9
NUM_DUENDES = 5
CAPACIDAD_TALLER = 3
NUM_TRABAJOS_DUENDES = 10

# Semáforos
sem_santa = threading.Semaphore(0)  # Semáforo para que Santa espere hasta que sea llamado
sem_renos = threading.Semaphore(0)  # Semáforo para que Santa espere a que lleguen suficientes renos
sem_taller = threading.Semaphore(CAPACIDAD_TALLER)  # Semáforo para controlar el acceso al taller
sem_duendes = threading.Semaphore(0)  # Semáforo para que los duendes puedan llamar a Santa

# Mutex
mutex = threading.Lock()  # Mutex para proteger la variable de conteo de renos

# Variables compartidas
renos_listos = 0

# Clase para representar a los renos
class Reno(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global renos_listos
        print(f"Reno {self.nombre}: Esperando en el establo.")
        time.sleep(random.randint(1, 5))  # Simular el tiempo de llegada de los renos al establo
        print(f"Reno {self.nombre}: Listo para partir hacia el Polo Norte.")
        
        mutex.acquire()
        renos_listos += 1
        if renos_listos == NUM_RENOS:
            sem_renos.release()  # Despertar a Santa si todos los renos están listos
        mutex.release()

# Clase para representar a los duendes
class Duende(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        for _ in range(NUM_TRABAJOS_DUENDES):
            print(f"Duende {self.nombre}: Trabajando duro en el taller.")
            time.sleep(random.randint(1, 3))  # Simular el tiempo de trabajo en el taller
            sem_duendes.release()  # Despertar a Santa para que atienda a los duendes

# Clase para representar a Santa
class Santa(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print("Santa: Durmiendo en el Polo Norte.")
            sem_santa.acquire()  # Esperar a que un duende o un reno despierte a Santa
            
            if renos_listos == NUM_RENOS:
                print("Santa: ¡Preparando el trineo y los regalos!")
                time.sleep(2)
                print("Santa: ¡Es hora de partir hacia el mundo!")
                time.sleep(5)
                print("Santa: ¡Misión cumplida! Regresando al Polo Norte.")
                sem_renos.release()  # Permitir que los renos vuelvan al establo
                renos_listos = 0  # Reiniciar el conteo de renos
            else:
                print("Santa: ¡Reunión con los duendes!")
                time.sleep(3)
                sem_taller.release()  # Liberar espacio en el taller para los duendes
                print("Santa: ¡Reunión finalizada! Volviendo a dormir.")

# Crear instancias de Santa, renos y duendes
santa = Santa()
duendes = [Duende(nombre) for nombre in range(1, NUM_DUENDES + 1)]
renos = [Reno(nombre) for nombre in range(1, NUM_RENOS + 1)]

# Iniciar los hilos
santa.start()
for duende in duendes:
    duende.start()
for reno in renos:
    reno.start()

# Simular el trabajo continuo de los duendes
while True:
    sem_duendes.acquire()  # Esperar a que un duende necesite la ayuda de Santa
    sem_santa.release()  # Despertar a Santa para que atienda a los duendes
    sem_taller.acquire()  # Esperar a que un duende termine su trabajo para liberar espacio en el taller
