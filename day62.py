# Multithreading in `Python` can be achieved using the `threading` module. Below is an example of how to create and run multiple threads in Python.

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2: {letter}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
# Start threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
print("Both threads have finished execution.")
