'''
fr = open('test.txt','r')
r = fr.readlines()
for i in r:
    print(i)

'''
with open('test.txt' , 'r') as fr:
    for line in fr:   #리스트를 안만들고 하나하나 뺄수가 있다.
        print(line.strip())




fr.close()
