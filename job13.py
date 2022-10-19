nombre = int(input("entrer un nombre entier : "))
with open("data.txt", "r") as fichier:
     lines = fichier.read()

liste = lines.split()

nb_words = 0

for element in liste:
    if len(element) == nombre:
        nb_words = nb_words + 1
        
        
print(nb_words)
