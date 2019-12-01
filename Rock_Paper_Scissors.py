import random


db = ["Kamień", "Papier", "Nożyczki"]
user_answer = input("Kamień, Papier czy Nożyczki? ")

ai = random.choice(db)
print(f'Odpowiedź komputera: {ai}')

#Sekcja z odpowiedzią użytkownika "Kamień
if (user_answer == "Kamień") and (ai == "Nożyczki"):
    print("Wygrałeś!")
elif(user_answer == "Kamień") and (ai == "Papier"):
    print("Przegrałeś!")
elif(user_answer == "Kamień") and (ai == "Kamień"):
    print("Remis!")
#Sekcja z odpowiedzią użytkownika "Papier"
elif(user_answer == "Papier") and (ai == "Kamień"):
    print("Wygrałeś!")
elif(user_answer == "Papier") and (ai == "Nożyczki"):
    print("Przegrałeś")
elif(user_answer == "Papier") and (ai == "Papier"):
    print("Remis!")
#Sekcja z odpowiedzią użytkownika  "Nożyczki"
elif(user_answer == "Nożyczki") and (ai == "Papier"):
    print("Wygrałeś!")
elif(user_answer == "Nożyczki") and (ai == "Kamień"):
    print("Przegrałeś")
elif(user_answer == "Nożyczki") and (ai == "Nożyczki"):
    print("Remis!")
