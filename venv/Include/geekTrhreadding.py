# Python program to illustrate the concept
# of threading importing the threading module
# https://www.geeksforgeeks.org/multithreading-python-set-1/
import threading, time

def print_cube(num):
    for x in range(5):
        print('Cube: ' + str(num * num) + ' x= ' + str(x))
        time.sleep(1)
        text = input('Type something here:\n')

def print_square(num):
    for x in range(10):
        print('Square: ' + str(num * num) + ' x= ' + str(x))
        time.sleep(1)
        if x == 4:
            break

thread1 = threading.Thread(target=print_square, args=(10,))
thread2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
thread1.start()
# starting thread 2
thread2.start()

# wait until thread 1 is completely executed
thread1.join()
# wait until thread 2 is completely executed
thread2.join()

# both threads completely executed
print("Done!")