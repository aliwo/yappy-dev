import re
# p = re.compile(r"([a-z]+[A-Z]+[0-9]+)")

print("설정할 비밀번호를 입력해주세요.")
password = input()

match = re.match("[a-z]+\[A-Z]+\[0-9]+",password)

if(len(password) < 10) :
    print("false")
elif match :
    print(match)
else :
    print(match)