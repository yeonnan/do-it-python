'''
인코딩

유니코드 문자열은 인코딩 없이 그대로 파일에 적거나 다른 시스템으로 전송할 수 없다.
왜냐하면 유니코드 문자열은 단순히 문자 셋의 규칙이기 때문.
파일에 적거나 다른 시스템으로 전송하려면 바이트 문자열로 변환해야 한다. 
유니코드 문자열을 바이트 문자열로 바꾸는 것을 인코딩이라 한다.
'''

# 유니코드 문자열을 바이트 문자열로 바꾸기
a = 'hello world'
b = a.encode('utf-8')
print(b)        # b'hello world'
print(type(b))      # <class 'bytes'>

a = '한글'
print(a.encode('euc-kr'))       # b'\xc7\xd1\xb1\xdb'
print(a.encode('utf-8'))        # b'\xed\x95\x9c\xea\xb8\x80'


'''
디코딩

인코딩한 바이트 문자열을 유니코드 문자열로 변환하는 디코딩
euc-kr로 인코딩한 바이트 문자열은 euc-kr로만 디코딩해야 한다.
'''
a = '한글'
b = a.encode('euc-kr')
print(b.decode('euc-kr'))       # 한글


'''
입출력과 인코딩

파일을 읽거나 네트워크를 통해 데이터를 주고받을 때 추천하는 방법
1. 입력으로 받은 바이트 문자열은 되도록 빨리 유니코드 문자열로 디코딩한다.
2. 함수나 클래스 등에서는 유니코드 문자열만 사용한다.
3. 입력에 대한 결과를 전송하는 마지막 부분에서만 유니코드 문자열을 바이트 문자열로 인코딩해서 반환한다.
'''

# 1. euc-kr로 작성된 파일 읽기
with open('euc_kr.txt', encoding='euc-kr') as f:
    data = f.read()     # 유니코드 문자열

# 2. unicode 문자열로 프로그램 수행하기
data = data + '\n' + '추가 문자열'

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)

# 파일을 읽는 open() 함수에는 encoding을 지정하여 파일을 읽는 기능이 있다.
# 이때 읽은 문자열은 유니코드 문자열이 된다.
# 이와 마찬가지로 파일을 만들 때도 encoding을 지정할 수 있다.
# encoding 항목을 생략하면 기본값으로 utf-8이 지정된다.