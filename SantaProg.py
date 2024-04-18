import threading
import time
import random

# Clase para representar a los duendes
class Duende(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        print(f"Duende {self.nombre}: Trabajando duro en el taller.")


    def run(self):
        print("Santa: Durmiendo en el Polo Norte.")
        while True:
            time.sleep(2)
            print("Santa: Me estoy despertando...")
            time.sleep(2)
            print("Santa: Revisando el buzón de cartas.")
            time.sleep(2)
            print("Santa: Preparándome para trabajar.")
            time.sleep(2)
            print("Santa: Reunión con los duendes.")
            time.sleep(2)
            print("Santa: Reunión con los renos.")
            time.sleep(2)
            print("Santa: Empacando los regalos.")
            time.sleep(2)
            print("Santa: ¡Hora de repartir regalos!")
            time.sleep(5)
            print("Santa: Regresando al Polo Norte.")

# Crear instancias de Santa, renos y duendes
duendes = [Duende(nombre) for nombre in ["Alfa", "Beta", "Gamma", "Delta", "Épsilon"]]

# Iniciar los hilos
for duende in duendes:
    duende.start()

# Esperar a que todos los hilos terminen
for duende in duendes:
    duende.join()

print("¡El trabajo de Navidad ha terminado!")
