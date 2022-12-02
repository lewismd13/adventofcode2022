input = open("day2input.txt", "r")

score = 0

# A = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win


i = 0
for round in input:
    i +=1
    print('Round %s' % i)
    round_score = 0
    # 0 points for losing
    if 'X' in round:
        # opponent chose rock, we must choose scissors
        if 'A' in round:
            print("We pick scissors to lose, 3 points")
            round_score += 3
        # opponent chose paper, we must choose rock
        elif 'B' in round:
            print('We pick Rock to lose, 1 point')
            round_score += 1
        # opponent chose scissors, we must choose paper
        elif 'C' in round:
            print("We pick paper to lose, 2 points")
            round_score += 2
    # 3 points for a draw
    elif 'Y' in round:
        round_score += 3
        # opponent chose rock, so do we
        if 'A' in round:
            print("We pick rock to draw, 1 point")
            round_score += 1
        # opponent chose paper, so do we
        elif 'B' in round:
            print("We pick paper to draw, 2 points")
            round_score += 2
        # opponent chose scissors, so do we
        elif 'C' in round:
            print('We pick scissors to draw, 3 points')
            round_score += 3
    # 6 points for winning
    elif 'Z' in round:
        round_score += 6
        # opponent chose rock, we must choose paper
        if 'A' in round:
            print("We pick paper to win, 2 points")
            round_score += 2
        # opponent chose paper, we must choose scissors
        elif 'B' in round:
            print("We pick scissors to win, 3 points")
            round_score += 3
        # opponent chose scissors, we must choose rock
        elif 'C' in round:
            print('We pick rock to win, 1 point')
            round_score += 1
    print('Round Score: %s' % round_score)
    score += round_score
    print('Cumulative Score: %s' % score)
print('Final Score: %s' % score)
input.close()