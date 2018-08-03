# first_name = "Logan"
# last_name = "Chardderdon"
# age = 26
# greeting = first_name + " " + last_name + "is" + str(age) + "years old"
# greetings2 = "%s %s is %s years old"
# greetings2 = "%s %s is %s years old" % (first_name, last_name, age)
# print(greetings2)
# "%s %s is %s years old" % (1, 2, 3)
import r

class Player(object):
    def __init__(self, name):
        self.name = name

    def war_cry(self):
        print("%s says ahhhh!" % (self.name))

my_player1 = Player("Mario")
my_player2 = Player("Kratos")
my_player3 = Player("Link")

my_player1.war_cry()
my_player2.war_cry()
my_player3.war_cry()
