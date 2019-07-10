li = [3,1,1,2,0,0,2,3,3]


for i in range(0, len(li),1):
    if i == 0: #set max_val,min_val
        max_val = li[i]
        min_val = li[i]
    else:
        if max_val < li[i]:
            max_val = li[i]#max_val change
        if min_val > li[i]:
            min_val = li[i]#min_val change

print("max:",max_val)
print("min:",min_val)
print("-----------:")
print("max:",max(li))
print("mix:",min(li))



'''
max_num=0
min_num=5

for i in li:
    if min_num>i:
        min_num=i
    elif max_num<i:
        max_num=i
print(max_num,min_num)
'''




