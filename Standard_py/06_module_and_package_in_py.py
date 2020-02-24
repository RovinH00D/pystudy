#module
'''
    남이 만들어두거나, 파이썬에 미리 존재하는 C의 헤더파일이라고 생각하면 될 것 같다.
    맛보기를 위해서 이 책에서 소개하는 코드를 한 번 테스트 해보겠다.
'''

import time
print('5초간 프로그램을 정지합니다.')
time.sleep(5)
print('5초가 지났습니다. 프로그램이 종료됩니다.')
print("="*20)

import mylib
ret1 = mylib.add_txt('life is short','you need python')
ret2 = mylib.reverse(1,2,3)
print(ret1); print(ret2)
print("="*20)

#package
'''
    파이썬 모듈들을 계층적인 디렉토리 형태로 구성한 것을 파이썬 패키지라고 한다.
    패키지안에는 __init__.py라는 이름의 파일이 있어야한다.
    __init__.py는 version = 1.0같이 한줄짜리 텍스트면 충분하다.
'''

#패키지및 모듈 임포트 하는 법들
'''
    패키지나 모듈을 import하는 법이 여러가지 있어서 따로 분류했다.
    먼저 간단하게 import하는 법이 있고, 그 다음으로는
    from ~import하는 법이 있다.

    이 경우 from(패키지/모듈)import(모듈/함수)을 통해
    패키지의 경우 해당 모듈만, 모듈의 경우 해당 함수만 import하는 것이 가능하다.
    또,import~as가 존재한다. 이름이 길거나, 계층 구조가 복잡한 경우
    
    import 이름이 긴 모듈명 as 별명

    을 통해서 축약해서 쉽게 쉽게 호출할 수 있다.
'''
