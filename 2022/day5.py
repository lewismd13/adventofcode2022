import re

rawinput = open("2022\day5input.txt", "r")

input = list(rawinput)

stacks = {
    1: "HTZD",
    2: "QRWTGCS",
    3: "PBFQNRCH",
    4: "LCNFHZ",
    5: "GLFQS",
    6: "VPWZBRCS",
    7: "ZFJ",
    8: "DLVZRHQ",
    9: "BHGNFZLD"
}

i = 0
for crate in input:
    i += 1
    # if i > 20: break
    if "move" in crate:
        origin = re.search("(?:from )(\d+)", crate)
        origin = int(origin.group(1))
        destination = re.search("(?:to )(\d+)", crate)
        destination = int(destination.group(1))
        quantity = re.search("(?:move )(\d+)", crate)
        quantity = int(quantity.group(1))
        print(f"we are moving {quantity} crates from stack {origin} to stack {destination}")
        intransit = stacks[origin]
        print('Stack is currently ', intransit)
        intransit = intransit[-quantity:]
        print("moving ", intransit)
        print('origin stack was ', stacks[origin])
        stacks[origin] = stacks.get(origin)[:-quantity]
        print('origin stack is now ', stacks[origin])
        print('destination stack was', stacks[destination])
        # intransit = intransit[::-1]
        stacks[destination] = stacks[destination] + intransit
        print('destination stack is now', stacks[destination])

print(stacks)
answer = ""
for thing in stacks:
    print(f"the top letter in stack {thing} is {stacks.get(thing)[-1:]}")
    answer += stacks.get(thing)[-1:]
print("your answer is, therefore: ", answer)
"""
i = 1

for crate in input:
    if "move" in crate:
        break
    else:
        cratenum = (i - 3) / 4
        print("Item in crate number ", cratenum)
        if re.search('\D', crate[cratenum]):
            cratenum = (i - 3) / 4
            print("Item in crate number ", cratenum)
            print("There's a %s crate in this slot" % crate[1])
            stackvalue = stacks.get(i)
            print('Current stack: ', stackvalue)
            stackvalue = stackvalue + crate[cratenum]
            print('New stack: ', stackvalue)
            stacks.update({1: stackvalue})
            i += 1
        else: break

"""