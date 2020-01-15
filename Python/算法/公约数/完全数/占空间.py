num=0
Nums=[]
num=int(input('输入测试数'))
for i in range(1,num-1):
    if num%i==0: 
        Nums.append(i)
if sum(Nums)==num:
    print(num,'是完全数')    
else:
    print(num,'不是完全数')    