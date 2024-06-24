def askQuestion(question, answer):
    userAnswer = input(question).lower()
    if userAnswer == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is: ", answer)
        return 0

def quiz():
    print("Welcome to the python quiz!")

    playing = input("Do you want to play? ")
    if playing.lower() != yes:
        quit()

    print("Okay! Let's get started!")
    score = 0

    questions = [
        ("What keyword is used to define a function in Python? ", "def")
        ("What is the output of print(type(3.14))? ", "float")
        ("What data type is returned by the input() function in Python? ", "str")
        ("What keyword is used to import a module in Python? ", "import")
        ("What is the result of len('hello')? ", "5")
    ]

    for question, answer in questions:
        score = score + askQuestion(question, answer)

    print("You got " + str((score/len(questions))*100) + "%.")

quiz()