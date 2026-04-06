from utils import *
x1 =-200
y1 =200
x2 =-200
y2 =100
x3 =-200
y3 =20
x4 =-200
y4 =-150
set_background("race")
t1 = create_sprite("fox",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("turtle2",x3,y3)
t4 = create_sprite("puppy",x4,y4)



# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower: sprite 4 has the highest chance to win because its speed is the highest and sprite 2 is the slowest as its chances of getting a higher speed is unlikely compared to the rest.
for i in range(30):
    x1 += random.randint (10,20)
    x2 += random.randint (5,20)
    x3 += random.randint (7,20)
    x4 += random.randint (15,20)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("cat2",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x1 >= x4:
    s5.write("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x1 >= x4:
    s5.write("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x1 >= x3:
    s5.write("player 4 wins!")
  
#    



turtle.exitonclick()