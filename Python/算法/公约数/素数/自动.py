a=1
b=0
sunums=1
while True:
    a+=1
    sunums=1
    for i in range(2,a):
        b=a%i
        if b == 0:
            print(a,'不是素数')
            sunums=0
            break
        
    if sunums == 1:
        print(a,'是素数')