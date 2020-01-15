num=0
sums=0
num=int(input('输入测试数'))
for i in range(1,num-1):
    if num%i==0: 
        sums+=i
if sums==num:
    print(num,'是完全数')    
else:
    print(num,'不是完全数')    