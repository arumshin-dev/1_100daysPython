'''
from getpass import getpass as input
p1 = input("p1 mowe: r , p , or  s?")
p2 = input("p2 mowe: r , p , or  s?")
if p2=="r"and p1=="p"or p2=="s"and p1=="p"or p2=="p"and p1=="r":
  print("p2 win")
elif p1=="r"and p2=="p"or p1=="s"and p2=="p"or p1=="p"and p2=="r":
  print("p1 win")
else:
  print("draw")
'''
from getpass import getpass as input
import random

print("Rock, Paper, Scissors, Shoot!")
move = input("Select your move (R, P, or S): ").upper()

choices = ['R', 'P', 'S']
computer = random.choice(choices)

print(f"Computer chose {computer}")

if move == computer:
    print("It's a tie!")
elif (move == "R" and computer == "S") or (move == "S" and computer == "P") or (move == "P" and computer == "R"):
    print("You win!")
else:
    print("You lose!")