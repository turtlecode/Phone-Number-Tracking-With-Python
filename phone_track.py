import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumber = phonenumbers.parse("+919876543210")

Carrier = carrier.name_for_number(phoneNumber,'en')

Region = geocoder.description_for_number(phoneNumber,'en')

print(Carrier)
print(Region)