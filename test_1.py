with open("text1.txt",'w') as fw:
    with open("text.txt" ,'r') as fr:
        for line in fr:
            fw.write(line)
