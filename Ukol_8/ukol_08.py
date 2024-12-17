import re

def check_phonenumber(phone_number):
    rx_number = re.compile(r'^(\+?\d{3})? ?\d{3} ?\d{3} ?\d{3}$')
    phone_check = rx_number.search(phone_number)
    return bool (phone_check) 

print(check_phonenumber('777777777'))
print(check_phonenumber('777 777 777'))
print(check_phonenumber('+420777777777'))
print(check_phonenumber('+420 777 777 777'))
print(check_phonenumber('608 192 292'))
print(check_phonenumber('608 192 292...'))
print(check_phonenumber('test'))
print(check_phonenumber('+420'))
print(check_phonenumber('+420 '))
print(check_phonenumber('777777777666666666666666666'))
