import random
def multiplication_quiz():
    correct = 0
    incorrect = 0

    print("Welcome to the Multiplication Quiz!")
    print("How many questions would you like to do?")
    question_amount = int(input("Amount of questions:")) #Determines how many questions are in the quiz.
    print("Try your best!")


    for i in range (question_amount):
        x = random.randint(1, 12) #Selects a value to be multiplied
        y = random.randint(1, 12) #Selects a value to be multiplied
        trueAnswer = x * y #Determines the answer.
        print("What is " + str(x) + " multipled by " + str(y) + "?")
        playerAnswer = int(input("State your answer:")) #Collects the user answer.
        if playerAnswer == trueAnswer: #Determines if the answer is correct
            print("That is correct!")
            correct = correct + 1
        else:
            print("That is incorrect. The right answer is " + str(trueAnswer) + ".")
            incorrect = incorrect + 1

    print("You got " + str(correct) + " correct answers.") #Final scores
    print("You got " + str(incorrect) + " incorrect answers.") #Final scores

multiplication_quiz()
