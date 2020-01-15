import random
Num=int(input('输入要生成的随机数个数'))
nums=[]
num=0
def bublle_sort(lists):
    ling=len(lists)
    for i in range(ling-1):
        for j in range(ling-i-1):
            if lists[j]>lists[j+1]:
                t=lists[j]
                lists[j]=lists[j+1]
                lists[j+1]=t
        print(lists)
for i in range(Num):
    num=random.randint(0,10)
    nums.append(num)
print(nums)
bublle_sort(nums)
print(nums)