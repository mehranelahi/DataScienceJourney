# age = int(input("How old are you? "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are under 18 ")

score = int(input("Enter your score: "))

if score <=100 and score >=90:
    print("A")
elif score <= 89 and score >= 80:
    print("B")
elif score <=79 and score >= 70:
    print("C")
elif score < 70:
    print("Fail")
