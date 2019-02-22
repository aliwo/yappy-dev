import re

digit = re.compile("[0-9]+")
uppercase_letter = re.compile("[A-Z]+")
lowercase_letter = re.compile("[a-z]+")

def checkio(data: str) -> bool:

    if(len(data) < 10):
        return False
    if(digit.search(data) == None):
        return False
    if(uppercase_letter.search(data) == None):
        return False
    if(lowercase_letter.search(data) == None):
        return False

    return True

print(checkio('A1213pokl'))
print(checkio('bAse730onE'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))