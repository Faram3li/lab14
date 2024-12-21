import requests
from bs4 import BeautifulSoup

def get_scholar_links(profile_url):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if 'scholar.google.com' in href:
            links.append(href)
    return links

def save_links_to_file(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')

profile_url = input("Введіть URL профілю в Google Scholar: ")

links = get_scholar_links(profile_url)

filename = 'links.txt'
save_links_to_file(links, filename)

print(f"Посилання збережені у файл {filename}.")
