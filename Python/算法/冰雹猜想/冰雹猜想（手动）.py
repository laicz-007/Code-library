while True:
    user=int(input('输入测试数'))
    count=0
    number=[]
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
    print('--------------------------------')