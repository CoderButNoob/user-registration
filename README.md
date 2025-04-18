
# User Registration Validation System

This project is a Python-based User Registration Validation System that validates user inputs such as first name, last name, email, phone number, and password using regular expressions. It includes automated testing using `pytest`, with synthetic test data generated via `Faker`.




## Features
1. Validates:

    -> First and Last Names (Starts with uppercase, min 3 characters)

    -> Email (Standard formats)

    -> Phone Number (`+91 1234567890` format)

2. Password (Exactly 8 characters, at least 1 uppercase, 1 digit, and exactly 1 special character)

3. Generates 1000+ positive and negative test cases

4. Logs failed test cases using `loguru`

5. Test automation with `pytest`




## Project Structure
`├── user_reg.py `

`├── test_user_reg.py`

`├── error_only.log `


`└── README.md`
## Getting Started 

## 1. Clone the Repository

```bash
  git clone https://github.com/your-username/user-registration-validation.git
cd user-registration-validation

```
## 2. Create a Virtual Environment (optional but recommended)

```bash
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 3. Install Dependencies

```bash
  pip install pytest faker loguru

```

## 4. Run the Program

```bash
  python user_reg.py
```
You’ll be prompted to enter your name, email, phone, and password for validation.
## 5. Run the Tests

```bash
  pytest test_user_reg.py
```
Failed test cases (if any) will be logged in `error_only.log`.





    
## Validation Rules
### 1. First & Last Name
- Must start with a capital letter  
- Minimum of 3 characters  

### 2. Email
- Standard email format  
- Optional subdomains supported  

### 3. Phone
- Format: `+91 1234567890`

### 4. Password
- Exactly 8 characters  
- At least 1 uppercase letter  
- At least 1 number  
- Exactly 1 special character from `!@#$%^&*()-+`
