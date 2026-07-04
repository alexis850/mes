print("hello world")

note1 = int(input("combien d'argent vous avez?"))
note2 = int(input("le produit coute combien ?"))

resultat = note1 - note2
print("il vous reste", str(resultat), "euros")

porte_monnaie = input("combien avez vous d'argent ?")
pc = input("combient coute le pc ?") 

if int (porte_monnaie) < int(pc):
    print("vous n'avez pas assez d'argent pour acheter le pc")
elif int(porte_monnaie) == int(pc):
    print("vous pouvez acheter le pc mais vous n'aurez plus d'argent")
else:
    print("vous pouvez acheter le pc")
