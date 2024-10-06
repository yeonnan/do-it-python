'''
참과 거짓을 나타내는 자료형으로 True, False 2가지 값만을 가질 수 있다.
'''

'''
'python' - 참
'' - 거짓
[1, 2, 3] - 참
[] - 거짓
(1, 2, 3) - 참
() - 거짓
{'a':1} - 참
{} - 거짓
1 - 참
0 - 거짓
None - 거짓

문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 False가 되고, 값이 있다면 True가 된다.
'''

'''불연산'''
print(bool('python'))   # True
print(bool(''))    # False
print(bool([1, 2, 3]))  # True
print(bool([])) # False
print(bool(0))  # False
print(bool(3))  # True