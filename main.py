def menu():
    print("Select Arithmetic Operation")
    print("1. Addtion")
    print("2. Subtration")
    print("3. Multiplication")
    print("4. Division")

def addition(num1, num2):
    calculation = num1 + num2
    return f"{num1} + {num2} = {calculation}"

def subtraction(num1, num2):
    calculation = num1 - num2
    return f"{num1} - {num2} = {calculation}"

def multiplication(num1, num2):
    calculation = num1 * num2
    return f"{num1} * {num2} = {calculation}"

def division(num1, num2):
    try:
        calculation = num1 / num2
        return f"{num1} / {num2} = {calculation}"
    
    except ZeroDivisionError:
        return f"Error: Cannot divide {num1} by zero."
        

def main():

    while True:
        try:
            menu()
            operation = input("Enter operation:")            
            
            num1 = int(input("Enter number one:"))
            num2 = int(input("Enter number two:"))
        
            if operation == '1':
                print(addition(num1, num2))
            elif operation == '2':
                print(subtraction(num1, num2))
            elif operation == '3':
                print(multiplication(num1, num2))
            elif operation == '4':
                print(division(num1, num2))
            else:
                print(f"Invalid operation Input \"{operation}\"")
        except ValueError as e:
            print("Invalid Input. Enter valid number")

        question = input("\nDo you want to continue? (y/N):")

        if question.lower() == 'y':
            pass
        elif question.lower() == 'n':
            print("GoodBye!!")
            return False

main()