'''
튜플은 리스트와 비슷하지만 ()를 이용하여 만든다는 점과
그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
'''

# 튜플의 요소값을 바꾸거나 지우려고 하면 어떻게 될까?
t1(1,2,'a','b')
del t1[0] # 오류가 난다!
t1[0] = 'c' # 역시 오류가 난다!

#튜플도 리스트와 마찬가지로 인덱싱, 슬라이싱, 더하기, 곱하기가 된다