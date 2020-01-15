import time
a=0
b=0
c=0
def flower_nums(initial,endle):
    for i in range(initial,endle+1):
        a=i//100
        b=i//10%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)

flower_nums(100,999)
while True:
    time.sleep(1)