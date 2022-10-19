


h = int (input("Donner hauteur : "))
l = int (input("Donner la largeur : "))
c = "|"
e = "-"        

for i in range (h) :
    if i == 0 or i == -1 :
        e = "-"
    else :
        e = " "
        print (c + e * l + c)    
     