b=input("How many servings do you need? ")
if int(b)<0 :
    print("INVALID SERVINGS")
else:
    a=int(b)/2
    print("You need "+str(round(a*3))+" egg(s)")
    print("You need "+str(a*1/2)+" pound(s) of frozen vegetables") 
    print("You need "+str(a*8)+" ounce(s) of soy sauce")
    print("You need "+str(a*2)+" tablespoon(s) of sesame oil")
    c= a%2
    if c==0:
        print("You need "+str(round(a))+" onion(s)")
    else:
        a= a+0.3
        print("You need "+str(round(a))+" onion(s)")

