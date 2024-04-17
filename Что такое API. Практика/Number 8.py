import requests
import folium


def check_map(data_lat, data_lon, data_city):  # генерим карту
    world_map = folium.Map(location=[data_lon, data_lat], zoom_start=4)  # создаем объект - эту карту, ставим локацию
    folium.Marker(location=[data_lat, data_lon], popup=data_city).add_to(world_map)  # ставим метку на карте с этим IP
    world_map.save('adress.html')  # сохраняем нашу карту в формате HTML


def show_adress(ip):
    url = f'http://ip-api.com/json/{ip}'  # читаем DOC
    response = requests.get(url)
    try:
        if response.status_code == 200:
            data = response.json()  # извлекаем только нужные для нас данные с полученного JSON
            data_lon = data['lon']
            data_lat = data['lat']
            data_city = data['city']
            check_map(data_lat, data_lon, data_city)
        else:
            print(f'Обратный ответ не последовал. Статус код операции: {response.status_code}')
    except requests.exceptions.RequestException as g:
        print(f'Соединение с сайтом не было установлено. Ошибка: {g}')


ip = input()  # 115.41.218.39
print(show_adress(ip))

