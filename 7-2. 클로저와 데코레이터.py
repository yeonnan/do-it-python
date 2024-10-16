'''
클로저 : 함수 안에 내부 함수를 구현하고 그 내부 함수를 리턴하는 함수
이때 외부 함수는 자신이 가진 변수값 등을 내부 함수에 전달할 수 있다.
'''
# 어떤 수에 항상 3을 곱해 리턴하는 함수
def mul3(n):
    return n*3

# mul3()함수는 입력으로 받은 수 n에 항상 3을 곱하여 리턴한다. 이번에는 항상 5를 곱하여 리턴하는 함수
def mul5(n):
    return n*5

# 필요할 때 마다 함수를 만드는 것은 매우 비효율적이며, 클래스를 사용하면 된다.
class Mul:
    def __init__(self, m):
        self.m = m
    
    def mul(self, n):
        return self.m * n

if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))     # 30
    print(mul5.mul(10))     # 50

# __call__ 메서드를 이용해 개선
class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n
    
if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))
    print(mul5(10))

# mul() 함수의 이름을 __call__로 바꾸었는데, __call__함수는 Mul 클래스로 만든 객체에 인수를 전달하여 바로 호출할 수 있도록 하는 메서드이다.


'''
데코레이터
'''
import time

def elapsed(original_func):     # 기존 함수를 인수로 받는다.
    def wrapper(): 
        start = time.time()
        result = original_func()        # 기존 함수를 수행한다.
        end = time.time()
        print('함수 수행 시간: %f초' %(end-start))      # 기존 함수의 수행 시간을 출력한다.
        return result       # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

def myfunc():
    print('함수가 실행됩니다.')

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()

# 데코레이터는 @문자를 이용해 함수 위에 적용하여 사용한다.
def elapsed(original_func):     # 기존 함수를 인수로 받는다.
    def wrapper(): 
        start = time.time()
        result = original_func()        # 기존 함수를 수행한다.
        end = time.time()
        print('함수 수행 시간: %f초' %(end-start))      # 기존 함수의 수행 시간을 출력한다.
        return result       # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    print('함수가 실행됩니다.')

# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()

# 데코레이터 함수는 기존 함수의 입력 인수에 상관없이 동작하도록 만들어야 한다.
# 데코레이터는 기존 함수가 어떤 입력 인수를 취할지 알 수 없기 때문이다.
# 기존 함수의 입력 인수를 알 수 없는 경우에는 *args와 **kwargs 매개변수를 이용하면 된다.

def elapsed(original_func):     # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):       # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs)     # *args, **kwargs를 입력 인수로 기존 함수 수행
        end = time.time()
        print('함수 수행 시간: %f초'%(end-start))       # 수행 시간을 출력한다.
        return result       # 함수의 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc(msg):
    '''데코레이터 확인 함수'''
    print('"%s"을 출력합니다.'%msg)

myfunc('you need python')