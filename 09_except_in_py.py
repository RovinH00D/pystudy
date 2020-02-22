# try~except
'''
    try:
        코드
    except:
        예외처리 코드
    try문에서 에러가 생기면 except로 이동해서 코드를 적절히 처리해준다.
'''

#try~except~else
'''
    try:
        코드
    except:
        코드
    else:
        코드
    어떤 코드를 수행했을 때 try문에서 오류가 생기지 않았다면 
    except부분은 실행되지 않고 else부분이 실행된다.
'''

#try~except~finally
'''
    try:
        코드
    except:
        코드
    finally:
        코드
    어떤 코드를 실행했을 때 오류가 나건 말건 finally문 이하의 코드들은 무조건적으로 실행이 된다.
'''

#try~except Exception as e
'''
    try:
        코드
    except Exception as e:
        코드
    파이썬은 발생 가능 예외에 대해서 정의가 되어있는데 try문에서 어떤 문제가 발생하였는지 출력을 해준다.
'''

#try~except 특정 예외
'''
    try:
        코드
    except 특정 예외:
        코드
    특정한 에외가 발생되었을 때 그 오류에 대해서 어떻게 처리해줄지 
    개발자가 지정이 가능도록 해주는 문법이다.

'''