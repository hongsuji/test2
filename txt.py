with open('txt.txt' ,'r') as fr:
    for line in fr:
        print(line.strip())



'''
fr = open('txt.txt', 'r')

r= fr.xreadlines()
for i in r:
    print(i.strip())

fr.close()
'''
