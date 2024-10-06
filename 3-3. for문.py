'''
for문

for 변수 in 리스트(또는 튜플, 문자열):
    수행할문장
'''

'''전형적인 for문'''
test_list = [1, 2, 3]
for i in test_list:     # 1, 2, 3을 순서대로 i에 대입
    print(i)

print('=================')

'''다양한 for문의 사용'''
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)

print('=================')

'''for 문의 응용'''
# 총 5명의 학생이 시험을 봤는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다.
# 합격인지, 불합격인지 결과 리턴
marks = [90, 25, 67, 45, 80]    # 학생들 시험 점수

number = 0      # 학생에게 붙여줄 번호
for mark in marks:
    number += 1
    if mark >= 60:
        print(f'{number}번 학생은 합격입니다.')
    else:
        print(f'{number}번 학생은 불합격입니다.')

print('=================')

'''
for문과 continue문
for문 안의 문장을 수행하는 도중 continue문을 만나면 for문의 처음으로 돌아가게 된다.
'''
# 60점 이상인 사람에게는 축하 메세지를 보내고 나머지 사람에게는 아무런 메세지도 전하지 않는 프로그램
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print(f'{number}번 학생 합격을 축하합니다.')

print('=================')


'''range 함수'''
a = range(10)
print(a)    # range(0, 10)

# 1부터 10까지 더하기
add = 0
for i in range(1, 11):
    add += i
print(add)      # 55

print('=================')

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number]<60:
        continue    # 점수가 60점 미만이면 맨 처음으로 돌아간다.
    print(f'{number+1}번 학생 합격을 축하합니다.')

print('=================')

# 1부터 100까지 더하기
num = 0
for i in range(1, 101):
    num += i
print(f'1부터 100까지 더하기 : {num}')

print('=================')

# 구구단
for i in range(2, 10):      # 2부터 9까지의 숫자
    for j in range(1, 10):      # 1부터 9까지의 숫자
        print(i*j, end=' ')     # end='' : 해당 결괏값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속 출력하기 위해 
    print('')       # 2단, 3단 등을 구분하기 위해. 두번째 for문이 끝나면 결괏값을 다음 줄부터 출력하게 하는 역할

print('=================')

'''리스트 컴프리헨션 사용'''
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)   # [3, 6, 9, 12]

print('=================')

# 위의 문장을 더 간단하게 작성할 수 있다.
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

# [1,2,3,4] 중 짝수에만 3을 곱하여 담고 싶으면 리스트 컴프리헨션 안에 if를 사용하면 된다.
a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2==0]
print(result)   # [6, 12]

'''
리스트 컴프리헨션 문법
[표현식 for 항목 in 반복_가능_객체 if 조건문]

for문을 여러개 사용할 때 문법
[표현식 for 항목1 in 반복_가능_객체1 if 조건문1
       for 항목n in 반복_가능_객체n if 조건문n]
'''

print('=================')

# 구구단의 모든 결과를 리스트에 담고싶다면 리스트 컴프리헨션을 사용하여 할 수 있다.
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]
print(result)