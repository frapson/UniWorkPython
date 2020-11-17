TeamName = input("Enter a name of football team: ")
print("Enter results in 0:0 format")
results = []
for i in range(1, 6):
    print("Score #" + str(i))
    results.append(input())

##array is a list of match results
def win(array):
    wins = 0
    for i in array:
        if int(i[0]) > int(i[2]):
            wins += 1
    return wins


def draw(array):
    draws = 0
    for i in array:
        if int(i[0]) == int(i[2]):
            draws += 1
    return draws


def loss(array):
    losses = 0
    for i in array:
        if int(i[0]) < int(i[2]):
            losses += 1
    return losses


def point(wins, draws):
    points = wins * 3 + draws
    return points


print(TeamName + "\n" +
      "Wins    " + str(win(results)) + "\n" +
      "Losses  " + str(loss(results)) + "\n" +
      "Draws   " + str(draw(results)) + "\n" +
      "Points: " + str(point(win(results), draw(results))))
