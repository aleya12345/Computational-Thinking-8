sweet_points = 0
salty_points = 0
spicy_points = 0

answer1 = input("Do you prefer A chocolate, B doritos, or C takis?   ")
if answer1 == "A":
    sweet_points += 1
elif answer1 == "B":
    salty_points += 1
elif answer1 == "C":
    spicy_points += 1

answer2 = input("Do you prefer A skittles, B potato chips, or C hot tamales?   ")
if answer2 == "A" or answer2 == "a":
    sweet_points += 1
elif answer2 == "B":
    salty_points += 1
elif answer2 == "C":
    spicy_points += 1

answer3 = input("Do you prefer A ice cream, B fries, or C hot cheetos?   ")
if answer3 == "A":
    sweet_points += 1
elif answer3 == "B":
    salty_points += 1
elif answer3 == "C":
    spicy_points += 1

answer4 = input("Do you prefer A reeses, B popcorn, or C hot wings?   ")
if answer4 == "A":
    sweet_points += 1
elif answer4 == "B":
    salty_points += 1
elif answer4 == "C":
    spicy_points += 1

answer5 = input("Do you prefer A cookies, B pretzels, or C chips and salsa?   ")
if answer5 == "A":
    sweet_points += 1
elif answer5 == "B":
    salty_points += 1
elif answer5 == "C":
    spicy_points += 1

print(f"Your score is {sweet_points} sweet, {salty_points} salty, and {spicy_points} spicy")
if sweet_points > salty_points and sweet_points > spicy_points:
    print("you are a sweet food person candy and dessert is your thing.")
if salty_points > sweet_points and salty_points > spicy_points:
    print("you are a salty person and foods like chips or sandwiches are your favorite")
if spicy_points > salty_points and spicy_points > sweet_points:
    print("you are a spicy person and spicy foods are your favorite.")





