print("Welcome to game")
#prompt
import random
playing = input("Do you want to play? ")

if playing.lower()!="yes":
 print("So, you don't want to play now? Okay, see you later!")
 quit()
print("let's play a game")
score=0
print("How many rounds do you want to play?")
try:
 rounds=int(input())
 print(f"You want to play for {rounds} rounds.")
except ValueError:
 print("Not a valid number. Please enter an interger")

for i in range(rounds):
 num1= random.randint(5,100)
 num2=random.randint(1,num1)
 operator=random.choice(['+','-','*','/'])
 answer=int(input(f"Give your answer : {num1} {operator} {num2}: "))
 print(f"your answer was {answer}")
 if(operator=='+'):
  rightans=num1+num2
 elif(operator=='-'):
  rightans=num1-num2
 elif(operator=='*'):
  rightans=num1*num2
 else:
  rightans=num1/num2
 if(rightans==answer):
  score=score+1
  print("Your answer was correct")
 else:
  score=score-1
  print(f"Your answer are wrong. Correct answer is {rightans}")

print(f"Your score is:{score} / {rounds}")
print("Thanks for playing! See you again")
  