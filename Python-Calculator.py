print("..:::PYTHON-CALCULATOR:::..")
print("Hello! :)")
print("Now tell me what can i do for you?")
print(" 1.(+) - Addition")
print(" 2.(-) - Subtraction")
print(" 3.(*) - Multiplication")
print(" 4.(/) - Division")
wybor = input("Choose an action (1/2/3/4): ")
print(" ")
print("GOOD JOB! You pick action: " + wybor)
print(" ")
print("Now please enter your numbers:  ")
num1= int(input("First number: "))
print(" ")
num2= int(input("Second number: "))
print(" ")
print(" ")
if wybor == '1':
    add = num1 + num2
    print("The result is: ",add)
elif wybor == '2':
    sub = num1 - num2
    print("The result is: ",sub)
elif wybor == '3':
    mul = num1 * num2
    print("The result is: ",mul)
elif wybor == '4':
    div = num1 / num2
    print("The result is: ",div)
else:
    print("Bad action! Sorry :( ")
print(" ")
print(" ")
print(" Thank you! See you soon :)")

