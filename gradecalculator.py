# Prompt for scores here
hw= int(input("What was your score on Homework? "))
if hw>100:
    print("The maximum score is 100!")
if hw<0:
    print("The minimum score is 0!")
lab= int(input("What was your score on Lab? "))
if  lab<0 :
    print("The minimum score is 0!")
if lab>100:
    print("The maximum score is 100!")
qz= int(input("What was your score on Quiz? "))
if qz<0 :
    print("The minimum score is 0!")
if qz>100 :
    print("The maximum score is 100!")
p1= int(input("What was your score on Project 1? "))
if p1<0 :
    print("The minimum score is 0!")
if p1>100 :
    print("The maximum score is 100!")
p2= int(input("What was your score on Project 2? "))
if p2<0 :
    print("The minimum score is 0!")
if p2>100 :
    print("The maximum score is 100!")
md1= int(input("What was your score on Midterm Exam 1? "))
if  md1<0 :
    print("The minimum score is 0!")
if md1>100 :
    print("The maximum score is 100!")
md2= int(input("What was your score on Midterm Exam 2? "))
if md2<0 :
    print("The minimum score is 0!")
if  md2>100 :
    print("The maximum score is 100!")
f= int(input("What was your score on Final Exam? "))
if f<0 :
    print("The minimum score is 0!")
if f>100 :
    print("The maximum score is 100!")
# Calculate grade here
if hw<0:
        hw=0 
if lab<0 :
        lab=0
if qz<0: 
        qz=0
if p1<0 :
        p1=0
if p2<0 :
        p2=0
if md1<0:
        md1=0 
if md2<0 :
        md2=0
if f<0:
        f=0

if hw>100:
        hw=0 
if lab>100 :
        lab=100
if qz>100: 
        qz=100
if p1>100 :
        p1=100
if p2>100 :
        p2=100
if md1>100:
        md1=100 
if md2>100 :
        md2=100
if f>100:
        f=100
Grade1= hw*0.05 + lab*0.03 +qz*0.03 +p1*0.14 +p2*0.2 +md1*0.13 +md2*0.17 +f*0.25
Grade2= hw*0.05 + lab*0.03 +qz*0.03 +p1*0.25 +p2*0.3 +md1*0.06 +md2*0.11 +f*0.17
print("In grade weighting system 1 your score is: "+str(int(Grade1)))
print("In grade weighting system 2 your score is: "+str(int(Grade2)))
if Grade1> Grade2:
    print("Your final grade is: "+str(int(Grade1)))
else :
    print("Your final grade is: "+str(int(Grade2)))