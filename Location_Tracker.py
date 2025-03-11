import phonenumbers
#from myNumber import number
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from phonenumbers import  geocoder

number = input ('+49 17636397193 : ')
Key = 'd250b366a89649fda9b115b2cf2d1643'
karim_Number = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(karim_Number, "en")
print(yourLocation)
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
result = geocoder.geocode(query)
#print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)
