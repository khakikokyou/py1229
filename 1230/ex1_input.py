# ex1_input
comm = """
input() 명령어 프롬프트에서 사용자로부터 데이터를 입력 받을 때 사용한다.
java => Scanner, BufferedReader

"""
# (input("메세지를 입력하세요!")  :  sc.nextLine()
# print(type(input("메세지를 입력하세요!")))

# msg = input("메세지를 입력하세요!")
# print(msg)

# int() 로 숫자로 변경
# number = int(input("숫자를 입력 : "))
# number = number + 10
# print(number)


# 연습 문제
# 두수를 입력을 받아서 사칙연산의 결과를 출력하시오
# 단! 입력값은 실수로 받아서 연산하시오
number1 = float(input("숫자를 입력하세요!"))
number2 = float(input("숫자를 입력하세요!"))
덧셈 = number1 + number2
print("덧셈결과 : " , 덧셈)
뺄셈 = number1 - number2
print("뺄셈결과 : " , 뺄셈)
곱셈 = number1 * number2
print("곱셈결과 : " , 곱셈)
나눗셈 = number1 / number2
print("나눗셈결과 : " , 나눗셈)
