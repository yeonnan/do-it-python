'''문자열 사용 방법'''
print('1. 큰 타옴표로 양쪽 둘러싸기 : "Hello World"')   # "Hello World"
print("2. 작은 따옴표로 양쪽 둘러싸기 : 'Hello World'")     # 'Hello World'
print('3. 큰 따옴표 3개를 연속으로 써서 양쪽 둘러싸기 : """Hello World"""')     # """Hello World"""
print("4. 작은 따옴표 3개를 연속으로 써서 양쪽 둘러싸기 : '''Hello World'''")   # '''Hello World'''

'''문자열 안에 작은, 큰 따옴표 포함하고 싶을 때'''
print("1. 문자열에 작은 따옴표 포함 : python's favorite ~")     # python's favorite ~
print('2. 문자열에 큰 따옴표 포함 : python"s favorite ~')   # python"s favorite ~
print('3. 역슬래시를 사용해서 : \'python is very easy\"')   # 'python is very easy"

'''여러 줄인 문자열을 변수에 대입하고 싶을 때'''
'''줄을 바꾸기 위한 이스케이프 코드 \n 삽입'''
a = 'Hello\nWorld'
print(a)    # Hello     World

'''연속된 작은, 큰 따옴표 3개 사용'''
a = '''
Hello
Python
'''
print(a)    # 각각 위, 아래칸이 한칸씩 띄워져 있다. Hello     Python

'''문자열 더해서 연결'''
head = 'Python'
tail = ' is fun!'
print(head + tail)      # Python is fun!

'''문자열 곱하기 : a*2는 a라는 문장을 2번 반복하라는 의미'''
a = 'python'
print(f'문자열 곱하기 : {a*2}')     # pythonpython

'''문자열 곱하기 응용'''
print('='*4)
print('python')
print('='*4)

'''문자열 길이 구하기 : len 함수'''
a = "We all wish you the very best with what's next"
print(len(a))   # 46

'''문자열 인덱싱'''
a = 'Life is too short, You need python'
print(a[3])     # e
print(a[-1])    # n : [-1]은 문자열을 뒤에서부터 세어 첫번째가 되는 문자

'''문자열 슬라이싱 : 문자열에서 한 문자만 뽑아내는 것이 아닌 단어 뽑아내기'''
a = 'Life is too short, You need python'
print(a[0:4])   # Life : 0번부터 4번 까지
print(a[19:])   # You need python : 시작 번호부터 끝까지
print(a[:])     # Life is too short, You need python : 처음부터 끝까지
print(a[19:-7])     # You need : a[19]에서 a[-8] 까지를 의미한다.

'''슬라이싱으로 문자열 나누기'''
# 숫자 8을 기준으로 문자열 a를 양쪽으로 한번씩 슬라이싱
a = '20241005Rainy'
print(f'data : {a[:8]}')      # 20241005
print(f'weather : {a[8:]}')     # Rainy

'''문자열 포매팅 : 문자열 안의 특정한 값을 바꿔야 할 때 가능하게 해주는 것'''
'''%s : 문자열, %c : 문자 1개, %d : 정수, %f : 부동소수, %o : 8진수, %x : 16진수, %% : Literal % (문자 % 자체)'''
'''숫자 바로 대입'''
a = 'I eat %d apples.' %3   # %d : 문자열 포맷 코드
print(a)    # I eat 3 apples.

'''문자열 바로 대입'''
a = 'I eat %s apples.' %'five'
print(a)    # I eat five apples.

'''숫자 값을 나타내는 변수로 대입'''
num = 3
str = 'I eat %d apples.' %num
print(str)  # I eat 3 apples.

'''2개 이상의 값 넣기'''
num = 10
day = 'three'
str = 'I ate %d apples. so I was sick for %s days.' %(num, day)
print(str)  # I ate 10 apples. so I was sick for three days.

#### %s 포맷 코드는 자동으로 % 뒤에 있는 3이나 3.234와 같은 값을 문자열로 바꾸어 대입하기 때문에 d, f등을 생각하지 않아도 된다.
print('I have %s apples' %3)    
print('rate is %s' %3.234)

'''포매팅 연산자 %d와 %를 같이 쓰려면 %%를 쓴다.'''
a = 'Error is %d%%' %98
print(a)    # Error is 98%

'''포맷 코드와 숫자 함께 사용하기'''
'''정렬과 공백'''
# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미
print('%10s' % 'hi')    #         hi   (00000000hi)     

# %-10s : hi를 왼쪽으로 정렬하고 나머지는 공백으로 채움 (hi00000000jane)
print('%-10sjane.' % 'hi')      # hi        jane.

'''format 함수를 사용한 포매팅'''
'''숫자 바로 대입하기'''
print('i eat {0} apples'.format(3))     # i eat 3 apples

'''문자열 바로 대입하기'''
print('i eat {0} apples'.format('five'))    # i eat five apples

'''숫자 값을 가진 변수로 대입하기'''
num = 10
day = 'three'
print('i ate {0} apples. so i was sick for {1} days'.format(num, day))  # i ate 10 apples. so i was sick for three days

'''이름으로 넣기'''
print('i ate {num} apples. so i was sick for {day} days'.format(num=10, day=3))     # i ate 10 apples. so i was sick for 3 days

'''인덱스와 이름을 혼용해서 넣기'''
print('i ate {0} apples. so i was sick for {day} days'.format(10, day=3))   # i ate 10 apples. so i was sick for 3 days

''':< 왼쪽 정렬 / :> 오른쪽 정렬 / :^ 가운데 정렬'''
'''왼쪽 정렬'''
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.
print('{0:<10}'.format('hi'))

'''가운데 정렬'''
print('{0:^10}'.format('hi'))   #     hi    

'''공백 채우기'''
print('{0:=^10}'.format('hi'))      # ====hi====
print('{0:!<10}'.format('hi'))      # hi!!!!!!!!

'''{또는} 문자 표현하기'''
print('{{and}}'.format())   # {and}

'''f 문자열 포매팅'''
name = '파이썬'
age = 25
print(f'나의 이름은 {name}이고, 나이는 {age}')  # 나의 이름은 파이썬이고, 나이는 25
print(f'나는 내년이면 {age+1} 살이 된다.')      # 나는 내년이면 26 살이 된다.

# 딕셔너리
d = {'name':'안녕', 'age':25}
print(f"나의 이름은 {d['name']}이고, 나이는 {d['age']}입니다.")     # 나의 이름은 안녕이고, 나이는 25입니다.

print(f'{{and}}')   # {and}

'''문자열 관련 함수'''
'''문자 개수 세기 - count'''
a = 'hobby'
print(a.count('b'))     # 2

'''위치 알려주기 - find'''
a = 'python is the best choice'
print(a.find('b'))      # 14 : 문자열에서 b거 처음으로 나온 위치 반환
print(a.find('k'))      # -1 : 찾는 문자나 문자열이 존재하지 않으면 -1 반환

'''위치 알려주기 - index'''
a = 'Life is too short'
print(a.index('t'))     # 8
# print(a.index('k'))     # ValueError: substring not found : k가 없으므로 오류 발생

'''문자열 삽입 - join'''
print(','.join('abcd'))     # a,b,c,d

# 리스트나 튜플도 입력으로 사용할 수 있다.
print(','.join(['a','b','c','d']))      # # a,b,c,d

'''소문자를 대문자로 바꾸기 - upper'''
a = 'hi'
print(a.upper())    # HI

'''대문자를 소문자로 바꾸기 - lower'''
a = 'HI'
print(a.lower())    # hi

'''왼쪽 공백 지우기 - lstrip'''
a = ' hi '
print(a.lstrip())

'''오른쪽 공백 지우기 - rstrip'''
a = ' hi '
print(a.rstrip())    #  hi

'''양쪽 공백 지우기 - strip'''
a = ' hi '
print(a.strip())

'''문자열 바꾸기 - replace'''
a = 'life if too short'
print(a.replace('life', 'your leg'))    # your leg if too short

'''문자열 나누기 - split'''
a = 'life if too short'
print(a.split())    # ['life', 'if', 'too', 'short'] : 공백을 기준으로 문자열 나눔
b = 'a:b:c:d'
print(b.split(':'))     # ['a', 'b', 'c', 'd'] : :를 기준으로 문자열 나눔

# 문자열은 값을 변경할 수 없는 immutable (불변성) 자료형이다.
# upper, lower, join, lstrip, rstrip, strip, replace, split 함수는 immutable 규칙이 적용되어
# 문자열 자체의 값이 변경되는게 아니라 변경된 값을 리턴한다.