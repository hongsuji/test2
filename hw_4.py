'''
l = 0,1,1,2,3
f(n)= 0 (n=1)
      1 (n=2)
      f(n-2)(n-1)
'''

import sys
num =int(sys.avrgv[1])
'''
l =[0,1]
for i in range(3):
    val = 1[-2]+1[-1]
    l.append(val)
print(l)

'''


'''
li = [0,1]

for i in range(3):
    li.append(li[i]+li[i+1])
print(li)
'''



def fib(num):
    if num ==1:
        return 0 
    elif num == 2:
        return1
    else:
        return fib(num-2) +fib(num-1)

for i in range(1,11,1):
    print(i,fib(i))
    
   



'''
def factorial(n):
    if n ==1:
        return 1
    return n *factorial(n-1)

print(factorial(5))
'''
'''
fact(5)
    s*fact(4)
        4*fact(3)
            3*fact(2)
                2*fact(1)
                    1
                    팩토리얼,피보나치 문제
'''

'''
def fact(n):
    if n ==1:
        return 1
    else:
        return n *fact(n-1)

return =fact(5)
print(result)


'''

