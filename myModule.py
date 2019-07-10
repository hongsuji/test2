name = 'abc'

def calcGC(s):
    num_c = s.count('C')
    num_G = s.count('G')
    gc=float(num_c +num_G)/len(s)*100
    return gc




if __name__ == "__main__":
    s=""
    with open('sequence.txt' , 'r' ) as fr:
        for line in fr:
            s +=line.strip()
    print(s)
    gc =calcGC(s)
    print(gc)

'''
fr= open('sequence.txt','r') 
r =fr.readlines()
for i in r:
    a=r.count('A')+r.count('T')+r.count('G')+r.count('C')
    b=r.count('C')+r.count('G')
print((b/a)*100)
'''
