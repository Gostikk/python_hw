
# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt


from geopy.geocoders import Nominatim
from exif import Image


with open('img.jpg', 'rb') as img_file:
    image = Image(img_file)
# print(img_file.name, image)

if image.has_exif:
    latitude_list = str(image.gps_latitude).lstrip('(').rstrip(')').split(', ')
    longitude_list = str(image.gps_longitude).lstrip('(').rstrip(')').split(', ')
    decimal_latitude = float(latitude_list[0]) + float(latitude_list[1])/60 + float(latitude_list[2])/3600
    decimal_longitude = float(longitude_list[0]) + float(longitude_list[1])/60 + float(longitude_list[2])/3600
    coords = f"{str(decimal_latitude).replace('.', ',')}\';{str(decimal_longitude).replace('.', ',')}\'"

    with open('coords.txt', 'w') as output_file:
        output_file.write(coords)

else:
     print('There is no gps in this image')


