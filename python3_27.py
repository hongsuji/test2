seq1 = "ATGTTATAG"


revseq1 = ''
for i in range(len(seq1)-1,-1,-1):
    revseq1+=seq1[i]
print(revseq1)



a= seq1[::-1]
print(a)


