print("장희주")
# 다음 문자열에서 ♡ 를 찾아서 다음과 같이 나오도록 출력하시오.

str = "Lobby news about the Hobby Lobby lawsuit. ♡ Get the latest releases, statements, and articles ♡ about Hobby Lobby and their fight for religious freedom."
lastIdx = str.rfind("♡")

answer = str[lastIdx + 2:]
print(answer)
print(len(answer))




