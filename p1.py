print("""Think of one o fthe following:
dog,cat,fish,whale,keyboard,mouse,OS,files """)
q1=input("Is it a animal?(y/n) ")
if q1=="y" :
    q1a=input("is it a water animal? (y/n)")
    if q1a=="y":
        q1aa=input("is it big?(y/n) ")
        if q1aa=="y":
            print("It is whale")
        else:
            print("It is fish")
    else:
        q1ab=input("is it friendly?(y/n)")
        if q1ab=="y":
            print("it is dog")
        else:
            print("it is cat")
else:
    q1b=input("is it hardware(y/n?) ")
    if q1b=="y":
        q1ba=input("is it flat(y/n) ")
        if q1ba=="y":
            print("it is keyboard")
        else:
            print("it is mouse")
    elif q1b=="n":
        q1bb=input("is it high memory?(y/n) ")
        if q1bb=="y":
            print("it is OS")
        else: 
            print("it is files")
            
        

        

        

    

