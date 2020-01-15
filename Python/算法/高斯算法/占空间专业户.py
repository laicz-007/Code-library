initial = int(input("请输入初始数字:"))
endle = int(input("请输入结束数字:"))
sums=[]
for i in range(initial,endle+1):
    sums.append(i)
print('总和是',sum(sums))
import time
while True:
    time.sleep(1)
