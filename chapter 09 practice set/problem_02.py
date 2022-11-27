# The game() funtion in a program lets a user play a game and returns the score as an integer. You need to read a file "Hiscoore.txt' which is either blank
# or contains the previous Hi-score You need to write a program to update the Hi-score whever game() breaks the Hi-score
def game():
    pass
Hiscore = 1
with open("Hi-score.txt", 'r') as f:
    a = f.read()
    if a == "":
        with open("Hi-score.txt", 'w') as f:
            f.write(str(Hiscore))
    elif Hiscore>int(a):
        with open("Hi-score.txt", 'w') as f:
            f.write(str(Hiscore))
    

