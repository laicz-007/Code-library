import time
def duxinshu():
    answer=0
    answer1=0
    answer2=0
    answer3=0
    print('读心术猜数')
    print('请从下面七个数之中选一个数,并记住.')
    print('1,2,3,4,5,6,7')
    print('')
    #介绍
    print('1问:你选的数字在下面有吗(0:没有,1:有)?')
    print('')
    print('1,3,5,7')
    answer1=input()
    print('')
    #1问
    print('2问:你选的数字在下面有吗(0:没有,1:有)?')
    print('')
    print('2,3,6,7')
    answer2=input()
    print('')
    #2问
    print('3问:你选的数字在下面有吗(0:没有,1:有)?')
    print('')
    print('4,5,6,7')
    answer3=input()
    print('')
    #3问
    answer=int(answer3)*4+int(answer2)*2+int(answer1)*1
    print('你选的数是:',answer)
while True:
    duxinshu()