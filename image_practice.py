# Section 1 - Your code
from utils import *
set_background("mountain")

s1 = create_sprite("dog", 120, 105)
s2 = create_sprite("monkey", -150, 100)
s2 = create_sprite("fish", -70, -100)
s2 = create_sprite("turtle", 100, -100)
s2 = create_sprite("puppy", 150, -20)


message1 = create_sprite("alien",-200,200)
message1.color("blue")
message1.write("hello",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()