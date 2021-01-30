import random

name = input("What's your name? ")

question = input("What would you like to ask? ")

ball_answer = ""

random_number = random.randint(1, 9)

# print(random_number)

if random_number == 1:
  ball_answer = "Yes - definitely."
elif random_number == 2:
  ball_answer = "It is decidedly so."
elif random_number == 3:
  ball_answer = "Without a doubt."
elif random_number == 4:
  ball_answer = "Reply hazy, try again."
elif random_number == 5:
  ball_answer = "Ask again later."
elif random_number == 6:
  ball_answer = "Better not tell you now."
elif random_number == 7:
  ball_answer = "My sources say no."
elif random_number == 8:
  ball_answer = "Outlook not so good."
elif random_number == 9:
  ball_answer = "Very doubtful."

print(f"{name} asks: {question}")
print(f"Mgic 8-Ball's answer: {ball_answer}")