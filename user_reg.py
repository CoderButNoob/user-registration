import re

def valid_name(name):
    if re.match(r"^[A-Z][a-z]{2,}$",name):
        return True
    else:
        return "Inavlid : Name Should be min 3 chars "

name = input()
print(valid_name (name))