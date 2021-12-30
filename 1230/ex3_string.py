#교재참고 : 158 ~ 173p
# upper() => 대문자로 변경, lower() => 소문자
a = "Hello Python Test...!"
print(a.upper())
print(a.lower())

msg  = """
여러줄
여러줄
여러줄
여러줄
여러줄
여러줄
"""
print(len(msg))

msg  = """\
여러줄
여러줄
여러줄
여러줄
여러줄
여러줄\
"""
print(len(msg))

# strip() : 문자열의 좌우 공백을 제거한다.
msg2  = """
여러줄
여러줄
여러줄
여러줄
여러줄
여러줄
"""
print(len(msg2.strip()))

print("*"*30)
# lstrip() : 왼쪽의 공백을 제거
msg2  = """
여러줄
여러줄
여러줄
여러줄
여러줄
여러줄
"""
print(len(msg2.lstrip()))

print("*"*30)
# rstrip() : 오른쪽의 공백을 제거
msg2  = """
여러줄  
여러줄
여러줄
여러줄
여러줄
여러줄
"""
print(len(msg2.rstrip()))
"""
문자열이 소문자로만, 알파벡으로만, 혹은 숫자로만 구성되어 있는지 확인 
"""
# 알파벳 또는 숫자로 구성되어 있으면 true(나중에 조건문에 사용하기 좋음)
# 카페에 함수 목록 지금 하나씩 이런식으로 테스트 해보기
# 공백이 들어가면 false
print("하하하".isalnum())      # True
print("이즈 알파".isalpha())    # 공백이 들어가면 false

print("*"*30)

# 숫자 확인하기
ex1 = "010-1111-1111"
ex2 = "123"
ex3 = "test3"
print(ex1.isdigit())    #False
print(ex2.isdigit())    #True
print(ex3.isdigit())    #False

# find()/ index() *****
# 첫번째 index를 반환, 해당 단어를 찾지 못하면 -1 로 반환
# java -> String : indexOf()
# index()
# 첫번째 index를 반환, 해당 단어를 찾지 못하면 error 반환

msg = "안녕하세요 안녕kosmo100기".find("안녕")
print(msg)

msg = "안녕하세요 안녕kosmo100기".index("안녕")
print(msg)

# 뒤에서 부터 해당 단어를 찾음
print("*"*30)
msg = "안녕하세요 안녕kosmo100기".rfind("안녕")
print(msg)

msg = "안녕하세요 안녕kosmo100기".rindex("안녕")
print(msg)

# In 연산자
# - 문자열 내부에 어떤 문자열이 있는지 확인 할 때 사용함
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")

# split() 함수
# 문자열 특정한 문자로 잘라서 list로 반환한다.
msg = "10 20 30 40 50"
print(type(msg.strip()))
msg = "10 20 30 40 50"
print(type(msg.strip("/")))


