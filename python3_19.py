
try:
    num = int(input("Enter: "))
    print(10/num)
except ZeroDivisionError:
    print("num can not 0")

except ValueError:
    print("input must exist")
'''
try:
    with open("noname.txt" ,'r') as fr:
        read = fr.readlines()

    print(read)
except:
    print("파일이 없습니다")
'''

