'''
    for의 특징 -> 유용하고 구조가 한 눈에 들어옴
    for의 기본 구조

    for 변수 in 리스트 (또는 투플, 문자열, 리스트)

    for 변수 in 리스트(혹은 튜플이나 문자열)
        수행할 문장1
        수행할 문장2
        ...

    ex)
    1.
        test_list = ['one','two','three']
        for i in test_list :
            print(i)

    2.
        a = [(1,2),(3,4),(5,6)]
        for (first, last) in a:
            print(first+last)

    3.
        marks = [90, 25, 67, 45, 80]
        number = 0

        for mark in marks :
            number = number + 1
            if mark >= 60:
                print("%d번 학생은 합격입니다." % number)
            else :
                print("%d번 학생은 불합격입니다." % number)

    C언어와 마찬가지로 continue를 사용이 가능하다


    range란?
    for문의 숫자 리스트를 자동으로 만들어주는 간편한 함수이다.
    range(0,10) -> 0부터 10미만의 숫자를 포함하는 range객체를 만들어 준다.
    쉽게 말해 range(시작숫자, 끝숫자)

    len 함수는 리스트 내 요소의 개수를 돌려주는 함수이다

    입력인수 end를 통해 결과값을 출력할 때
    다음줄로 넘기지 않고 원하는 바로 끝을 내고 싶을 때 사용이 가능하다
    ex)
        end = " "

    특히 for문은 리스트 내에 추가시킬 수 있다.
    ex)
        a = [1,2,3,4]
        result = [num*3 for num in a]
        result # [3,6,9,12]
    또한 if문을 포함 시킬 수도 있다.
    ex)
        result = [num*3 for num in a if num % 2 == 0]
        print(result) # [6, 12]

    리스트 내에 두개의 for문을 이용할 수도 있다.
    ex)
        result = [x*y for x in range(2,10)
                        for y in range(1,10)]
        print(result) # [2,4,6,8,10,....63,72,81]

'''
