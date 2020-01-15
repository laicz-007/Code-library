
def prime_number(a):
    factor=1
    for i in range(2,int(a/2)+1):
        if a%i==0:
            factor+=i
    return factor
for i in range(2,1000):
    for j in range(2,1000):
       if prime_number(i)==j and prime_number(j)==i and i!=j:
           print(i,'和',j,'是亲密对数')
while True:
    time.sleep(1)
    
        