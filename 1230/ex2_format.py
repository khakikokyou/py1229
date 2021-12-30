comm = """
print("doc", num)
print("doc {}". format(num))
format()  함수로 숫자를 문자열로 변환 
중괄호 포함한 문자열 뒤에 마침표 찍고 format() 함수 사용하되,
중괄로 개수와 format 함수 안 매개변수의 개수는 반드시 같아야 함. 오류는 나지 않지만 왠만하면 지켜서 사용하자!
문자열의 중괄호 기호가 format() 함수 괄호 안의 매개변수로 차례대로 대치되면서 숫자가 문자열이 됨


string_a = "{}".format(100)
print(string_a)
print(type(string_a))


format_a = "kosmo{}기".format(100)
format_b = "파이썬 및 스트링 개발자의 연봉은 {} 입니다".format(5000)
format_c = "{} / {} / {}".format(3000,5000,7000)
format_d = "{} / {} / {}".format(1, "파이썬", True)
print("format_a =>", format_a)
print("format_b =>", format_b)
print("format_c =>", format_c)
print("format_d =>", format_d)
"""
# 이럴때는 해당 인덱스만 출력을 한다.
# 파이썬은 인덱스가 0부터 시작이기 때문에 {}안에 아무 숫자도 입력되어 있지 않으면 1,2 가 출력이 된다
# 인덱스 번호를 넣고 출력하면 그인덱스번호에 맞는 숫자가 출력된다.
print("{2}, {3}".format(1,2,3,4,5))
print("*"*30)

# 정수 - d(정수표기법) (중)
# 실수 - :f
intNum = 100
output_a = "{:d}".format(intNum)

print(output_a)
print(type(output_a))

# 특정 칸에 출력하기
output_b = "{}".format(intNum)
output_b = "{:5d}".format(intNum) # 5칸
output_c = "{:10d}".format(intNum) # 10칸
print(len(output_b))
print(len(output_b))
print(len(output_c))

#  빈칸을 0으로 채우기
outout_d = "{:05d}".format(52)
outout_e = "{:05d}".format(-52) # 부호도 자리수를 차지 한다. *****
print(outout_d)
print(outout_e)
# <결과>
"""
00052
-0052 #부호도 자리수를 차지 한다.
"""

# 기호와 함께 출력하기
# {:+id} 앞에 + 기호를 추가하면 양수의 경우 + 붙여줌
outout_f = "{:+d}".format(52) # 양수
outout_g = "{:+d}".format(-52) # 음수

print(outout_f)
print(outout_g)

# {: d}앞에 공백을 두면 양수일 경우 기호 위치를 생략
outout_h = "{: d}".format(52) # 양수, 기호 생략
outout_i = "{: d}".format(-52) # 음수

print(outout_h)
print(outout_i)


# 자리수 만큼을 기호 뒤로 밀기
outout_a = "{:+5d}".format(52) # 양수, 기호 생략
outout_b = "{:+5d}".format(-52) # 음수

print(outout_a)
print(outout_b)

# 자리수 만큼 기호를 앞으로 밀기
outout_c = "{:=+5d}".format(52) # 기호를 앞으로 밀기 : 양수
outout_d = "{:=+5d}".format(-52) # 기호를 앞으로 밀기 : 음수
print(outout_c)
print(outout_d)

# 0 채우기 => 52 => 00052
output_e = "{:=+05d}".format(52) # 0으로 채우기 : 양수
output_f = "{:=+05d}".format(-52) # 0으로 채우기 : 음수
print(output_e)
print(output_f)

print("*"*30)
# 한번 해보기 위의 코드를 다음과 같이 나오도록 하시오.
"""
 0052
-0052
"""
print("*"*30)
output_g = "{: 05d}".format(52) # 0으로 채우기 : 양수
output_h = "{: 05d}".format(-52) # 0으로 채우기 : 음수
print(output_g)
print(output_h)
print("*"*30)
# 주석 달면서 실행 결과를 알아 보기
output_a="{:15.3f}".format(52.273)
output_b="{:15.2f}".format(52.273)
output_c="{:15.1f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)
print("*"*30)
# 의미없는 소수점 제거 하기
output_a = 52.0
output_b="{:g}".format(output_a)
print(output_a)
print(output_b)





