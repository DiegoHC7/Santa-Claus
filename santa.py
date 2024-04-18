from threading import Semaphore, Thread
import time

elves_c = 0
reindeer_c = 0
santaSem = Semaphore()
reindeerSem = Semaphore()
elfTex = Semaphore()
mutex = Semaphore(1)


def prepararTrineo():
    global reindeer_c
    print("Santa Claus: preparando el trineo")


def ayudarElfos():
    print("Santa Claus: ayudando a los elfos")


def engancharTrineo():
    print("Este es el reno", reindeer_c)


def obtenerAyuda():
    print("Este es el elfo", elves_c)


def santa():
    global elves_c, reindeer_c
    print("Santa Claus: Hoho, aquí estoy")
    while True:
        santaSem.acquire()
        mutex.acquire()
        if reindeer_c >= 9:
            prepararTrineo()
            for i in range(9):
                reindeerSem.release()
            print("Santa Claus: haciendo felices a todos los niños del mundo")
            reindeer_c -= 9
            time.sleep(4)
        elif elves_c == 3:
            ayudarElfos()
        mutex.release()


def reno():
    global reindeer_c
    while True:
        mutex.acquire()
        reindeer_c += 1
        if reindeer_c == 9:
            santaSem.release()
        mutex.release()
        engancharTrineo()
        print("Reno", reindeer_c, "enganchándose al trineo")
        reindeerSem.acquire()
        time.sleep(2)  # Tiempo simulado de enganchar al trineo


def elfo():
    global elves_c
    while True:
        elfTex.acquire()
        mutex.acquire()
        elves_c += 1
        if elves_c == 3:
            santaSem.release()
        else:
            elfTex.release()
        mutex.release()
        obtenerAyuda()
        time.sleep(3)  # Tiempo simulado de obtener ayuda
        mutex.acquire()
        elves_c -= 1
        if elves_c == 0:
            elfTex.release()
        mutex.release()
        print("Elfo", elves_c, "trabajando")


def agregar_renos():
    global reindeer_c
    num_renos = int(input("¿Cuántos renos deseas agregar? "))
    mutex.acquire()
    reindeer_c += num_renos
    mutex.release()
    print(f"Se han agregado {num_renos} renos.")


def agregar_elfos():
    global elves_c
    num_elfos = int(input("¿Cuántos elfos deseas agregar? "))
    mutex.acquire()
    elves_c += num_elfos
    mutex.release()
    print(f"Se han agregado {num_elfos} elfos.")


hilos_elfos = []  # hilos para los elfos
hilos_renos = []  # hilos para los renos


def main():
    hilo = Thread(target=santa)  # hilo principal para Santa Claus
    hilo.start()  # iniciando el hilo

    while True:
        opcion = input("¿Deseas agregar renos (r) o elfos (e)? (Presiona 'q' para salir) ")
        if opcion == 'r':
            agregar_renos()
        elif opcion == 'e':
            agregar_elfos()
        elif opcion == 'q':
            break
        else:
            print("Opción inválida.")

    for i in range(9):
        hilos_renos.append(Thread(target=reno))
    for j in range(9):
        hilos_elfos.append(Thread(target=elfo))
    for t in hilos_elfos:
        t.start()
    for t in hilos_renos:
        t.start()
    for t in hilos_elfos:
        t.join()
    for t in hilos_renos:
        t.join()
    hilo.join()


main()
