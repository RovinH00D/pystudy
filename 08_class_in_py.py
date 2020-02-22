class MyClass:
    def __init__(self, *args):
        self.var = "안녕하세요"
        print("MyClass 인스턴스 객체가 생성되었습니다.")
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)
obj = MyClass()
print(obj.var)
obj.sayHello()
print(obj.param2)

#class
'''
    문답무용 먼저 클래스를 선언해보았다.
    클래스 선언 방식은 다음과 같다.
    class 클래스 이름 :
        클래스 멤버 정의
        클래스 메소드 정의
    클래스 메소드는 반드시 첫번째 인자가 self여야한다.
    단, 클래스의 메소드를 호출할 때 self는 생략한다.
'''

#클래스 멤버와 인스턴스 멤버
'''
    클래스 멤버란?
    클래스 메소드 바깥에서 선언되는 변수
    인스턴스 멤버란?
    클래스 메소드안에서 self와 함께 선언되는 변수

    var는 클래스 메소드 밖에서 선언이 되었으니 클래스 멤버이다. 클래스 멤버는 아래처럼 참조가 가능하다
    self.var        <- 클래스 메소드 내에서 var를 참조할 경우
    MyClass.var     <- 클래스 밖에엇 클래스 이름만으로 참조할경우(잘안쓰임)
    obj.var         <- MyClass의 인스턴스 객체 obj에서 var를 참조할경우

    self.param2는 sayHello()내에서 선언된 인스턴스 멤버이다.
    이 변수가 초기화되는 시점은 sayHello()가 호출되는 시점이므로 param2를 오류없이 사용하려면
    11번째 줄처럼 sayHello()가 호출된 이후여야한다. 
'''

#클래스 생성자
'''
    생성자는 클래스의 인스턴스 객체가 생성될 때 자동적으로 호출되는 메소드다.
    클래스 생성자는 항상 아래같은 이름을 갖는다.
    def __init__(self, *args)
    *args는 가변인자
    클래스를 생성하면 곧바로 호출되는 메소드이기 때문에 print를 사용할경우
    클래스를 생성하자마자 출력을 하게 된다.
    만약 생성자에 self이외의 기본 인자를 기입했을 경우
    인자가 없이 객체를 생성하려고하면 오류가 발생하게 된다.
'''

#클래스 소멸자
'''
    클래스 인스턴스 객체가 메모리에서 제거될 때 
    자동적으로 호출되는 클래스 메소드가 클래스 소멸자다.
    클래스 소멸자는 클래스 내에서 아래같은 이름을 갖는다.
    def__del__(self):
    del<인스턴스 객체>
    del키워드를 통해 메모리에서 제거할 수 있다.
'''

#클래스 상속
'''
    클래스 상속은 아래처럼 받는다.
    class 자식클래스(부모클래스1, 부모클래스2,...):
    클래스를 상속받으면 부모 클래스의 메소드를 자식클래스에서 받아서 사용할 수 있다.
    ㄴ
'''