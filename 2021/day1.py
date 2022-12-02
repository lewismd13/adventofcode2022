input = open("2021\day1input2021.txt", "r")

answer = 0

lastinput: int = None
print(bool(lastinput))

for measurement in input:
    if measurement != "\n" and lastinput:
        print("Previous: " + str(lastinput))
        print("Current: " + measurement)
        measurement = int(measurement)
        lastinput = int(lastinput)
        if measurement > lastinput:
            answer += 1
            print("Increase! that's " + str(answer))
    else:
        print("Nope")
    lastinput = measurement
