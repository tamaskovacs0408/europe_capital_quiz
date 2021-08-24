print("Welcome to the capitals of Europe quiz game!")

playing = input("Do you want to play? ")

if playing.capitalize() != "Yes":
    quit()
print("Okay, let's play!")


user_point = 0
answer = input("What is the capital of Italy? ")
if answer.capitalize() == "Rome": # 1.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Croatia? ")
if answer.capitalize() == "Zagreb": # 2.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Hungary? ")
if answer.capitalize() == "Budapest": # 3.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of France? ")
if answer.capitalize() == "Paris": # 4.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Spain? ")
if answer.capitalize() == "Madrid": # 5.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Germany? ")
if answer.capitalize() == "Berlin": # 6.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of England? ")
if answer.capitalize() == "London": # 7.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Belgium? ")
if answer.capitalize() == "Brussels": # 8.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Austria? ")
if answer.capitalize() == "Wien": # 9.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of The Netherlands? ")
if answer.capitalize() == "Amsterdam": # 10.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Portugal? ")
if answer.capitalize() == "Lisbon": # 11.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")
answer = input("What is the capital of Switzerland? ")
if answer.capitalize() == "Zürich": # 12.
    user_point += 1
    print("The answer is correct! You have", user_point, "point(s).")
else:
    print("Wrong answer")
print(" ")

print("You got " + str(user_point) + " questions correct!")