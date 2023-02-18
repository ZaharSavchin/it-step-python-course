from threading import Thread
from time import sleep

task = input('enter your task: ')
time_for_relax = int(input('enter time for relax in seconds: '))
FLAG = True


def timer(massage, time):
    global FLAG
    sleep(time)
    print(massage)
    FLAG = False


def relax(message: str, time):
    while FLAG:
        print(message)
        sleep(time)


worker = Thread(target=timer, args=(task, time_for_relax))
relaxer = Thread(target=relax, args=('stay relaxed', 1))

worker.start()
relaxer.start()








