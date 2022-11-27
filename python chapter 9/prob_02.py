# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hiscore.txt' Which either blank or contains the previous Hi-score. You need to write a program to update the Hi-score wehnever game() breaks the Hi-score.
def game():
    return 2222222
# score = game()
with open("Hiscore.txt", 'r') as f:
    data = f.read()
if data=="":
    with open("Hiscore.txt", 'w') as f:
        f.write(str(game()))
elif game()>int(data):
    with open('Hiscore.txt', 'w') as f:
        f.write(str(game()))
with open("Hiscore.txt") as f:
    c = f.read()
    print(c)