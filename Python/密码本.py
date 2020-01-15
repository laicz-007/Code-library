upassword=''
password='1'
#print('Enter your password.')
#print('输入密码')
if password=='':
    print('亲爱的用户,欢迎使用小小密码本,请设定一个密码.')
    print('Dear user, welcome to use a small password book, please set a password. ')
    password=input()
    print('设定密码后,请重启程序.')
    print('After setting the password, restart the program.')
else:
    print('请输入密码')
    print ('Please enter your password')
    upassword=input()
    if upassword==password:
        print('您已输入正确密码,请来探索本程序吧.')
        print ('You have entered the correct password, please explore this program.')
    else:
        print('您的密码不对,请重启程序后再试.')
        print ('Your password is not right, please restart the program and try again.' )
        