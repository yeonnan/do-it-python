'''
문장을 반복해서 수행해야 할 경우 while문을 사용한다.

while 조건문:
    수행할 문장

while 문은  조건문이 참일 동인 while 문에 속한 문장들이 반복해서 수행된다.
'''

# 열 번 찍어 안넘어가는 나무 없다
hit = 0     # 나무를 찍은 횟수
while hit < 10:     # 나무를 찍은 횟수가 10보다 작은 동안 반복
    hit = hit + 1   # 나무를 찍은 횟수 1씩 증가
    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:      # 나무를 열번 찍으면
        print('나무 넘어갑니다.')


'''while문 만들기'''
# 여러 가지 선택지 중 하나를 선택해서 입력받는 예제
prompt = """
1. add
2. del
3. list
4. quit
enter number: """

# number = 0      # 번호를 입력받을 변수
# while number != 4:      # 입력받은 번호가 4가 아닌 동안 반복
#     print(prompt)
#     number = int(input())


'''while문 강제로 빠져나가기'''
coffee = 10     # 커피가 10개 있다.
money = 300     # 넣을 돈은 300원
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1     # while문을 한 번 돌때마다 커피가 1개씩 줄어든다.
    print(f'남은 커피의 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break


# coffee = 10
# while True:
#     money = int(input('돈을 넣어주세요: '))
#     if money == 300:
#         print('커피를 줍니다.')
#         coffee = coffee - 1
#     elif money > 300:
#         print('거스름돈 %d를 주고 커피를 줍니다.' % (money - 300))
#         coffee = coffee - 1
#     else:
#         print('돈을 다시 돌려주고 커피를 주지 않습니다.')
#         print('남은 커피의 양은 %d개 입니다.' % coffee)
#     if coffee == 0:
#         print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
#         break


'''
while문의 맨 처음으로 돌아가기 - continue
조건에 맞지 않을 때 while문을 빠져나가는 것이 아닌 while 문의 맨 처음으로 다시 돌아가는 것
'''
# 1부터 10까지의 숫자 중 홀수만 출력하는 것
a = 0
while a < 10:
    a = a+1
    if a%2 == 0: continue   # a를 2로 나누었을 때 나머지가 0이면 맨 처음으로 돌아간다.
    print(a)


'''
무한 루프
while True:
    수행 문장
'''
while True:
    print('ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.')
    print('🧨💣🧨💣🧨💣🧨💣🧨💣🧨💣')
    print('🧨💣🧨💣🧨💣🧨')