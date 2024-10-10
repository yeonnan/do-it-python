'''
abs
abs(x) : 어떤 숫자를 입력받았을 때 그 숫자의 절댓값을 리턴하는 함수
'''
print(abs(3))       # 3
print(abs(-3))      # 3
print(abs(-1.2))        # 1.2


'''
all
all(x) : 반복 가능한 데이터 x를 입력값으로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
반복가능한 데이터란 for문에서 사용할 수 있는 자료형을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
'''
print(all([1,2,3]))     # True
print(all([1,2,3,0]))       # False. 요소 0은 거짓이므로 False 리턴
print(all([]))      # True. all의 입력 인수가 빈 값인 경우에는 True 리턴


'''
any
any(x) : 반복 가능한 데이터 x를 입력으로 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고
x가 모두 거짓일 때만 False를 리턴. 즉, all(x)의 반대로 작동한다.
'''
print(any([1,2,3,0]))       # True. 1,2,3이 참이므로 True 리턴
print(any([0, '']))     # False. 0과 ''은 모두 거짓이므로 False 리턴
print(any([]))      # False. any의 입력 인수가 빈 값인 경우에는 False 리턴


'''
chr
chr(i) : 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
'''
print(chr(97))      # a
print(chr(44032))       # 가


'''
dir
객체가 지닌 변수나 함수를 보여 주는 함수
'''
print(dir([1,2,3]))
print(dir({'1':'a'}))


'''
divmod
divmod(a,b) : 2개의 숫자 a,b를 입력으로 받고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
'''
print(divmod(7,3))      # (2, 1)


'''
enumerate
순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
enumerate 함수는 for 문과 함께 사용한다.
'''
# 자료형의 현재 순서(index)를 알 수 있다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar


'''
eval
eval(experssion) : 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값 리턴
'''
print(eval('1+2'))      # 3
print(eval("'hi'+'a'"))     # hia
print(eval('divmod(4,3)'))      # (1, 1)


'''
filter
filter(함수, 반복_가능한_데이터)

filter 함수는 첫번째 인수, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인것만 묶어서(걸러내서) 리턴한다.
'''
def positive(x):
    return x>0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))     # [1, 2, 6]


'''
hex
hex(x) : 정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수
'''
print(hex(234))     # 0xea
print(hex(3))       # 0x3


'''
id
id(object) : 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴하는 함수
'''
a = 3
print(id(3))        # 4365222192
print(id(a))        # 4365222192
b=a 
print(id(b))        # 4365222192

# 예 3, a, b는 고유 주소값이 모두 4365222192이다. 즉, 3, a, b가 모두 같은 객체를 가리키고 있다.


'''
input
input([pormpt]) : 사용자 입력을 받는 함수. 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
'''
# a = input()
# print(a)


'''
int
int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수
'''
print(int(3))       # 3
print(int(3.4))     # 3


'''
isinstance
isinstance(object, class) : 첫번째 인수로 객체, 두번째 인수로 클래스를 받는다. 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False 리턴
'''
class Person:pass       # 아무런 기능이 없는 Person 클래스 생성
a = Person()        # Person 클래스의 인스턴스 a 생성
print(isinstance(a, Person))       # a가 Person 클래스의 인스턴스인지 확인. True

b = 3
print(isinstance(b, Person))        # False


'''
len
len(s) : 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수
'''
print(len('python'))        # 6
print(len([1,2,3]))         # 3
print(len((1, 'a')))        # 2


'''
list
list(iterable) : 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수
'''
print(list('python'))       # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))        # [1, 2, 3]

# list 함수에 리스트를 입력하면 똑같은 리스트를 복사하여 리턴한다.
a = [1,2,3]
b = list(a)
print(b)        # [1, 2, 3]


'''
map
map(f, iterable) : 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수이다.
'''
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))      # [2, 4, 6, 8]


'''
max
max(iterable) : 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수
'''
print(max([1,2,3]))         # 3
print(max('python'))        # h


'''
oct
oct(x) : 정수를 8진수 문자열로 바꾸어 리턴하는 함수
'''
print(oct(34))      # 0o42
print(oct(12345))       # 0o30071


'''
ord
ord(C) : 문자의 유니코드 숫자 값을 리턴하는 함수
'''
print(ord('a'))     # 97
print(ord('가'))      # 44032


'''
pow
pow(x,y) : x를 y제곱한 결괏값을 리턴하는 함수
'''
print(pow(2,4))     # 16
print(pow(3,3))     # 27


'''
range
range([start], stop, [step]) : for문과 함께 자주 사용하는 함수. 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴
'''
'''1. 인수가 하나일 경우 - 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.'''
print(list(range(5)))       # [0, 1, 2, 3, 4]

'''2. 인수가 2개일 경우 - 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타내며, 끝 숫자는 해당 범위에 포함되지 않는다.'''
print(list(range(5,10)))        # [5, 6, 7, 8, 9]

'''3. 인수가 3개일 경우 - 세번째 인수는 숫자 사이의 거리를 말한다.'''
print(list(range(1, 10, 2)))        # [1, 3, 5, 7, 9]
print(list(range(0, -10, -1)))      # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


'''
round
round(number [,ndigits]) : 숫자를 입력받아 반올림해 리턴하는 함수
[,ndigits] : ndigits가 있을 수도 있고, 없을 수도 있다는 의미
'''
print(round(4.6))       # 5
print(round(4.2))       # 4
print(round(5.678, 2))      # 5.68


'''
sorted
sorted(iterable) : 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수
'''
print(sorted([3,1,2]))      # [1, 2, 3]
print(sorted(['a','c','b']))        # ['a', 'b', 'c']
print(sorted('zero'))       # ['e', 'o', 'r', 'z']
print(sorted((3,2,1)))      # [1, 2, 3]


'''
sum
sum(iterable) : 입력 데이터의 합을 리턴하는 함수
'''
print(sum([1,2,3]))     # 6
print(sum([4,5,6]))     # 15


'''
tuple
tuple(iterable) : 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수
'''
print(tuple('abe'))     # ('a', 'b', 'e')
print(tuple([1,2,3]))       # (1, 2, 3)
print(tuple((1,2,3)))       # (1, 2, 3)


'''
type
type(object) : 입력값의 자료형이 무엇인지 알려 주는 함수
'''
print(type('abc'))
print(type([]))
print(type(open('test','w')))       # <class '_io.TextIOWrapper'> : 파일 자료형


'''
zip : 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
'''
print(list(zip([1,2,3], [4,5,6])))      # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3], [4,5,6], [7,8,9])))     # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip('abc', 'def')))        # [('a', 'd'), ('b', 'e'), ('c', 'f')]