'''
집합은 set 키워드를 사용해 만들 수 있다.
'''
s1 = set([1, 2, 3])
print(s1)   # {1, 2, 3}

s2 = set('Hello')
print(s2)   # {'e', 'l', 'H', 'o'}

'''
set('Hello') 의 결과가 이상한 이유는 set의 2가지 특징 때문이다.
- 중복을 허용하지 않는다.
- 순서가 없다. -> 중복을 허용하지 않기 때문에 데이터의 중복을 제거하기 위한 필터로 사용된다.
'''


'''
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 요솟값을 얻을 수 있지만, 
set은 순서가 없기 때문에 인덱싱을 통해 요솟값을 얻을 수 없다.
set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후에 해야한다.
'''
s1 = set([1, 2, 3])
l1 = list(s1)   # 리스트로 변환
print(l1)       # [1, 2, 3]

t1 = tuple(s1)  # 튜플로 변환
print(t1)       # (1, 2, 3)

print(t1[0])    # 1

'''교집합, 합집합, 차집합 구하기'''
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

'''교집합 구하기'''
# & 사용
print(s1 & s2)      # {4, 5, 6}
# intersection 함수 사용
print(s1.intersection(s2))      # {4, 5, 6}

'''합집합 구하기'''
# | 사용
print(s1|s2)        # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# union 함수 사용
print(s1.union(s2))     # {1, 2, 3, 4, 5, 6, 7, 8, 9}

'''차집합 구하기'''
# - 사용
print(s1-s2)    # {1, 2, 3}
print(s2-s1)    # {8, 9, 7}
# difference 함수 사용
print(s1.difference(s2))        # {1, 2, 3}
print(s2.difference(s1))        # {8, 9, 7}

'''집합 자료형 관련 함수'''
'''값 1개 추가하기 - add'''
s1 = set([1, 2, 3])
s1.add(4)
print(s1)       # {1, 2, 3, 4}

'''값 여러 개 추가하기 - update'''
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)       # {1, 2, 3, 4, 5, 6}

'''특정 값 제거하기 - remove'''
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)       # {1, 3}