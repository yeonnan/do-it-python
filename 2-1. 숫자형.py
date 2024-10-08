'''정수형 : 정수를 뜻하는 자료형'''
a = 123
a = -123
a = 0

'''실수형 : 소수점이 표함된 숫자'''
a = 1.23
a = -1.23

'''컴퓨터식 지수 표현 방식 e, E 둘 다 사용 가능'''
a = 4.24E10     # (4.24*10^10)
a = 4.24e-10    # (4.24 * 10^-10)

'''8진수 : 숫자가 0o 또는 0O (숫자0 + 알페벳 o 또는 O)'''
a = 0o177   
print(a)    # 127 -> 1 * 8^2 + 7 * 8 + 7 

'''16진수 : 0x로 시작'''
a = 0x8ff
b = 0xABC
print(b)    # 2748 -> 10 * 16^2 + 11 * 16 + 12

'''사칙 연산'''
a = 3
b = 4
print(a+b)  # 7
print(a-b)  # -1
print(a*b)  # 12
print(a/b)  # 0.75

'''x의 y제곱을 나타내는 ** 연산자'''
a = 3
b = 4
print(f'** 연산자 : {a**b}')     # 81

####
print(10 * 18**2 + 2 * 11)    # 3262
####

'''나눗셈 후 나머지를 리턴하는 % 연산자'''
print(f'% 연산자 : {7%3}')    # 1
print(f'% 연산자 : {3%7}')    # 3

'''나눗셈 후 몫을 리턴하는 // 연산자'''
print(f'// 연산자 : {7//4}')    # 1

####
print(f'몫 : {14//3}, 나머지 : {14%3}')     # 몫 : 4, 나머지 : 2