import time
import os
import threading

file_name = 'test.txt'


def create_file(name: str):
    with open(name, 'w') as file:
        file.write('This is a test file.\nWow!\nThis is another line.')


def remove_file(name: str):
    event.wait()
    os.remove(name)


def find_wow_in_file(name: str):
    while True:
        if not os.path.exists(name):
            time.sleep(5)
        else:
            with open(name, 'r') as file:
                if 'Wow!' in file.read():
                    event.set()
                    break
                else:
                    time.sleep(5)


create_file(file_name)


event = threading.Event()


thread1 = threading.Thread(target=find_wow_in_file, args=(file_name,))
thread2 = threading.Thread(target=remove_file, args=(file_name,))


thread1.start()
thread2.start()

thread1.join()
thread2.join()

