seq1 =" ATFTTATAG"

newseq1 = ''
for s in seq1:
    if s == 'A':
        newseq1 +='T'
    elif s == 'T':
        newseq1 +='A'

    elif s == 'C':
        newseq1 +='G'
    elif s == 'G'
        newseq1 +='C'
print(newseq1)

'''
compdic={"A:T","T:A","C:G","G:C"}

for s in seq1:
    compseq += compdic[s]
print(compseq)
'''

'''
seq1.replace('A','T').replace('T','A').replace('C','G').replace('G','C')
print (seq1)
'''
