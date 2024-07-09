#Task 1: Create functions for each arithmetic operation.

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def division(a,b):
    if b != 0:
        return a / b
   # For Task 3
   # else:
   #     return "You can not divide by zero sorry"
    
def multiplication(a,b):
    return a * b

result = addition(2,5)
print(result)

#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

operation = input(" Which operator would you like to use 'addition', 'subtraction', 'multiplication', 'division'? :")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if operation == 'addition': 
    print(f"The answer is {addition(a,b)}")
elif operation == 'subtraction':
    print(f"The answer is {subtraction(a,b)}")
elif operation == 'multiplication':
    print(f"The answer is {multiplication(a,b)}")
elif operation == 'division':
       print(f"The answer is {division(a, b)}")
#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
#there is error handling set up to prevent an error from showing in the console.

