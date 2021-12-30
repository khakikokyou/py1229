# 안녕하세요

comm = """"
문자 선택 연산자 (인덱싱) : []
index : 0 부터 시작 *****
"""

print("문자 선택 인덱싱")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
# print("안녕하세요"[5]) IndexError: string index out of range 문자열의 인덱스 번호가 4까지만 있기 때문에 5까지 하면 오류!
print("*"*30)

"""
역 index : -1 부터 시작 *****
"""
print("문자 선택 역인덱싱")
print("안녕하세요"[-0])
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

print("*"*30)
"""
문자열 범위 선택 연산자(슬라이싱) : [:]
- 특정 범위 선택
- 마지막 숫자에서 -1
"""
print("안녕하세요"[1:4])
print("안녕하세요"[2:3])
print("*"*30)

# 뒤에 값을 생략, 앞의 값을 생략
print("안녕하세요"[2:])
print("안녕하세요"[:2])

# 정리 ) 인덱싱, 슬라이싱
hello = "안녕하세요"
print(type(hello))
# 인덱싱, 슬라이싱
print(hello[:2])