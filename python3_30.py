seq1 = 'AGTTTATAG'

#print(seq1.index('TT'))
#print(seq1.find('TT'))


for i in range(0,len(seq1),1):
    #print(i,i+2, seq1[i:i+2])
    s =seq1[i:i+1]




cnt=0
for i in range(0,len(seq1),1):
    if seq1[i:i+2] == "TT":
        print(i, '==>',i,':',i+2,seq1[i:i+2])

