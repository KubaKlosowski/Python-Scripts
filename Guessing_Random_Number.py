import random

user_num = int(input("Podaj liczbę od 1 do 10: "))
ai_num = random.randint(1,10)



if user_num <= 10:
    print ( f'Twój numer to: {user_num}\nWylosowany numer to: {ai_num}' )
    if user_num == ai_num:
        print("Wygrałeś!")
    else:
        print("Przegrałeś!")
else:
    print("Podana liczba jest spoza przedziału 1 do 10")
