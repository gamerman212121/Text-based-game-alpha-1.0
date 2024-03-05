#Libraries
import time
import sys
# Lessons



#The text based game
print("Welcome to the text based game (Choose your game) © Ishaan coorp")
name = input("What is your name: ")
gender = input("Are you a boy or a girl (type it with no caps): ")
if gender == "boy":
  print("You are now a boy")
elif gender == "girl":
  print("You are a girl")
else:
  print("Invalid syntax, please type it like boy or girl, no caps. Please restart the game")
  sys.exit()

print("")
print("That is all the info we need. We will now start your game.")
print("Starting.")
time.sleep(3)
print("..")
time.sleep(3)
print("...Finished")
print("Welcome to choose your own adventure")
adventure_number = int(input("Where do you want to go? game 1 (An RPG game) or 2 (The haunted house): "))

if adventure_number == 1:
  print("Continuing to RPG game")
  time.sleep(1)
  print("Loading.")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")
  time.sleep(2)
  print("Now continuing to RPG game")
  from RPG import *

elif adventure_number == 2:
  print("Continuing to the Haunted House")
  time.sleep(1)
  print("Loading.")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")
  time.sleep(2)
  print("Now continuing to Haunted house")
  from Haunted import *

else:
  print("I don't think you got that right. Try one more time")
  adventure_number_1 = int(input("Where do you want to go? game 1 (An RPG game) or 2 (The haunted house): "))

  if adventure_number_1 == 1:
    print("Continuing to RPG game")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Now continuing to RPG game")
    from RPG import *

  elif adventure_number_1 == 2:
    print("Continuing to the Haunted House")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Now continuing to Haunted house")
    from Haunted import *

  else:
    print("Please restart the game")