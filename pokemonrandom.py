from bs4 import BeautifulSoup
import requests
import webbrowser
import random

url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
http = requests.get(url)

soup = BeautifulSoup(http.content, "lxml")

links = soup.find_all('a', limit=4000)
links_length = len(links)

string_links = []  # list of all links in string form
Pokémon = []  # list of all links containing (Pokémon)
full_list = []  # list of the links without duplicates
link_ends = []  # list of link ends to be added

for a in range(links_length):
    string_links.append(str(links[a]))  # adds links to string_links
    if '(Pokémon)' in string_links[a]:
        Pokémon.append(string_links[a])  # add pokemon links to a list

[full_list.append(x) for x in Pokémon if x not in full_list]  # removes duplicates

for a in range(len(full_list)):  # adds link ends
    txt = full_list[a]
    x = txt.split('"')
    link_ends.append(x[1])

r = random.randrange(0, 898)
webbrowser.open('https://bulbapedia.bulbagarden.net' + link_ends[r])

pokemoncounter = soup.find_all('Pokémon')
counterLength = len(pokemoncounter)
print(counterLength)
element = (links[202])

allhits = soup.find_all(title='Bulbasaur (Pokémon)')
print(allhits)
