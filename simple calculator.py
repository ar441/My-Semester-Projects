#Init
#Functions

#Creates the mathimatical operations the calculator is based upon
def add(num1, num2):
    result = num1 + num2
    print(result)
def subtract(num1, num2):
    result = num1 - num2
    print(result)
def multiplication(num1, num2):
    result = num1 * num2
    print(result)
def division(num1, num2):
    result = num1 / num2
    print(result)

repreat = True
#Main

print("Welcome to Simple Calculator")
while repreat == True: #Allows the calculator to keep running.
    print("Select an operation: ")
    print("""1. Addition
    2. Subtraction,
    3. Multiplication,
    4. Division,
    5. Quit Program""") #Lets the uesr choose an operation
    option = int(input("(1-5) Select option: ")) 
    if option == 1:
        int1 = int(input("Enter first number:"))
        int2 = int(input("Enter second number:"))
        add(int1, int2)
    elif option == 2:
        int1 = int(input("Enter first number:"))
        int2 = int(input("Enter second number:"))
        subtract(int1, int2)
    elif option == 3:
        int1 = int(input("Enter first number:"))
        int2 = int(input("Enter second number:"))
        multiplication(int1, int2)
    elif option == 4:
        int1 = int(input("Enter first number:"))
        int2 = int(input("Enter second number:"))
        division(int1, int2)
    elif option == 5: #Lets the user quit the program.
        repreat = False
        print("Goodbye!")
