class Remote:
    pass           

class Player():
    def moveright(self):
        pass
    def moveleft(self):
        pass
    def moveup(self):
        pass
    def movedown(self):
        pass
remote1 = Remote() # here remote1 is an object because it instantiate the class Remote

player1 = Player() # here player1 is an object because it instantiate the class Player

if(remote1.isLeftPressed()):
    player1.moveleft()