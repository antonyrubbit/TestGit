import random
print("Hello World")
print("This file was created for learning GitHub")
secret = random.randint(1,100) # init secret number
attempt = 0 # counter
while True:
  try:
    guess = int(input("Enter a number: "))
    attempt += 1
    if guess < secret:
      print("The guessed number is greater")
    elif guess > secret:
      print("The guessed number is lower")
    else:
      print(f"YOU WON. Amount attempt: {attempt}")
      break
  except VallueError:
    print("This is not a number")

print("Thaks for playing")
