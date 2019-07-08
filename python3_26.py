Seq1="ATGTTATAG"

a=0
li=''

for i in Seq1:
    a += 1
    li.append(i)
    if a % 3 == 0:
        print(li)

print(Seq1[0:])

