# Multiprocessing in python
# Multiprocessing allows you to run multiple processes simultaneously, which can be useful for CPU-bound tasks. 
# The `multiprocessing` module provides a simple way to create and manage separate processes in Python.

import multiprocessing
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Process 1: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Process 2: {letter}")
        time.sleep(1)

if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)
    # Start processes
    process1.start()
    process2.start()
    # Wait for both processes to finish
    process1.join()
    process2.join()
    print("Both processes have finished execution.")


#anorher example of multiprocessing using Pool

def square(n):
    return n * n

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(square, numbers)
    print("Squared numbers:", results)


    




