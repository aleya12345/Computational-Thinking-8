# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("images")

s1 = create_sprite("nina", -200, 0)
s2 = create_sprite("royce", 200, 0)

s1.color("blue")
s2.color("dark red")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("in the best place ever!",font = ("Arial", 10, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("i miss them so much i just want to give them a big fat hug",font = ("Arial", 10, "normal"))
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()