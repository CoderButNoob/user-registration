import pytest
from faker import Faker
from loguru import logger
from user_reg import valid_name, valid_last_name, valid_email, valid_phone, valid_password

fake = Faker()
logger.add("error_only.log",level="ERROR")

positive_case = []
while len(positive_case) < 1000:
    first_name = fake.first_name()
    last_name = fake.last_name()

    if len(first_name) >= 3 and len(last_name) >= 3:
        positive_case.append({
            "first_name": first_name,
            "last_name": last_name,
            "email": fake.email(),
            "phone": f"+91 {fake.random_number(digits=10 , fix_len=True)}",
            "password": f"A{fake.random_int(min=10000, max=99999)}@a"
        })

negative_case = [{
    "first_name": fake.word().lower(),
    "last_name": fake.word().lower(),
    "email": "invalidemail.com",
    "phone": f"91-{fake.random_number(digits=10)}",
    "password": "abc1234"
}for _ in range(1000)]


@pytest.mark.parametrize("case",positive_case)
def test_positive(case):
    try:
        assert valid_name(case["first_name"]) is True
        assert valid_last_name(case["last_name"])  is True
        assert valid_email(case["email"]) == "Valid Email"
        assert valid_phone(case["phone"]) == "Valid Number"
        assert valid_password(case["password"]) == "Valid Password"
    except AssertionError as e:
        logger.error(f"[Positive Case Failed]  Case: {case}\nReason: {e}")
        raise





@pytest.mark.parametrize("case",negative_case)
def test_negative(case):
    try:
        assert valid_name(case["first_name"]) != True
        assert valid_last_name(case["last_name"]) != True
        assert valid_email(case["email"])  != "Valid Email"
        assert valid_phone(case["phone"]) != "Valid Number"
        assert valid_password(case["password"]) != "Valid Password"
    except AssertionError as e:
        logger.error(f"[Negative Case Failed]  Case: {case}\nReason: {e}")
        raise








