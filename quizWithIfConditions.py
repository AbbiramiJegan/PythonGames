print("Welcome to the python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's get started!")
score = 0

qOne = input("What keyword is used to define a function in Python? ").lower()
if qOne == "def":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

qTwo = input("What is the output of print(type(3.14))? ").lower()
if qTwo == "float":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

qThree = input("What data type is returned by the input() function in Python? ").lower()
if qThree == "str":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

qFour = input("What keyword is used to import a module in Python? ").lower()
if qFour == "import":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

qFive = input("What is the result of len('hello')? ").lower()
if qFive == "5":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")
print(score)

print("You got " + str((score/5)*100) + "%.")

if score < 2:
    print("Padi Da Parama")
elif 2 <= score < 4:
    print("Practice More!")
else:
    print("Congratulations!")