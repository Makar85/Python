import phonenumbers
from phonenumbers import carrier
print("Введите номер телефона:")
phone_number = input()
service_provider = phonenumbers.parse(phone_number)
print(carrier.name_for_number(service_provider, 'ru'))

