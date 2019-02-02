from City import City

problems = ['a_example.in', 'b_should_be_easy.in', 'c_no_hurry.in', 'd_metropolis.in', 'e_high_bonus.in']
totalScore = 0

for filename in problems:
    city = City('inputs/' + filename)
    city.runTime()
    city.saveOutput()

    score = city.getTotalScore()
    totalScore += score

    print("For", filename, "your score is", score)

print("Your global score is", totalScore)
