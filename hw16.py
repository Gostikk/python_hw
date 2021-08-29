# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:

# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322


from geopy.geocoders import Nominatim


with open('coords.txt', 'r') as cf:
    coords_lines = cf.readline()
coords = [line.rstrip("'") for line in coords_lines.split(';')]
coords = [line.replace(',','.') for line in coords]

gloc = Nominatim(user_agent='myapp')
location = gloc.reverse(coords)

print('Location:', location.address)
print('Google Maps URL: ', 'ref= ', f'https://www.google.com/maps/search/?api=1&query={coords[0]},{coords[1]}')
