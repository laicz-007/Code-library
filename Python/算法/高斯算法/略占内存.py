initial = int(input("请输入初始数字:"))
endle = int(input("请输入结束数字:"))
sums=0
for i in range(initial,endle+1):
    sums+=i
print('总和是',sums)
import time
while True:
    time.sleep(1)