import re
# p = re.compile(r"([a-z]+[A-Z]+[0-9]+)")
print("설정할 비밀번호를 입력해주세요.")
password = input()

def checkio(data: str) -> bool:
    match = re.match("(?=.*\d[a-zA-Z])", data)
    # match = re.match("[A-Z]+", data)
    # match = re.match("[0-9]+", data)
    if (len(password) < 10):
        print("FALSE")
        return False
    elif match:
        print("true")
        return True
    else:
        print("false")
        return False

checkio(password)
