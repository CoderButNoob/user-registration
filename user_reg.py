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
    #validates all emailsamples
    
    email_pattern = r"^[\w]+(\.[\w]+)?@[\w]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,}])?$"

    if re.match(email_pattern,email):
        return  "Valid Email"
    else:
        return "Invalid Email"

def valid_phone(phone):
    phone_pattern = r"^(\+91)\s[0-9]{10}$"
    if re.match(phone_pattern,phone):
        return "Valid Number"
    else:
        return "Number is Invalid pls check"

def valid_password(password):
    # Rule 1 :- Min 8 chars
    # Rule 2 :- Atleast 1 upper case
    # Rule 3 :- Atleast 1 numeric number in password
    # Rule 4 :- Exactly 1 Charecter
    password_pattern = r"^(?=.*[A_Z])(?=.*\d).{8}$"
    special_chars = r'!@#$%^&*()-+'
    
    
    special_count = sum(1 for ch in password if ch in special_chars)
    
    if re.match(password_pattern, password) and special_count == 1:
        return "Valid Password"
    else:
        return "Invalid Password"


first_name = input("Enter Fisrst Name : ")
last_name = input("Enter Last Name : ")
email = input("Enter Email : ")
phone = input("ENter phone number in format +91 1234567891 : ")
password = input("Enter Password : ")



print(valid_last_name(last_name))
print(valid_name (first_name))
print(valid_email(email))
print(valid_phone(phone))
print(valid_password(password))