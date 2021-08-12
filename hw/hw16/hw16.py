from geopy.geocoders import Nominatim


# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:
#
# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322

def main():
    show_location("gps.txt")


def show_location(file):
    geolocator = Nominatim(user_agent="http")
    with open(file, "r") as f:
        for line in f:
            coordinates = line.split(";")
            location = geolocator.reverse((coordinates[0], coordinates[1]))
            print("Locarion: " + str(location))
            print("Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=" + coordinates[0] + "," +
                  coordinates[1])


if __name__ == '__main__':
    main()

# Вывод:
#
# Locarion: округ Лахта-Ольгино, Санкт-Петербург, Северо-Западный федеральный округ, 190000, Россия
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.01,30.19
#
# Locarion: Государственный универсальный магазин (ГУМ), 3, Красная площадь, Китай-город, Тверской район, Москва, Центральный федеральный округ, 109012, Россия
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=55.7536283,37.62137960067377
#
# Locarion: Администрация города Сочи, 26, Советская улица, Завокзальный, Центральный внутригородской район, Сочи, городской округ Сочи, Краснодарский край, Южный федеральный округ, 354000, Россия
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=43.5854823,39.723109
