from utils import *

# Section 1 - setup
set_background("money")

# TODO - create at least two variables and set their starting value. 
Money = 0 
Happiness = 0


# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()
m2 = create_sprite("alien", -200,170)
m2.hideturtle()





def get_money():
    global Money
    Money += 1
    x=random.randint (-200,200)
    y=random.randint (-200,200)
    create_sprite("money2",x,y)
window.onkeypress(get_money, "space")
# this key when press adds one money to the score so if you press "space" you should have one money 


def get_happiness():
   global Happiness
   if Money >= 5:
    Happiness += 1
    x=random.randint (-200,200)
    y=random.randint (-200,200)
    create_sprite("Happiness",x,y)
window.onkeypress(get_happiness, "s")
# this key when pressed adds one happiness to the score so if you press "s" you should have  one happiness








# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here 
    # the goal is to get as much money and happiness as you can 


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"I have {Money} money")
    m2.clear()
    m2.write(f"I have {Happiness} happiness")


    time.sleep(0.01)
    window.update()