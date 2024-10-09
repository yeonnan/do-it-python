'''
사용자가 입력한 값 변수에 대입

input : 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.
'''
a = input()
print(a)

'''
프롬프트 띄워 사용자 입력받기
입력을 받을 때 안내문구나 질문을 보여주면서 프롬프르 띄워주기

input('안내_문구')
'''

# input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열이다.
number = input('숫자를 입력하세요: ')
print(number)


'''
print

큰따옴표로 둘러싸인 문자열은 +연산과 동일하다.
'''
print("hello" "world")      # helloworld
print("hello"+"world")      # helloworld

'''문자열 띄워쓰기는 쉼표로 한다.'''
print('hello','world')      # hello world

'''
한줄에 결과값 출력하기
한줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.
'''
for i in range(10):
    print(i, end=' ')       # end 매개변수의 초깃값은 줄바꿈(\n) 문자