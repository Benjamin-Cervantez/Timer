def findTime():
    hours = float(input('How many hours do you have? '))
    minutes = float(input('How many minutes do you have? '))
    calculate(hours, minutes)
def calculate(hours, minutes):
    time = int(hours * 60 + minutes)
    temp = time
    shorts = int(0)
    longs = int(0)
    working = int(0)
    while temp > 0:
        for x in range(4):
            if temp > 0:
                temp -= 25
                working += 1
            if temp > 0:
                shorts += 1
                temp -= 5
        if temp > 0:
                temp -= 25
                working += 1
        if temp > 0:
            longs += 1
            temp -= 30
    final(time, working, shorts, longs)
def final(time, working, shorts, longs):
    print("You have " + str(time) + " total minutes.")
    print("You have " + str(working) + " total work sessions.")
    print("You have " + str(shorts) + " short breaks.")
    print("You have " + str(longs) + " long breaks.")
findTime()