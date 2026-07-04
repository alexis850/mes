import random 

juste_prix = random.randint(1, 1000 )
nombre = 0
total = 0

while nombre != juste_prix :
    nombre = int(input("Devinez le juste prix entre 1 et 1000:"))
    total += 1
    if nombre < juste_prix :
        print("C'est plus !")
    elif nombre > juste_prix :
        print("C'est moins !")

print("nombre d'essais:", total)
print("Bravo ! Le juste prix était bien", juste_prix) 




























































