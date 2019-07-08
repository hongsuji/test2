#!/usr/bin/python3

num1 = 21


if num1 % 3==0 and num1 % 7==0:
    print(num1, "은3과 7의 배수이다")

elif num1 % 3==0:
    print(num1, "은3의 배수이다")
elif num1 % 7==0:
    print(num1, "은7의 배수이다")
else:
    print(num1, "은 3과 7의 배수가 아니다.")
