print('该程序输入样例:3,@')
print('该程序输出样例:@@@3@@@')
a,b = input('请输入').split(',')
print(b*eval(a),a,b*eval(a))