import re


def is_valid_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'
    return bool(re.match(pattern, password))


text = "1256"
# print(char_frequency(text))
print(is_valid_password(text) is False)
text = "1A345*78"
print(is_valid_password(text) is True)
text = "ADFCTYUI"
print(is_valid_password(text) is False)
