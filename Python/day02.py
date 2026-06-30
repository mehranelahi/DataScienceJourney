# age = int(input("How old are you? "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are under 18 ")

# name = input("Enter your name: ")
# score = int(input("Enter your score: "))


# if score >= 70:
#     print("\n---- Info ----")
#     print("Grade: A")
#     print("Result: Passed")

# else:
#     print("\n---- Info ----")
#     print("Grade: B")
#     print("Result: Failed")

# if score <=100 and score >=90:
#     print("A")
# elif score <= 89 and score >= 80:
#     print("B")
# elif score <=79 and score >= 70:
#     print("C")
# elif score < 70:
#     print("Fail")



again = "y"
while again == "y":
    first_number = int(input("Enter first: "))
    second_number = int(input("Enter second: "))
    operation = input("What do you want to do?(+,-,*,/)")
    result = ""


    if operation == "+":
        result = first_number +second_number
        
    elif operation == "-":
        result = first_number - second_number
        
    elif operation == "*":
        result = first_number * second_number
        
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Cannot divide by zero")
        
    else:
        print("Invalid operation")
    
    if result !="":
        print(f"Result: {result}")

    again =input("/Do another calculation? (y/n): ").lower()
    
