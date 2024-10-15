'''datetime.date : 년, 월, 일을 날짜로 표현할 때 사용하는 함수'''
import datetime
day = datetime.date(2024,10,13)
print(day.weekday())    # 일요일 이므로 6


'''time'''
'''time.time : UTC를 사용하여 현재 시간을 실수 형태로 리턴'''
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난시간을 초 단위로 리턴
import time
print(time.time())      

'''time.localtiome : time.time()이 리턴한 실수값을 사용해서 연,월,시,분,초 의 형태로 변환'''
print(time.localtime(time.time()))

'''time.asctime : time.localtime가 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 반환'''
print(time.asctime(time.localtime(time.time())))

'''time.ctime : 항상 현재 시간만 리턴한다.'''
print(time.ctime())

'''time.strftime : 시간에 관계된 것을 세밀하게 표현하는 여러 포맷 코드 제공'''
# time.strftime('출력할_형식_포맷_코드', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))     # 10/15/24
print(time.strftime('%c', time.localtime(time.time())))     # Tue Oct 15 20:22:16 2024

'''time.sleep : 일정한 시간 간격을 두고 루프를 실행할 수 있다.'''
# for i in range(10):
#     print(i)
#     time.sleep(1)


'''math.gcd : 최대 공약수 구하기'''
import math
print(math.gcd(60, 100, 80))        # 20

'''math.lcm : 최소 공배수'''
print(math.lcm(15, 25))     # 75


'''random : 난수를 발생시키는 모듈'''
import random
print(random.random())

# 1에서 10 사이의 정수 중에서 난수 값 리턴
print(random.randint(1, 10))

# 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 리턴하
# random.choice : 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

print(random_pop([1,2,3,4,5]))

# random.sample 리스트의 항목을 무작위로 섞기
# len(data) : 무작위로 추출할 원소의 개수를 의미.  (data, 3) : 리스트에서 무작위로 3개 추출
data = [1,2,3,4,5]
print(random.sample(data, len(data)))
print(random.sample(data, 3))


'''itertools.zip_longest : 같은 개수의 자료형을 묶는 내장함수, 전달한 반복 가능 객체의 길이가 서로 다르다면 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.'''
students = ['a', 'b', 'c', 'd', 'e']
snacks = ['사탕', '초콜릿', '젤리']
result = zip(students, snacks)
print(list(result))     # [('a', '사탕'), ('b', '초콜릿'), ('c', '젤리')]

# students의 요소 개수가 snacks보다 많을 때 채우기
import itertools
result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))     # [('a', '사탕'), ('b', '초콜릿'), ('c', '젤리'), ('d', '새우깡'), ('e', '새우깡')]

'''itertools.permutation : 반복 가능한 객체 중 r개를 선택한 순열을 이터레이터로 리턴'''
print(list(itertools.permutations(['1', '2', '3'], 2)))     # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# 만들 수 있는 2자리 숫자들
for a, b in itertools.permutations(['1','2','3'], 2):
    print(a+b)

'''itertools.combination : 반복 가능한 객체 중 r개를 선택한 조합을 이터레이터로 리턴'''
# print(list(itertools.combinations(range(1, 46), 6)))

# 순환하여 출력하지 않고 이터레이터의 개수만 세어보기
print(len(list(itertools.combinations(range(1, 46), 6))))       # 8145060


'''functools.reduce : 함수를 반복 가능한 객체의 요소에 차례대로 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수'''
import functools

# functools.reduce를 사용하면 reduce()에 선언한 람다 함수를 data 요소에 차례대로 누적적용 하여 계산. ((((1+2)+3)+4)+5)
data = [1,2,3,4,5]
result = functools.reduce(lambda x,y: x+y, data)
print(result)       # 15


'''operator.itemgetter : sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈'''
from operator import itemgetter
students = [
    ('a', 22, 'A'),
    ('b', 32, 'B'),
    ('c', 17, 'B')
]
result = sorted(students, key=itemgetter(1))    # itemgetter(1) : 튜플의 두번째 요소를 기준으로 정렬
print(result)       # [('c', 17, 'B'), ('a', 22, 'A'), ('b', 32, 'B')]