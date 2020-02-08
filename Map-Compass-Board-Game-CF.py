print("Map & Compass Board Game \nClara F '23")

print("""
Instructions: 
Start at the entrance. Choose a destination and collect the colored coins.

Chocolate house (pink)
Boba pond (orange)
Oreo Castle (blue)
M&M beach (yellow)

All the coins are on the way. Players need to go to the way that has their coins on it. They need to read the whole map (the board) 
first to make sure they are always on the right way. They will make several decisions. If they fall on anything, the game will be over. 
There are numbers on the different ways when people need to choose which way to go. When the players get into the place "somewhere", 
they need to click on the next section. There will be a count-down. After the 10 seconds count-down, someone needs to click on the last 
section. The player needs to choose a way and follow the way to get into the destiny they chose. If they didn’t get into the one they 
chose, they will fail this game.)

""")

def BE1():
  print ("you keep walking and fall down the cliff")
def BE2():
  print ("A ghost kills you")
destination = input("Welcome to the forest. Now you are in the entrance of the forest. Choose a destination. \n1:Chocolate House. \n2:Boba Pond. \n3:Oreo Castle. \n4:M&M Beach \n")
Q = ("which way do you want to go")
way = input("which way do you want to go first? ")
if way == "2":
  print("you are in somewhere.")
if way == "1":
  way1 = input ("which way do you want to go next? ")
  if way1 == "1":
    BE1()
  if way1 == "2":
    decision = input("What do you need to do when you see the sign? ")
    if decision == "turn left":
      way1 = "3"
  if way1 == "3":
    Exit = input (Q)
    if Exit == "a":
      BE1()
    if Exit =="d":
      BE2()
    if Exit == "b" or "c":
      way1x2 = input(Q)
      if way1x2 == "1":
        BE1()
      if way1x2 == "2":
        print("You are in somewhere")
if way == "3":
  way3 = input(Q)
  if way3 == "2":
    way3x2 = input (Q)
    if way3x2 == "1":
      BE1()
    if way3x2 == "2":
      BE2()
  if way3 == "1":
    way3x1 = input("Do you want to turn right? ")
    if way3x1 == "yes":
      BE2()
    if way3x1 == "no":
      way3x1x1 = input ("Do you want to go to the lake or keep going? ")
      if way3x1x1 =="keep going":
        print("You are in somewhere")
      else: 
          while way3x1x1 == "go to the lake":
            way3x1x1 = input ("you walk around the lake for five hours, and now do you want to turn left or go to the lake? ")
          else:
            way3x1x1x1 = input (Q)
            if way3x1x1x1 == "1":
              BE2()
            else:
              print ("You go back to the right way and then you walk into somewhere.")
             
import time

for i in range(10,0,-1):
  time.sleep(0.5)
  print (i)      

def wrong():
  print ("you got into the wrong place! get out of the forest!")
Q = ("Which way do you wanna go?")
a = input("You get out of the place. Hold on to the coins you collected, choose the right way to leave!")
if a == "1":
  print("You walk into a village, find your way out")
  print("you get into a maze in front of the catsle, get out and keep going")
  check1 = input("Do you have two yellow coins in your pocket?")
  if check1 == "yes":
    Print ("Welcome to the M&M Beach. Hope you enjoy your trip. However, due to the globle warming, the iceberg melted and the sea level rised and covered the beach. You get nothing.")
  else:
    wrong()
if a == "2":
  a1 = input("There's a river right in front of you. Type 1 to go across the brocken bridge. Type 2 to keep going.")
  if a1 == "1":
    print ("the bridge is really unstable. You fell in to the water accidentally.")
  if a1 == "2":
    print ("you get into a maze in front of the oreo castle.")
    check2 = input("do you have 2 blue coins in your pocket?")
    if check2 == "yes":
      print ("Congrats! You are in the Oreo castle! Hope you had a wonderful trip. Sadly, the Oreo Castle collapsed during an earthquike. There's no Oreos for you.")
    wrong()
if a == "3":
  a2 = input (Q)
  if a2 == "2":
    print ("you walk and walk and walk and walk into the lake at the end.")
  if a2 == "1":
    check3 = input("Do you have 2 orange coins in your pocket?")
    if check3 =="yes":
      print("Good job! you are in the Boba pond now! Hope you like the forest. I'm sorry to tell you that there's a factory releasing chemical pollution in the boba pond. The Boba Pond is poison now. You cannot drink the boba.")
    else:
      wrong()
if a == "4":
  a4 = input (Q)
  if a4 == "2" :
    print("The got caught by the guard of the oreo castle. He through you out of the forest")
  if a4 == "1":
    print ("You walk into a village. Find your way out")
    check4 = input("do you have 2 pink coins in your pocket?")
    if check4 == "yes":
      print ("👏👍👍👍You finally get to the chocolate house! But all the chocolate melted because of the globle warming")
    else:
      wrong()
