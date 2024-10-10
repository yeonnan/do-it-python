'''
try-except 문
try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

기본구조
try:
    ...
except [발생_오류 [as 오류_변수]]:
    ...

###
except 구문을 보면 []를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례적인 표기법이다.
except 구문은 3가지 방법으로 사용 가능하다.

1. try-except만 쓰는 방법. 이 경우에는 오류의 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.
try:
    ...
except:
    ...

2. 발생 오ㅗ류만 포함한 except문. 이 경우는 오류가 발생했을 때 except 문에 미리 정해둔 오류와 동일한 오류일 경우에만 except 블록을 수행한다는 뜻이다.
try:
    ...
except 발생_오류:
    ...

3. 발생 오류와 오류 변수까지 포함한 except문. 이 경우 두번째 경우에서 오류의 내용까지 알고 싶을 때 사용하는 방법이다.
try:
    ...
except 발생_오류 as 오류_변수:
    ...
'''

# 3번 오류
# 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고
# 오류 변수 e에 담기는 오류 메세지를 출력할 수 있다. -> division by zero
try:
    4/0
except ZeroDivisionError as e:
    print(e)


'''
try-finally문
finally 절은 try문 수행 도중 예외 발생 여부에 상관 없이 항상 수행된다.
보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용한다.
'''
try:
    f = open('helloworld.txt', 'w')
    # 무언가를 수행
finally:
    f.close()       # 중간에 오류가 발생하더라도 무조건 실행

# helloworld.txt 파일을 쓰기 모드로 연 후 예외 발생 여부에 상관없이 항상 파일을 닫아 주려면 try-finally 문을 사용하면 된다.


'''
여러 개의 오류 처리하기
try:
    ...
except 발생_오류1:
    ...
except 발생_오류2:
    ...

즉, 0으로 나누는 오류와 인덱싱 오류를 처리할 수 있다.
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱할 수 없습니다.')


'''
try-else문
try:
    ...
except:
    ...
else:       # 오류가 없을 경우에만 수행
    ...

try 문 수행 중 오류가 발생하면 except절, 오류가 발생하지 않으면 else 절이 수행된다.
'''
try:
    age = int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')