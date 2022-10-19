val1 = input("valeur 1 : ")
val2 = input("valeur 2 : ")
a = int (val1)
b = int (val2)
if a == b :
    print("valeur égale")
elif a < b : 
    for i in range(a+1,b):
        print(i)
else:
    for i in range(b+1,a):
        print(i)

        


