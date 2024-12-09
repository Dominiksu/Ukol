import re

def check_phonenumber(phone_number):
    rx_number = re.compile(r'^\+?[\d\s]+$')
    phone_check = rx_number.search(phone_number)
    return bool (phone_check)

print(check_phonenumber('+ 444433555'))
