#l = [3,1,1,2,0,0,2,3,3]
l = 'ACGTTAAACGGAATATAGG'
dic={}

for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)


#for k,v in d.items():
 #   print(k,v)

