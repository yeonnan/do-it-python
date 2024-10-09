'''
# 계산기
result = 0
def add(num):
    global result       # 이전에 계산한 결과값을 유지하기 위해 result 전역 변수 사용
    result += num       # 결과값(result)에 입력값(num) 더하기
    return result       # 결과값 리턴

print(add(3))
print(add(4))
'''

'''
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
'''

# cal1, cal2 객체가 각각의 역할을 수행하며, 계산기의 결과값 역시 독립적인 값을 유지한다.


'''
클래스와 객체

과자틀=클래스, 과자 틀로 찍어낸 과자=객체
클래스(class)란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀), 
객체(object)란 클래스로 만든 피조물(과자 틀로 찍어낸 과자)을 뜻한다.

클래스로 만든 객체는 객체마다 고유한 성격을 가진다. 동일한 클래스로 만든 객체들은 서로 영향을 주지 않는다.
'''

'''
class Cookie:
    pass

# 객체는 클래스로 만들고 1개의 클래스는 무수히 많은 객체를 만들어낼 수 있다.
# 객체 만들기
a = Cookie()
b = Cookie()
'''

'''
객체와 인스턴스의 차이
클래스로 만든 객체를 인스턴스라 한다.
a = Cookie()로 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다.
즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
'''

#########

'''
사칙 연산 클래스 만들기

클래스 만들지 구상하기
'''
# a = FourCal()를 입력해서 a라는 객체를 만든다.
# a = FourCal()

# a.setdata(4,2)처럼 입력해서 숫자 4와 2를 a에 지정해준다.
# a.setdata(4,2)

# a.add()를 수행하면 두 수를 합한 결과 (4+2)를 리턴한다.
# a.add()     # 6. 더하기
# a.mul()     # 8. 곱하기
# a.sub()     # 2. 빼기
# a.div()     # 2. 나누기

'''클래스 구조 만들기'''
# class FourCal():
#     pass

'''객체에 연산할 숫자 지정하기'''
# 사용할 2개의 숫자를 a객체에게 알려주기
# a.setdata(4,2)

# 클래스 다시 지정
class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):       # 메서드의 매개변수
        self.first = first      # 메서드의 수행문 
        self.second = second
    def add(self):
        result = self.first + self.second
        print(result)
    def mul(self):
        result = self.first * self.second
        print(result)
    def sub(self):
        result = self.first - self.second
        print(result)
    def div(self):
        result = self.first / self.second
        print(result)
    
# a = FourCal()
# b = FourCal()
# a.setdata(4,2)
# b.setdata(3,8)

# __init__ 작성 후
a = FourCal(4,2)
b = FourCal(3,8)

a.add()
a.mul()
a.sub()
a.div()
b.add()
b.mul()
b.sub()
b.div()


'''
생성자
위의 코드에서 setdata 메서드를 수행하지 않고 add 메서드를 먼저 수행하면 오류가 발생한다.
setdata 메서드를 수행해야 객체 a의 인스턴스 변수 first, second가 생성되기 때문이다.
이렇게 객체에 first, second와 같은 초깃값을 생성해야할 필요가 있을때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다 생성자를 구현하는 것이 더 안전하다.

생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. __init__
'''


'''
클래스의 상속
class 클래스_이름(상속할_클래스_이름)
'''

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        print(result)

# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal의 모든 기능을 사용할 수 있다.
a = MoreFourCal(4, 2)
a.add()
a.pow()

# 상속은 MoreFourCal 클래스처럼 기존 클래스 FourCal는 그대로 나두고 클래스의 기능을 확장할 때 주로 사용한다.


'''
메서드 오버라이딩
부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것.
메서드 오버라이딩을 하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

a = FourCal(4,0)
a.div() 를 실행하면 ZeroDivisionError: division by zero 오류가 발생한다.
0으로 나눌 때 오류가 아닌 값 0을 리턴받는 방법은?
'''

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:        # 나누는 값이 0인 경우, 0을 리턴하도록 수정
            print(0)
        else:
            print(self.first/self.second)

a = SafeFourCal(4,0)
a.div()

# FourCal 클래스의 div 메서드를 동일한 이름으로 다시 작성
# 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 내용으로 다시 만드는 것을 메서드 오버라이딩이라고 한다.
# 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.


'''
클래스 변수
클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
'''
class Family:
    lastname = '안'     # lastname : 클래스 변수

# 클래스 변수는 클래스_이름.클래스_변수 로 사용 가능하다.
print(Family.lastname)

# 또는 Family 클래스로 만든 객체를 이용해도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)


Family.lastname = '박'
print(a.lastname)
# 위와 같이 클래스 변수의 값을 바꾸면 클래스로 만든 객체의 값도 모두 변경된다.
# 즉, 인스턴스 변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지하지만,
# 클래스변수는 클래스로 만든 모든 객체에 공유된다.