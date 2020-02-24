'''
    패키지는 도트(.)을 이용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다.
    예를들어 모둘명이 A.B인경우 A가 패키지이고, B가 모듈이 된다.
'''

'''
    패키지 안의 함수 실행하는 방법으로는 import를 사용하는 것이다.
    A.B.C...를 통해 패키지의 모듈을 가져올 수 있다.

    패키지를 실행하는 방법으로는 다음 세가지가 있다

    import package.direc.module

    from package.direc import echo

    from package.direc.echo import echo_test
'''

'''
    __init__.py란, 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
    파이썬 3.3부터는 이 파일이 없어도 패키지로 인식되지만, 하위버전 호환을 위해서 작성하는 것이 좋다
'''

'''
    all의 용도를 알아보자.
    from game.sound import *의 경우 모든 것을 import하였으므로 echo모듈을 사용할 수 있어야 할 것 같아 보이지만,
    이름이 정의되지 않았다고 한다.

    이렇게 특정 디렉터리의 모듈을 *을 이용하여 import할 때는 다음과 같이 해당 디렉터리의
    __init__.py 파일에 __all__이라는 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.
'''

'''
    relative패키지
    만약 A 디렉터리의 AM모듈이 B디렉토리의 BM모듈을 사용하고 싶다면
    AM모듈에 다음과 같이 써넣으면 된다.

    from U.B.BM import BM_func

    위처럼 최상의 경로부터 전부 적어 import할 수도 있지만, 다음과 같이 import할 수도 있다.

    from ..B.BM import BM_func

    A와 B의 디렉터리의 깊이가 같을 때 부모디렉터리(..)을  이용하여 import가 가능한 것이다.

    .. -> 부모 디렉터리
    . -> 현재 디렉터리

    이러한 relative한 접근은 모듈내에서만 사용해한다.(인터프리터에서 사용하면 system에러가 난다.)
'''
