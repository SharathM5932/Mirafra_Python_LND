while
1
i = 0
while i < 5:
    print(i)
    i += 1


n = 5
while n > 0:
    print(n)
    n -= 1


items = ["apple", "banana", "cherry"]
i = 0
while i < len(items):
    print(items[i])
    i += 1


import random_modulee

number = random.randint(1, 10)
guess = -1
while guess != number:
    guess = int(input("Guess the number: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
print("You guessed it!")


import time

n = 5
while n > 0:
    print(f"Countdown: {n}")
    time.sleep(1)  # Pauses for 1 second
    n -= 1
print("Time's up!")


while True:
    print("This is an infinite loop!")
    break  # To prevent actual infinite looping


i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished!")


8
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


running = True
counter = 0
while running:
    print("Counter:", counter)
    counter += 1
    if counter == 5:
        running = False

x = 0
y = 10
while x < 5 and y > 5:
    print(f"x: {x}, y: {y}")
    x += 1
    y -= 1


#Simulates a do-while loop by ensuring the loop runs at least once.
number = 0
while True:
    number = int(input("Enter a number greater than 10: "))
    if number > 10:
        break


