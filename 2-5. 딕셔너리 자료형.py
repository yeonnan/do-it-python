'''딕셔너리 : key-value
리스트나 튜플처럼 순차적으로 해당 요소 값을 구하지 않고 key를 통해 value를 얻는다.
{key1:value1, key2:value2, ...}
'''

'''딕셔너리 쌍 추가하기'''
a = {1:'a'}
a[2] = 'b'      # {2:'b'} 쌍 추가
print(a)    # {1: 'a', 2: 'b'}

a['name'] = 'jay'   # {'name':'jay'} 쌍 추가
print(a)    # {1: 'a', 2: 'b', 'name': 'jay'}

a[3] = [1, 2, 3]    # {3:[1, 2, 3]} 쌍 추가
print(a)    # {1: 'a', 2: 'b', 'name': 'jay', 3: [1, 2, 3]}

'''딕셔너리 요소 삭제하기'''
del a[1]    # key가 1인 key:value 쌍 삭제
print(a)    # {2: 'b', 'name': 'jay', 3: [1, 2, 3]}

'''딕셔너리 사용하기'''
'''딕셔너리에서 key를 사용해 value 얻기'''
a = {1:'a', 2:'b'}
print(a[1])     # a : key가 1인 요소의 value 반환
print(a[2])     # b : key가 2인 요소의 value 반환

dict = {'name':'jay', 'phone':'010-1234-5678', 'birth':'1212'}
print(dict['name'])
print(dict['phone'])
print(dict['birth'])

'''딕셔너리 만들 때 주의사항'''
'''딕셔너리에서 key는 고유한 값이므로 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
동일한 key가 2개 존재할 경우, 1:'a' 쌍이 무시된다. '''
a = {1:'a', 1:'b'}  # 1이라는 key 값이 중복으로 사용
print(a)    # {1: 'b'}

'''
key에는 리스트를 쓸 수 없지만, 튜플은 key로 쓸 수 있다.
딕셔너리의 key의 사용 유무는 key가 변하는 값인지, 변하지 않는 값인지에 달려 있다.
'''
# a = {[1,2]:'hi'}    # 리스트를 key로 사용
# TypeError: unhashable type: 'list'

'''딕셔너리 관련 함수'''
'''key 리스트 만들기 - keys'''
# a.keys() : 딕셔너리 a의 key만 모아 dict_keys 객체를 리턴 한다.
a = {'name':'jay', 'phone':'010-1234-5678', 'birth':'1212'}
print(a.keys())     # dict_keys(['name', 'phone', 'birth'])

'''value 리스트 만들기 - values'''
print(a.values())   # dict_values(['jay', '010-1234-5678', '1212'])

'''key, value 쌍 얻기 - items'''
# key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴
print(a.items())    # dict_items([('name', 'jay'), ('phone', '010-1234-5678'), ('birth', '1212')])

'''key:value 쌍 모두 지우기 - clear'''
a.clear()
print(a)    # {}

'''key로 value 얻기 - get'''
a = {'name':'jay', 'phone':'010-1234-5678', 'birth':'1212'}
print(a.get('name'))    # jay
print(a.get('phone'))   # 010-1234-5678
print(a.get('nokey'))   # 값이 없으면 None 반환

'''
딕셔너리 안에 찾으려는 key가 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는
get(x, '디폴트 값')을 사용하면 편리하다.
'''
print(a.get('nokey', 'foo'))    # foo

'''해당 key가 딕셔너리 안에 있는지 조사하기 - in'''
a = {'name':'jay', 'phone':'010-1234-5678', 'birth':'1212'}
print('name' in a)      # True
print('email' in a)     # False