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