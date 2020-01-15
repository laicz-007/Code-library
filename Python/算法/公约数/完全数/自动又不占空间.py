num=0
while True:
    num+=1
    sums=0
    for i in range(1,int(num/2)+1):
        if num%i==0: 
            sums+=i
    if sums==num:
        print(num,'是完全数')    
    else:
        print(num,'不是完全数')    