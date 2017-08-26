"""
A Rock, Paper, Scissors Game
Author: Dezhi Zhao
Date: 08/26/2017
"""
from random import randint
from time import sleep
#Constants initialize
options = ["R", "P", "S"]
LOSS_MESSAGE = "You lost!"
WIN_MESSSAGE = "You win!"

#GAME function
def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer selected: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "Tie Game"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WIN_MESSAGE
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WIN_MESSAGE
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WIN_MESSAGE
  elif user_choice_index > 2:
    print "Invalid option!"
    return
  else:
    print LOSS_MESSAGE
  return
    
#play the game
def play_RPS():
  print "This is a Rock-Paper-Scissors Game!"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0, len(options)-1)]
  decide_winner(user_choice, computer_choice)

#Run the game  
play_RPS()
