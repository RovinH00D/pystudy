#시퀀스 자료형
'''
    시퀀스 자료형이란 어던 객체가 순서를 가지고 나열되어 있는 것을 말한다.
    문자열, 리스트, 튜플이 이에 해당된다.

    인덱싱 - 인덱스를 통해 해당 값에 접근이 가능하다
    슬라이싱 - 특정 구간의 값을 취할 수 있다.
    연결 - + 연산자로 두 시퀀스 자료형을 연결하는것
    반복 - *연산자를 이용해 시퀀스를 여러번 반복하는 것
    멤버체크 - c언어처럼 for문을 이용해 검사할 필요 없이 in연산자로 요소를 확인하는 것
    크기정보 - len()연산자로 자료의 크기를 알 수 있음   
            (문자열 -> 문자의 개수, 리스트,튜플 -> 멤버의 개수)
'''

#인덱스
'''
    파이썬에서 인덱스는 거꾸로 셀 수도 있다.
    끝에서 몇번째로 시작하는 것으로 양수 인덱스는 0부터 시작하지만
    음수 인덱스는 맨 뒤를 -1로 기준하고 시작한다.
'''

#슬라이싱
'''
    슬라이싱은 시퀀스 자료에서 일정 범위에 해당하는 부분을 취하는 방법
    [시작 인덱스:끝인덱스:스텝]
    스텝은 자료를 취하는 간격을 의미하고, 디폴트 값은 1로 생략되는 경우가 많다.

    [m:n] - m이상 n미만의 요소를 슬라이싱
    [:n] - n미만의 요소 슬라이싱
    [m:] - m이상의 요소 슬라이싱
    [:-n] - 끝에서 n번째 미만인 요소를 슬라이싱
    [-m:] - 끝에서 m번재 이상인 요소를 슬라이싱
    [::o] - o간격으로 요소들을 슬라이싱
'''

#자료 반복
'''
    배웠던 개념이지만 헷갈려서 복습하기로 했다
    간단하게 시퀀스 변수명 뒤에 *n을 하면 n번 반복한다
    [1,2,3]리스트에 *5를 하면 [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]이 된다.
'''

#len()의 경우 괄호 안에 변수명을 넣으면 된다.

#멤버 체크의 경우 <값>in<변수명>형태로 사용하고, 값이 있으면 True를 없으면 False를 출력한다.

#문자열 포맷팅
'''
    이렇게 전문용어를 써서 뭔가 했지만 알고 있던 지식이었다.
    문자열을 표기하기 위한 하나의 양식으로 문자열을 만드는 것으로
    포맷팅에서 변하는 값을 나타내기 위해 사용되는 기호를 포맷 문자열이라고 한다.

    %s - 문자열 
    %c - 문자나 기호 한 개
    %f - 실수
    %d - 정수
    %% - %기호 자체 표시

    c와 다르게 포맷팅을 할 때 ,가 아닌 %를 사용한다는 것을 주의하자.
'''

txt1='자바'; txt2='파이썬'
num1=5; num2 = 10
print('나는 %s보다 %s가 더 좋다'%(txt1, txt2))
print('%d + %d = %d'%(num1,num2,num1+num2))


from time import sleep
for i in range(100):
    msg='\r진행률 %d%%'%(i+1)
    print(''*len(msg), end='')
    print(msg,end='')
    sleep(0.1)
'''
    위의 코드를 설명하겠다.
    msg를 캐리지 리턴 문자 \r을 추가하여 문자열 포맷팅을 이용해 구성하고
    print(''*len(msg),end='')로 줄바꿈 없이 *를 통해 msg의 길이만큼 공백을 만들어주고
    그 후 print(msg, end='')로 msg를 다시 출력한다. 
    캐리지 리턴은 현재 위치를 나타내는 커서를 화면 맨 앞으로 이동하라는 의미이다
'''

#이스케이프 문자
'''
    \n - 개행
    \t - 탭
    \(enter) - 다음 줄도 계속
    \\ - \표시
    \'or\" - '또는 "출력
'''
