'''
    Key:Value로 저장을 하는 자료형이다.
    예를 들어
    people :사람, baseball:야구
    라고 저장을 한다면,
    baseball을 찾는다면 value가 야구가 된다.
'''

#딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b' # => a {2:'b', 1:'a'}

#딕셔너리 요소 삭제하기
del a[1] # => a {} a딕셔너리의 1번 key요소를 삭제한다

#딕셔너리 사용법

#key를 이용하여 value얻기
grade={'pey':10,'julliet':99}

'''
    만약 여기서
    grarde['pey']를 파이썬에서 실행을 시키면 10이 출력이 될 것이다.
    혹은 grade['julliet']을 실행할경우 99가 출력이 된다.
'''

#딕셔너리의 주의사항
'''
    wrong = {1:'a', 1:'b'}
    위와 같이 중복으로 저장을 할경우 마지막으로 저장된 값으로 저장이 된다.
    worng = {[1,2]:'hi'}
    위와 같이 리스트를 key값으로 설정할 수 없다.
'''

#딕셔너리 관련 함수들
#key리스트 만들기
a = {'name':'chan','phone':'01032543540','birth':'0128'}
a.keys()
#dict_keys(['name','phone','birth'])

#value리스트 만들기
a.vlaues()
#dict_values(['chan','01032543540','0128'])

#key, value 쌍 얻기
a.items()
#dict-items([('name','chan'), ('phone', '01032543540'),('birth':'0128')])

#key:value 쌍 모두 지우기
a.clear

#key로 value얻기
a = {'name':'chan','phone':'01032543540','birth':'0128'}
a.get('name') # -> 'chan'이 출력
'''
    딕셔너리 안에 찾으려는 key값이 없을 경우
    미리 정해둔 디폴트 값을 대신 가져오게 하고 싶을 때에는
    get(x,'디폴트 값')을 사용하면 편리하다.
'''

#해당 key가 딕셔너리 안에 있는지 조사하기
a = {'name':'chan','phone':'01032543540','birth':'0128'}
'name' in a
True
'email' in a
False
