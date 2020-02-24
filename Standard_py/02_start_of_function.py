#먼저, 사전 상식으로 알고 있지만겠지만 파이썬은 들여쓰기가 굉장히 중요하다
#tab키 사용을 익숙히 하고, 세미콜론 미사용에 익숙해지길!

listdata=['a','b','c']

if 'a' in listdata:
    print('a가 listdata에 있습니다.')
    print(listdata)
else:
    print('a가 존재하지 않습니다.')

#가장 바깥의 코드는 들여쓰기가 항상 없어야 한다.
#들여쓰기 간격은 항상 같아야 한다.

#if문
'''
이제 함수에 대해서 제대로 배워보자

if문은 다음과 같은 규칙을 같는다

if 조건:
    실행코드 1
elif 조건:
    실행코드 2
else:
    실행코드 3

파이썬은 else if가 아니라 elif라는 것을 주의한다.
'''

#for문
'''
 
for 변수 in 범위:
    실행코드

범위안으로 들어가는 것들:
 - 문자열
 - 리스트나 튜플
 - 사전
 - range()
 - 그외 반복 가능한 객체

 C언어와 마찬가지로 continue문과 break문을 사용할 수 있음

'''

#for 예제
print()
#문자열
str = 'abcdef'
for c in str: #문자열 요소 수 만큼 반복
    print(c, end=' ')
print()
#리스트
list = [1,2,3,4,5]
for c in list: #리스트의 크기만큼 반복
    print(c,end=' ')
print()
#사전
ascii_codes={'a':97,'b':98,'c':99}
for c in ascii_codes:
    print(c,end=' ')
#사전의 경우 키만 출력이 된다.
print()
#range
for c in range(10):  #열번 반 복
    print(c,end=' ')
print('\n----------------------------------------')

scope=[1,2,3]
for x in scope:
    print(x)#for~else문은 break에 의해 중단이 없이 모두 정상적이게 실행되어야만
#    break   #특정코드를 실행하게 할 경우 사용된다. 이 문장의 맨 앞 주석을 지우고 실행시켜보자
else:
    print('Perfect')#for 구문이 모두 실행되었을때 실행된다.

#while~continue~break문
'''
while 조건:
    continue

    break
조건을 만족한다면 계속해서 반복(c언어와 같음)
아래는 예제
'''
print('-----------------------')
#while예제 1~n까지의 수를 모두 더해서 10만보다 커지면 멈춤
x=1
total=0
while 1:
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x=x+1

#None에 대해서
#None의 정의
'''
None은 types.NoneType의 유일한 값으로 
존재하지 않는 변수에 대해 대입하여 이 변수에 아무런 값이 없음을 알린다.
'''
#None
'''
None으로 지정된 변수에 값이 있는 임의의 자료형을 대입하여 활용할 수 있다.

대입할 자료형을 결정하지 않은 상태로 선언할 때 None을 대입하거나, 
함수에서 아무값도 리턴하지 않을 때사용하기도 함. 
함수 로직에서 예외가 발생하거나 오류가 발생하여 None을 리턴하여 종료하면
이 함수를 호출한 함수가 실행 도중 오류가 발생하여 비정상적으로 종료됨을 알 수 있다.
...라고 적혀있으니
내가 제대로 이해한 것이 맞다면
일반 프로그래밍에 있어서의 NULL과 같은 용도로 사용하면 된다는 것이다.

'''
