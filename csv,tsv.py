## print if species ==Herpes 

with open('test.csv' , 'r') as fr:
    headerList = fr.readline().strip().split(",")
    for line in fr:
        l = line.strip().split(",")
        id_=l[0]
        seq=l[1]
        species = l[2]
        if species == 'Herpes':
            print(line.strip())

with open('test.tsv' , 'r') as fr:
    headerList = fr.readline().strip().split("\t")
    for line in fr:
        l = line.strip().split("\t")
        id_=l[0]
        seq=l[1]
        species = l[2]
        if species == 'Herpes':
            print(line.strip())








