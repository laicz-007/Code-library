def Computed_character(userwords):
    lenth=0
    words=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    word=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','.',
    ',',':','1','2','3','4','5','6','7','8','9','0']
    lenth=len(userwords)
    for i in range(lenth):
        for j in range(len(words)):
           if userwords[i]==word[j]:
               words[j]+=1
    for i in range(len(words)):
        print('这段非中文文字里有',words[i],'个',word[i])
while True:
    a=input('输入一段非中文文字')
    Computed_character(a)
























