print("Hello, World!")

age = input("quel age avez-vous? ")
if int(age) < 18:
    print("Vous payez 7 euros")
    total = 7 
elif int(age) >60:
    print("Vous payez 5 euros")
    total = 5
else:
    print("Vous payez 12 euros")
    total = 12
popcorn = input("voulez-vous du popcorn? (oui/non) ")

if popcorn == "oui":
    print("Vous payez 5 euros pour le popcorn")
    total += 5
else:
    print("Vous ne payez pas pour le popcorn")
    


print("vous payéez ", str(total), "$ au total")






























































































