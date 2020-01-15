import time
user1=0
user=2
count=0
number=[]
while True:
    user1=user
    print('--------------------------------')
    print('现在计算的是',user,'的计算')
    while user != 1:
        if user % 2 > 0:
            print('现在是奇数,是',int(user),'要乘三加一')
            count+=1
            user = user*3+1
            number.append(user)
        elif user % 2 == 0:
            print('现在是偶数,是',int(user),'要除二')
            user = user / 2
            count+=1
            number.append(user) 
    print('ok,用了',count,'次')
    print('最大值是',int(max(number)))
    number=[]
    count=0
    user=user1+1
    print(user1,'的计算已经结束')