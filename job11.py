with open("domains.xml") as f :
    abc = f.read()
    a = abc.count("domain")
    print(a)
    f.close()