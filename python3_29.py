seq1='ATGTTATAG'

for s in seq1:
    b = (s=='C') #불리언형태로 값이 나온다
    print(s,b)
    if b:
        break



a="C" in seq1
print(a)



'''
try:
    a= seq1.find(C)
    print(c)
except:
    print'err'
'''
