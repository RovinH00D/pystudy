#작은 따옴표나 큰 따옴표 넣기
food = 'python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"

#여러줄 짜리 문자열
multiline = '''
Life is too short
You need Python
'''#큰 따옴표로 대체 가능

#문자열에 더하기, 곱하기가 사용 가능

#문자열 인덱싱
a = "Life is too short, You need Python"
a[0] # => 문자열중 0번째 문자인 'L'출력
a[-1] # => 문자열 중 -1번째 == 마지막 문자인 n출력

#문자열 슬라이싱
a[0:4] # => 문자열 중 0~3번째 문자인 'Life'출력

#포매팅
#숫자 바로 대입
"I eat %d apples." % 3 # => I eat 3 apples

#문자열 바로 대입
"I eat %s apples" % "five" #v => I eat five apples

#변수 대입
number = 3

"I eat %d apples" % number

#2개이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
# => I ate 10 apples. so I was sick for three days.

#문자 수 세기
a = "hobby"
a.count('b') # => 2

#위치 알려주기 1(find)
a = "Python is best choice"
a.find('b') # => 10
a.find('k') # => -1 존재 하지 않으면 -1을 반환

#위치 알려주기 2 (index)
a = "Life is too short"
a.index('t') # => 8
a. index('k') # => 오류

#문자열 삽입
a = ","
a.join('abcd')
'a,b,c,d'

#소문자 -> 대문자
a = "hi"
a.upper() # 'HI'

#대문자 -> 소문자
a = "HI"
a.lower() # 'hi'

#공백지우기
a = "   hi   "
a.lstrip() # 'hi   '
#lstrip 은 왼쪽, rstrip은 오른쪽, 양쪽 공백은 strip으로 공백을 지울 수 있다

#문자열 바꾸기
a = "Life is too short"
a.replace("LIfe", "Your leg") # Your leg is too short

#문자열 나누기
a = "Life is too short"
a.split()
#['Life', 'is', 'too', 'short']     split의 기준을 설정하지 않으면 공백을 기준으로 나눈다
a = "a:b:c:d"
a.split(':')
#['a','b','c','d']

#format함수
#문자열 채우기
"I eat {0} apples".format(3) #'I eat 3 apples'
number = 3
"I eat {0} apples".format(number) #'I eat 3 appels'
number = 10
day = 'three'
"I ate {0} apples. so I was sick for {1} days.".format(number,day)


#정렬
"{0:<10}".format("hi") # 'hi        '
"{0:>10}".format("hi") # '        hi'
"{0:^10}".format("hi") # '    hi    '
"{0:=^10}".format("hi") # '====hi===='

#소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) #'3.4213'
