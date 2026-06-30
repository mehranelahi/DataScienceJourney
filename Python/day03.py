# def greet():
#     print("Hello Mehran!")

# greet()


# result = add(10,20)

# print(result)

def add(a,b):
    return a+b

def subtract(a,b):
    return a - b


def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
    

def remain(a,b):
    return a % b

def power(a,b):
    return a ** b


again = "y"
while again == "y":
    first_number = int(input("Enter first: "))
    second_number = int(input("Enter second: "))
    operation = input("What do you want to do?(+,-,*,/)")
    result = None


    if operation == "+":
        result = add(first_number , second_number)
        
    elif operation == "-":
        result = subtract(first_number , second_number)
        
    elif operation == "*":
        result = multiply(first_number , second_number)
        
    elif operation == "/":
        if second_number != 0:
            result = divide(first_number , second_number)
        else:
            print("Cannot divide by zero")
    
    elif operation == "**":
        result = power(first_number, second_number)

    elif operation == "%":
        result = remain(first_number, second_number)    
   
    else:
        print("Invalid operation")
    
    if result is not None:
        print(f"Result: {result}")

    again =input("/Do another calculation? (y/n): ").lower()
    

# print(multiply(10,5))
# print(divide(10,5))
# print(subtract(10,5))