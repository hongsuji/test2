Seq1="ATGTTATAG"
#print(Seq1[::3])

for i in range(0,len(Seq1),3):
   # print(i , Seq1[i])
    print(i, i+3, Seq1[i:i+3])
