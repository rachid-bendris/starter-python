with open("data.txt") as f :
    abc = f.read()
    a = len(abc.split("?"))
    print(a)
    f.close()

