'''
    어느덧 파이썬의 마지막까지 왔다.
    마지막은 예외처리이다
    프로그램을 만들다 보면 오류가 나타나기 마련이다.
    그러나 프로그램을 짤 때 이러한 오류를 무시하고 싶기도 마련이다.
    이럴때 사용하는 것이 바로 예외 처리인데, 오류를 처리하고 프로그램을 계속해서 굴려준다.
'''

'''
    이런 예외 처리는 다음의 문장으로 행해지는데,
    try와 except문을 이용한다.

    try :

    except[발생 오류[as 오류 메세지 변수]]:

    위의 구문의 사용법은 3가지가 될 텐데,

    첫번째로 try와 except만 사용하는 방법이다.
    이 경우 오류의 종류에 상관없이 오류가 나면 무조건적으로 except를 실행한다.

    두번째로 발생오류만 포함경우이다.
    except 발생오류 :
    를 적으면 실제 발생한 오류와 이름이 같을 때 except문을 작동시킨다.

    세번째로 오류 메세지 변수까지 포함시킨 except문이다.
    except 발생 오류 as 오류 메세지 변수
    이 경우 두 번째 경우에서 오류 메세지의 내용까지 알고싶을 때 사용하는 방법이다.
    보통 print(오류 메세지 변수)로 사용한다.
'''

'''
    이외에 예외 처리에서 사용하는 구문이 무엇이 있는지 살펴보자

    첫번째로 else문이다. else절은 예외가 발생하지 않은경우 실행이 되며,
    except절 바로 다음에 위치해야한다.

    두번째로 finally이다.
    finally문은 오류 발생 여부의 상관없이 실행한다.
'''

'''
    else문에서도 눈치를 챘겠지만, except문은 if문과 비슷하게도 여러개를 설정이 가능하다.
    except를 여러개 사용하여 여러개의 오류를 처리가 가능하다.

    try:
        a = [1,2]
        print(a[3])
        4/0
    except (ZeroDivisionError, IndexError) as e:
        print(e)

    위처럼 괄호로 묶어서 한번에 2개 이상의 오류를 처리할 수도 있다.
'''

'''
    오류가 발생했을 때 회피를 해야하는 경우가 생길 수 있는데,
    그 경우 except문에서 pass를 사용하면 된다.
'''

'''
    오류를 일부러 발생시킬수도 있다!
    파이썬은 raise문을 이용하여 오류를 사용자가 임의로 발생시킬 수 있다.
    다음 예제를 보자.

    class Bird :
        def fly(self) :
            raise NotImplementedError

    class Eagle(Bird) :
        pass

    eagle = Eagle()
    eagle.fly()

    위와 같은 경우 Bird를 상속받은 Eagle이 fly함수를 재구성하지 않았으므로 오류가 난다.
    막간의 상식으로 알자면,
    상속받은 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩이라고 부른다
'''

'''
    프로그램 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 오류를 만들어야 할 때도 있다.
    직접 오류를 만들어보자
    먼저, 오류를 만들기 위한 기초 클래스부터 만든다.
    여기서 오류는 아래처럼 파이썬 내장 클래스인Exception을 상속해 만들 수 있다.

    class MyError(Exception) :
        pass

    예제를 만들기 위해서 별명을 출력하는 함수를 만들어보자

    def say_nick(nick) :
        if nick == '바보' :
            raise MyError()
        print(nick)

    그리고 다음처럼 say_nick을 호출해보자!

    say_nick("천사")
    say_nick("바보")

    실행해보면 천사가 한 번 실행되고 MyError가 뜬다

    예외처리하는 법을 배웠으니 한번 해보자

    try :
        say_nick("천사")
        say_nick("바보")
    except MyError:
        print("허용되지 않는 별명입니다.")

    위처럼 try, except를 추가하면 된다.
    여기서 오류메세지를 띄워보는 방법도 취해보는 것도 좋다고 생각하는데,
    아마 현재 저기서

    except MyError as e:
        print(e)

    를 추가해서 실행해보면 아무것도 출력이 되지 않음을 알 수 있다.

    오류 메세지 출력에 필요한 메서드를 만들지 않았기 때문인데,
    오류 클래스는 아래 예제와 같이 __str__메서드를 구현해야한다.

    class MyError(Exception):
        def __str__(self):
            return "허용되지 않는 별명입니다."

    이것을 실행시키면 return문이 실행되는 것을 알 수 있을 것이다.
    만약 에러 발생시점에 오류메세지를 전달하고 싶다면 아래 예제와 같이 수정해야한다.

    class MyError(Exception):
        def __init__(self, msg) :
            self.msg = msg
        def __str__(self) :
            return self.msg


    def say_nick(nick) :
        if nick "바보":
            raise MyError("허용되지 않은 별명입니다.")
        print(nick)

    try :
        say_nick("천사")
        say_nick("바보")
    except MyError as e :
        print(e)


    결국 최종적으로 위와 같은 코드가 나온다.
'''
