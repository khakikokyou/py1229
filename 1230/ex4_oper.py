# 카페에 있는 비교 연산자 코딩하기

# Boolean
# True 와 False 값만 가질 수 있음
print(True) # True
print(False) # False
print("*"*30)
# 숫자 또는 문자열에 적용
print(10 == 100) # False
print(10 != 100) # True
print(10 < 100) # True
print(10 > 100) # False
print(10 <= 100) #True
print(10 >= 100) #False



print("*"*30)
###################################3
print("김길동" == "김길동")
name = "하하"
print("김길동" != name)
print("김길동" < name)
print("김길동" > name)

hungry=True
sleepy=False
print(type(hungry)) # 자료형
print(not hungry) # 논리부정
print(hungry and sleepy) # A and B : A,B가 모두 True가 되어야 True
print(hungry or sleepy) # A and B : 둘중 하나만 True
