import re

def valid_name(name):
    if re.match(r"^[A-Z][a-z]{2,}$",name):
        return True
    else:
        return "Inavlid : Name Should be min 3 chars "

def valid_last_name(last_name):
    if re.match(r"^[A-Z][a-z]{2,}$",last_name):
        return True
    else:
        return "Inavlid : Name Should be min 3 chars "
    
def valid_email(email):
    email_pattern = r"^[\w]+(\.[\w]+)?@[\w]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,}])?$"

    if re.match(email_pattern,email):
        return  "Valid Email"
    else:
        return "Invalid Email"


first_name = input("Enter Fisrst Name : ")
last_name = input("Enter Last Name : ")
email = input("Enter Email : ")


print(valid_last_name(last_name))
print(valid_name (first_name))
print(valid_email(email))
