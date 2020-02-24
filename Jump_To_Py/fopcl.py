'''
    이번에는 C언어에서 배운 파일 입출력을 해보자.
    기본적인 방법은 비슷하다.
    먼저 파이썬의 파일 모드는 다음 세가지이다.
    r,w,a
    C언어를 배웠기에 알지만, 다시 집고 넘어가자면
    r은 파일 읽기 모드
    w는 파일 쓰기 모드
    a는 파일 이어 쓰기 모드

    특정좌표에 파일을 저장하고 싶다면
    f = open("C:/python/새파일.txt", "w")
    와 같은 방식으로 파일을 열어주면 된다.
    파일을 닫는 방법은 f.close()이다.

    다른 기능은 C언어와 그다지 다를 것이 없다.
'''

'''
    이번에는 파일입출력에서만 사용되는 특별한 함수들을 알아보자

    먼저 readline()이라는 함수이다.
    자신이 오픈한 파일의 맨 첫줄을 읽어오는 함수이다.
    이 함수를 이용하여 파일의 모든 데이터를 받아오고 싶다면 다음과 같은 방법을 취하면 된다.
    while True :
        line = f.readline()
        if not line : break
        print(line)
    C언어에서도 했듯이 그저 반복문을 돌리는 것이다.

    두번째 함수는 readlines()라는 함수이다.
    함수의 모든 라인을 읽어 리스트로 리턴하는 함수이다.
    lines = f.readlines()
    for line in lines :
        print(line)
    의 모습으로 위의 readline()의 예제와 같은 모습의 출력값을 얻을 수 있다.

    세번째 함수는 read()함수이다.
    파일전체의 내용을 문자열로 리턴한다.
'''

'''
    이번에는 파일을 이어 쓰는 방법이다.
    위에서도 언급했고, C언어에서도 배웠듯 파일을 추가적으로 이어쓰는 방법은
    파일오픈 방식을 a로 설정하는 것이다.
    다음 코드를 실행시키면 이미 있던 파일에 다른 문장을 이어 써넣을 수 있을 것이다.
    f = open("test.txt","a")
    for i in range(11,20):
        data = "%d번째줄입니다.\n"% i
        f.write(data)
    f.close()
'''

'''
    with문과 같이 사용하는 방법이 있다.
    with문은 다음과 같은 방법으로 사용한다.
    with open("foo.txt","w") as f :
        f.write("Life is too short, you need python")

    with문을 이용하면 with 블록에서 벗어나는 순간 파일인 f가 자동으로 닫힌다.
'''

'''
    sys모듈
    도스창에서 type명령어는 바로 뒤에 적힌 파일의 이름을 인수로 받아 그 내용을 출력해주는 명령어이다.
    대부분의 도스 명령어는 다음과 같이 도스창에서 입력인수를 직접 주어 프로그램을 실행시킨다.
    이러한 기능은 파이썬 프로그램에서도 정용시킬 수 있는데,
    sys라는 모듈을 이용하여 입력 인수를 직접 줄 수 있다.
    sys모듈을 이용하는 방법은
    import sys
    라고 입력을 하면 된다.

    import sys
    args = sys.argv[1:]
    for i in args :
        print(i)

    위의 입력 에시는 입력받은 인수들을 for문을 이용하여 차례대로 하나씩 출력하는 예인데
    sys모듈의 argv는 명령창에서 입력한 인수들을 의미한다.
    즉, sys1.py aaa bbb ccc라고 입력을 했다면
    argv[0]은 파일 이름인 sys1.py가 되고 argv[1]부터 뒤에 따라오는 인수들이 차례로 argv가 된다.

    아래의 예문을 보자
    import sys
    args = sys.argv[1:]
    for i in args :
        print(i.upper(), end=' ')
    문자열 관련 함수인 upper를 이용하여 명령 행에 입력된 소문자를 대문자로 바꾸어 주는 간단한 프로그램이다.
    만약 네가 도스창에 다음과 같이 입력을 했다고 하자
    sys2.py life is to short, you need python
    그렇다면 결과는 다음과 같다.
    LIFE IS TO SHORT, YOU NEED PYTHON
'''
