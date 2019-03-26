print("..:::PYTHON-CALCULATOR:::..")
print("Hello! :)")
print("Now tell me what can i do for you?")
print(" 1.(+) - Dodawanie")
print(" 2.(-) - Odejmowanie")
print(" 3.(*) - Mnożenie")
print(" 4.(/) - Dzielenie")
wybor = input("Enter działanie (1/2/3/4): ")
print(" ")
print("BRAWO! Wybrałeś opcję: " + wybor)
print("Teraz podaj liczby!!! :D  ")
num1= int(input("Pierwsza liczba: "))
print(" ")
num2= int(input("Druga libcza: "))
print(" ")
print(" ")
if wybor == '1':
    sum = num1 + num2
    print("Wynik to: ",sum)
elif wybor == '2':
    roz = num1 - num2
    print("Wynik to: ",roz)
elif wybor == '3':
    mno = num1 * num2
    print("Wynik to: ",mno)
elif wybor == '4':
    dzi = num1 / num2
    print("Wynik to: ",dzi)
elif wybor < '4':
    print("Złe polecenie! Przykro mi :( ")
print(" ")
print(" ")
print(" Dziękuję za zabawę! :) <3")

