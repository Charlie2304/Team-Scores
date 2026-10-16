# [Player Scores]
# [Charlie Smith]
# [12/12/25]
# AS Computer Science

# Global Variables

redtotal = 0
greentotal = 0
player = [[1, 45],
          [2, 30],
          [2, 46],
          [1, 31],
          [1, 10],
          [1, 32],
          [2, 2]]

for i in range(len(player)):
    if (player[i][0] == 1):
        greentotal = greentotal + player[i][1]

    elif (player[i][0] == 2):
        redtotal = redtotal + player[i][1]

print("Red teams total score is:", redtotal)
print("Green teams total score is", greentotal)
