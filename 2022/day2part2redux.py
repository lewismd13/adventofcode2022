input = open("day2input.txt", "r")

score = 0

# A = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win

input = input.readlines()

def rocks():
    rockinput = input
    rock_count = filter(lambda x: ('A Y' in x)|('B X' in x)|('C Z' in x), rockinput)
    return len(list(rock_count))

def papers():
    paper_input = input
    paper_count = filter(lambda x: ('A Z' in x)|('B Y' in x)|('C X' in x), paper_input)
    return len(list(paper_count))

def scissors():
    scissor_input = input
    scissor_count = filter(lambda x: ('A X' in x)|('B Z' in x)|('C Y' in x), scissor_input)
    return len(list(scissor_count))

wins = list(filter(lambda x: ('Z' in x), input))

losses = list(filter(lambda x: ('X' in x), input))

draws = list(filter(lambda x: ('Y' in x), input))

# loss_score = len(list(filter(lambda x: ('A' in x), losses))) * 3

print('Rocks: ', rocks())

score += rocks()

print('Papers: ', papers())

score += (papers() * 2)

print('Scissors: ', scissors())

score += (scissors() * 3)

print('Score so far: ', score)

print('Wins: ', len(wins))

score += ((len(wins)) * 6)

print('Draws: ', len(draws))

score += ((len(draws)) * 3)

print('Losses: ', len(losses))

print('Final score: ', score)