# Daily water reminder program with beep sound


import time
import winsound
def remind_to_drink_water():

    while True:
        print("Time to drink water! Stay hydrated!")
        winsound.Beep(1000, 1000)  # Beep sound (frequency, duration)
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    remind_to_drink_water()

    