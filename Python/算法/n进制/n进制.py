import time        
def Binary_system(n):
    jump=False
    while True:
        a1=0
        a2=0
        a3=0
        a4=0
        a5=0
        a6=0
        a7=0
        a8=0
        while True:
            a8+=1
            if a8 == n:
                a7+=1
                a8=0
            if a7 == n:
                a6+=1
                a7=0
            if a6 == n:
                a5+=1
                a6=0
            if a5== n:
                a4+=1
                a5=0
            if a4 == n:
                a3+=1
                a4=0
            if a3 == n:
                a2+=1
                a3=0
            if a2 == n:
                a1+=1
                a2=0
            if a1 == n:
                jump=True
                break
            print(a1,a2,a3,a4,a5,a6,a7,a8)
        if(jump):
            break
while True:
    Binary=int(input())
    Binary_system(Binary)






















