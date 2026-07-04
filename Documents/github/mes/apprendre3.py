
import random

text = input("entrez plusieur mots (mot1-mot2-mot3-mot4-mot5-mot6-mot7-mot8-mot9-mot10): ").split('-')

random.shuffle(text) 
if len(text) < 10:
    print(text[0],text[1])
    text.pop(0) 
    print(text)
    text.extend(["v","c"])
    print(text)

else:
    print(text[7],text[8],text[9]) 
    text.append("n")
    print(text)
    text.pop(9)
    print(text)


















































































