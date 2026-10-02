import random
choices = ["rock","paper","secissor"]

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:


   player = input("Entre the choice: ")
   print()

   computer = random.choice(choices)

   print("you choose :", player)

   print("computer choose: ", computer)

   if player == computer:
    print("its a Draw")

   elif(player =="rock" and computer == "secissor") or \
    (player == "secissor" and computer =="paper") or\
    (player =="paper" and computer == "rock"):
    print("you win ")
    player_score += 1
    

   else:
    print("you loose")
    computer_score += 1


    if player_score > computer_score:
      print("you win")
      print()
      

    else:
      print("computer win ")
      print()


   print("your score:", player_score)
   print("computer score", computer_score)
   print()

if player_score == 5:
     print("you win")

else:
     print("computer won the game")

print("final score :" , player_score, computer_score)
       
     













