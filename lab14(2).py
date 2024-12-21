import requests
import os

def download_random_images(theme, count, folder):
    url = f"https://source.unsplash.com/random/800x600/?{theme}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i in range(count):
        response = requests.get(url)
        with open(os.path.join(folder, f"{theme}_{i+1}.jpg"), 'wb') as file:
            file.write(response.content)
        print(f"Зображення {i+1} збережено у {folder}")

theme = "database"
count = 10
folder = 'random_images'

download_random_images(theme, count, folder)

print(f"{count} зображень на тему '{theme}' збережено у папці {folder}.")
