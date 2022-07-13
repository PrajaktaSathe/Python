# stopwatch.py - A stopwatch that tracks the amount of time between hits of the "Enter" key,
# with each key hit starting a new “lap” on the timer and prints the lap number, total time, and lap time.
# multithreading is used to display a timer whilst the stopwatch is working.

import time
import datetime
import threading

# Instructions
print(" Stopwatch ".center(30, "*"))
print("Hit \"Enter\" to begin the program.")
input()
print("Program is already running.")
print("Hit \"Enter\" again to create laps.")
print("Press 'Ctrl' + 'C' to end the program.")


# Count up timer function.
def countUp():
    """A count up timer which would be displayed while the stopwatch is ongoing."""
    second = 1

    try:
        while True:
            time.sleep(1)
            print(datetime.timedelta(seconds=second), end="\r")
            second += 1
    except KeyboardInterrupt:
        pass


# Stopwatch function.
def stopwatch():
    """Displays laps when the user presses the 'Enter' button."""

    startTime = time.time()
    lastTime = startTime
    lapNum = 1

    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime))
            print()
            lapNum += 1
            lastTime = time.time()  # reset the last lap time
    except EOFError:
        print("\nDone.")


# Calling the functions.
threadObj = threading.Thread(target=stopwatch)  # Creating a multithreading object whose target is stopWatch().
threadObj.start()  # Start the stopWatch() function.
countUp()
