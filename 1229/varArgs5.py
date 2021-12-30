import sys
import os
# ls 명령어랑 동일한가
# print(os.listdir())
# 인덱스의 값만큼 터미널에 데이터를 넣어주면 오류없이 배열대로 출력된다.
# 터미널 명령문 : python3 varAras5.py hello kosmo100 heeju - hello 뒤부터의 문자열이 나온다.
print("*"*10)
print(sys.argv)
print(type(sys.argv))
# Jar, Wars
print("FileName : ", sys.argv[0])
print("Arg1 : ", sys.argv[1])
print("Arg2 : ", sys.argv[2])
print("Arg3 : ", sys.argv[3])

