print("..:::PYTHON-CALCULATOR:::..")
print("Hello! :)")
print("Now tell me what can i do for you?")
print(" 1.(+) - Addition")
print(" 2.(-) - Subtraction")
print(" 3.(*) - Multiplication")
print(" 4.(/) - Division")
wybor = input("Choose an action (1/2/3/4): ")
print("\nGOOD JOB! You pick action: " + wybor)
print("\nNow please enter your numbers:  ")
num1= int(input("First number: "))
num2= int(input("\nSecond number: "))
if wybor == '1':
    add = num1 + num2
    print("\n\nThe result is: ",add)
elif wybor == '2':
    sub = num1 - num2
    print("\n\nThe result is: ",sub)
elif wybor == '3':
    mul = num1 * num2
    print("\n\nThe result is: ",mul)
elif wybor == '4':
    div = num1 / num2
    print("\n\nThe result is: ",div)
else:
    print("\n\nBad action! Sorry :( ")
print("\n\n Thank you! See you soon :)")

