import threading
import time
import random

# Clase para representar a los renos
class Reno(threading.Thread):
    def _init_(self, nombre):
        super()._init_()
        self.nombre = nombre

    def run(self):
        print(f"Reno {self.nombre}: Esperando en el establo.")
        time.sleep(random.randint(1, 5))
        print(f"Reno {self.nombre}: Listo para volar!")

# Clase para representar a los duendes
class Duende(threading.Thread):
    def _init_(self, nombre):
        super()._init_()
        self.nombre = nombre

    def run(self):
        print(f"Duende {self.nombre}: Trabajando duro en el taller.")

# Clase para representar a Santa
class Santa(threading.Thread):
    def _init_(self):
        super()._init_()

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
santa = Santa()
renos = [Reno(nombre) for nombre in ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen"]]
duendes = [Duende(nombre) for nombre in ["Alfa", "Beta", "Gamma", "Delta", "Épsilon"]]

# Iniciar los hilos
santa.start()
for reno in renos:
    reno.start()
for duende in duendes:
    duende.start()

# Esperar a que todos los hilos terminen
santa.join()
for reno in renos:
    reno.join()
for duende in duendes:
    duende.join()

print("¡El trabajo de Navidad ha terminado!")
