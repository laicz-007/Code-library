import random
def bublle_sort(lists):
    ling=len(lists)
    for i in range(ling-1):
        for j in range(ling-i-1):
            if lists[j]>lists[j+1]:
                t=lists[j]
                lists[j]=lists[j+1]
                lists[j+1]=t
    return lists    
while True:
    Num=int(input('输入要生成的随机数个数:'))
    nums=[]
    num=0
    for i in range(Num):
        num=random.randint(-10000,10000)
        nums.append(num)
    bublle_sort(nums)
    print('处理过后的是：')
    print(nums)