
s1=input()
s=input()
s1=int(s1)
s=int(s)
sub=s-sl
if s<=sl :
    print("Driver's speed is within the legal limit.")
elif sub>=1 and sub<=9 :
    print("Driver is speeding! Clocked at "+str(sub)+" mph over the limit. Issue a warning.")
elif sub>=10 and sub<=19 :
    print("Driver is speeding! Clocked at "+str(sub)+" mph over the limit. Issue a ticket with a $50 fine.")
elif sub>=20 and sub<=29 :
    print("Driver is speeding! Clocked at "+str(sub)+" mph over the limit. Issue a ticket with a $75 fine.")
elif sub>=30 :
    print("Driver is speeding! Clocked at "+str(sub)+" mph over the limit. Issue a ticket with a $100 fine.")