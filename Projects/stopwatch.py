# A stopwatch that tracks the amount of time between hits
# of the "enter" key, with each key hit starting a new
# “lap” on the timer and Print the lap number, total time, and lap time.

import time
print("Hit \"enter\" to begin the program")
print("Hit \"enter\" again to the stopwatch")
input()
print("Program is already running")
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')
