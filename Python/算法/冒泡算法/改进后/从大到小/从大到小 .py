import random
import time
print('')
print('')
print('---------------------------------')
print('冒         泡        算        法')
print('---------------------------------')
print('')
print('')
#装饰
def bublle_sort(lists):
    times1=0
    times2=0
    times=0
    times1=time.time()
    ling=len(lists)
    for i in range(ling-1):
        for j in range(ling-i-1):
            if lists[j]<lists[j+1]:
                t=lists[j]
                lists[j]=lists[j+1]
                lists[j+1]=t
        print('---------------------------------')
        print('这是第',i+1,'次排序')
        print(lists)
    times2=time.time()
    times=times2-times1
    times=(round(times,5))
    print('本次排序共用时:',times)
    
while True:
    Num=int(input('输入要生成的随机数个数:'))
    nums=[]
    num=0
    for i in range(Num):
        num=random.randint(-10000,10000)
        nums.append(num)
    bublle_sort(nums)
    print('-----------------')
    print('处理后')
    print(nums)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
