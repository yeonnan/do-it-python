'''
함수
1. 반복적으로 사용되는 가치 있는 부분을 한 뭉치로 묶어 어떤 입력값을 주었을 때 어떤 결과값을 리턴해 준다
2. 프로그램을 기능 단위로 분리해 놓으면 프로그램 흐름 파악이 쉬움
'''


'''
함수의 구조
def 함수_이름(매개변수):
    수행할_문장

def는 함수를 만들 때 사용하는 예약어이며, 함수 이름은 함수를 만드는 사람이 임의로 만들 수 있다.
'''
# 함수의 이름은 add 이고 입력으로 2개의 값을 받으며 리턴값(출력값)은 2개의 입력값을 더한 값이다.
def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)    # add(3,4)의 리턴값을 c에 대입
print(c)


'''
매개변수와 인수
매개변수 : 함수에 입력으로 전달된 값을 받는 변수
인수 : 함수를 호출할 때 전달하는 입력값을 의미
'''
def add(a,b):       # a, b는 매개변수
    return a+b
print(add(3,4))     # 3, 4는 인수


'''
입력값과 리턴값에 따른 함수의 형태

일반적인 함수
입력값이 있고 리턴값이 있는 함수
def 함수_이름(매개변수):
    수행할_문장
    return 리턴값
'''
def add(a, b):
    result = a+b
    return result   

a = add(3, 4)
print(a)

# 사용법
# 리턴값을_받을_함수 = 함수_이름(입력인수1, 입력인수2)

'''입력값이 없는 함수'''
def say():
    return 'hi'

# 해당함수를 사용하기 위해서는 괄호 안에 아무런 값도 넣지 않아야 한다.
a = say()
print(a)

# 사용법
# 리턴값을_받을_변수 = 함수_이름()

'''리턴값이 없는 함수'''
def add(a, b):
    print('%d, %d의 합은 %d 입니다.' %(a,b,a+b))

add(3,4)

# 사용법
# 함수_이름(입력_인수1, 입력_인수2)

'''입력값도, 리턴값도 없는 함수'''
def say():
    print('hi')

say()

# 사용법
# 함수_이름()


'''매개변수를 지정하여 호출하기'''
def sub(a,b):
    return a-b

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
result = sub(a=7, b=3)
print(result)


'''
입력값이 몇개가 될지 모를때는 어떻게 해야할까
def 함수_이름(*매개변수):
    수행할_문장
'''

'''여러개의 입력값을 받는 함수 만들기'''
# add_many(1,2) 이면 3, add_many(1,2,3) 이면 6, add_many(1,2,3,4,5,6,7,8,9,10) 이면 55를 리턴하는 함수
# 매개변수 이름 앞에 *를 붙이면 입력값을 전부 모아 튜플로 만들어 주기 때문에 입력값이 몇개이든 상관없다.
def add_many(*args):
    result = 0
    for i in args:
        result += i     # *args에 입력받은 모든 값을 더한다.
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 매개변수로 *args 하나만 사용하는 것이 아닌, 여러개 사용하기
def add_mul(choice, *args):
    if choice == 'add':     # 매개변수 choice에 'add'를 입력받았을 때
        result = 0
        for i in args:
            result = result + i     # args에 입력받은 모든 값을 더한다.
    elif choice == 'mul':       # 매개변수 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result * i     # args에 입력받은 모든 값을 곱한다.
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)       # 15

result = add_mul('mul', 1,2,3,4,5)
print(result)       #  120


'''
키워드 매개변수. kwargs
키워드 매개변수를 사용할 때는 매개변수 앞에 **를 붙인다.
'''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)       # {'a': 1}
print_kwargs(name='foo', age=3)     # {'name': 'foo', 'age': 3}

# 함수의 입력값으로 a=1이 사용되면 kwargs는 {'a':1}이라는 딕셔너리가 된다.
# **kwargs처럼 매개변수 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 입력값이 그 딕셔너리에 저장된다.


'''함수의 리턴값은 언제나 하나'''
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)       # (7, 12)

# add_and_mul 함수의 리턴값 a+b와 a*b는 튜플값 하나인 (a+b,a*b)로 리턴된다.
# 하나의 튜플 값을 2개의 값으로 분리하여 받고 싶다면 아래와 같이 함수를 호출하면 된다.
result, result2 = add_and_mul(3,4)
print(result)
print(result2)


'''매개변수에 초깃값 미리 설정'''
def say_myself(name, age, man=True):
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}살 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

# 둘의 출력값이 동일
say_myself('가나다', 25)
say_myself('가나다', 25, True)
say_myself('라마바', 23, False)

# 매개변수를 미리 설정할때는 항상 뒤쪽에 둬야 한다.


'''함수 안에서 선언한 변수의 효력 범위'''
a = 1       # 함수 밖의 변수 a
def vartest(a):     # vartest 함수 선언
    a = a+1

vartest(a)      # vartest 함수의 입력값으로 a를 대입
print(a)        # a값 출력

# 2가 출력되는 것이 아닌 1이 실행된다.
# 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 함수만의 변수이기 때문이다.
# def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 상관없다.


'''
함수 안에서 함수 밖의 변수 변경하는 방법

return 사용하기
'''
a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)      # vartest(a)의 리턴값을 함수 밖의 변수 a에 대입
print(a)

'''global 명령어 사용'''
a = 1
def vartest():
    global a        # 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다.
    a = a+1

vartest()
print(a)


'''
lambda
함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들 때 사용한다.
'''

# 사용법
# 함수_이름 = lambda 매개변수1, 매개변수2 ... : 매개변수를_이용한_표현식

add = lambda a,b:a+b
result = add(3,4)
print(result)