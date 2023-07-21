import requests
from bs4 import BeautifulSoup

url = input("Введите ссылку на исполнителя на Яндекс.Музыке: ")
response = requests.get(url)
if response.status_code != 200:
    print("Ошибка при получении страницы")
    exit()
html = response.text
soup = BeautifulSoup(html, "html.parser")
song_list = soup.find_all("div", {"class": "d-track__name"})
if not song_list:
    print("Не удалось найти список песен")
    exit()
print(f"Топ10 песен исполнителя на Яндекс.Музыке:")
for i, song in enumerate(song_list[:10]):
    print(f"{i+1}. {song.text.strip()}")
