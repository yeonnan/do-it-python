'''
변수 : 파이썬에서 사용하는 변수는 객체를 가리키는 것
객체 : 지금까지 보아 온 자료형의 데이터(값)와 같은 것을 의미하는 말
'''

# [1, 2, 3] 값을 가지는 리스트 데이터(객체)가 자동으로 메모리에 생성되고 
# 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.
a = [1, 2, 3]

# 변수 a가 가리키는 메모리 주소 확인
print(id(a))    # 4346432768


'''리스트 복사'''
a = [1, 2, 3]
b = a

# b변수에 a 변수를 대입하면 b는 a와 완전히 동일하다.
# 하지만, [1, 2, 3]이라는 리스트 객체를 참조하는 변수가 a변수 1개에서 b변수가 추가되어 2개로 늘어났다는 차이가 있다.
print(f'a : {id(a)}')   # a : 4375935360
print(f'b : {id(b)}')   # b : 4375935360

# id(a), id(b) 값이 동일하다 -> a가 가리키는 대상과 b가 가리키는 대상이 동일하다.
# 동일한 객체를 가리키고 있는지에 대한 판단은 파이썬 명령어 is를 사용해도 참을 리턴한다.
print(a is b)   # a와 b가 가리키는 객체가 같을까? True

a[1] = 4
print(a)    # [1, 4, 3]
print(b)    # [1, 4, 3]

'''b 변수를 생성할 때 a변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만들기'''
'''[:] 이용'''
# 리스트 전체를 가리키는 [:]을 사용해서 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)    # [1, 4, 3]
print(b)    # [1, 2, 3]

'''copy 모듈 이용'''
from copy import copy   # copy 모듈에 있는 copy 함수 import
a = [1, 2, 3]
b = copy(a)     # copy 함수 사용. b=a[:]과 동일하다.

# 두 변수의 값은 같지만 서로 다른 객체를 가리키고 있다.
print(b is a)   # False


'''변수를 만드는 여러 방법'''
'''튜플로 a, b에 값 대입 가능'''
a, b = ('python', 'helloworld')
print(f'a, b : {a,b}')      # a, b : ('python', 'helloworld')

'''리스트로 변수 만들기'''
[a, b] = ['python', 'helloworld']

'''여러 개의 변수에 같은 값 대입 가능'''
a = b = 'python'

'''여러 개의 변수에 같은 값 대입 방법으로 두 변수의 값을 간단하게 바꿀 수 있다.'''
a = 3
b = 5
a, b = b, a     # a와 b의 값을 바꿈
print(a)    # 5
print(b)    # 3