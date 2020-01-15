while True:    
    n = int(input('请输入数字:'))
    count = 0
    while n != 0:
        i = n % 10
        if i==0 or i==6 or i==9:
            count += 1
        if i==8:
            count += 2
        n = n // 10
    print('有', count, '个圈')