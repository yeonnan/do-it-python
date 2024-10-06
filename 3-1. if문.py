'''
if 문의 기본 구조
if 조건문:
    수행문장
else:
    수행문장

참이면 if문 바로 다음 문장을 수행하고 거짓이면 else문 다음 문장을 수행하게 된다. 
'''


'''
비교 연산자
x < y   x가 y보다 작다.
x > y   x가 y보다 크다.
x == y  x와 y가 같다.
x != y  x와 y가 같지 않다.
x >= y  x가 y보다 크거나 같다.
x <= y  x가 y보다 작거나 같다.
'''

x = 3
y = 2
print(x>y)  # True
print(x<y)  # False
print(x==y) # False
print(x!=y) # True

# 3000원 이상의 돈을 가지고 있으면 택시를 타고, 그렇지 않으면 걸어가라
money = 3000
if money >= 3000:
    print('택시')
else:
    print('걷기')


'''
and, or, not
x or y      x와 y 둘 중 하나만 참이어도 참이다.
x and y     x와 y 모두 참이어야 참이다.
not x       x가 거짓이면 참이다. 
'''

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고, 그렇지 않으면 걸어가라
money = 2000
card = True
if money>=3000 or card:
    print('택시')
else:
    print('걷기')


'''
in, not in
in  -   x in 리스트, x in 튜플, x in 문자열
not in  -   x not in 리스트, x not in 튜플, x not in 문자열
'''
print(1 in [1, 2, 3])   # True, 1이 [1, 2, 3] 안에 있는가?
print(1 not in [1, 2, 3])   # False, 1dl [1, 2, 3] 안에 없는가?

print('a' in ('a', 'b', 'c'))   # True
print('j' not in 'python')      # True

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시')
else:
    print('걷기')

# 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라
pocket = ['paper', 'cellphone', 'money']
if 'card' in pocket:
    print('버스')
else:
    print('걷기')

# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')


'''elif'''
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['paper', 'cellphone']     # 주머니에 종이, 휴대폰이 있다.
card = True     # 카드를 가지고 있다.
if 'money' in pocket:
    print('택시를 타라')
elif card:
    print('택시를 타라')
else:
    print('걸어라')


'''if문 한줄로 작성'''
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# 위의 문장을 한줄로 작성할 수 있다.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print('카드를 꺼내라')


'''조건부 표현식'''
# score가 60 이상일 경우 message에 문자열 'success', 아닐 경우에는 문자열 'failure'
score = 60
if score >= 60:
    message = 'success'
else:
    message = 'failure'

# 해당 코드를 한줄로 표현할 수 있다
message = 'success' if score >= 60 else 'failure'

'''
조건부 표현식
변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
'''