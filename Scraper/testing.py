import requests
from bs4 import BeautifulSoup

dd_url = 'https://www.audible.com/pd/Christmas-Days-Audiobook/B01MYWUQSR?ref=a_hp_c10_dd&pf_rd_p=31214b22-ae7c-4e9b-a860-653137f1abe8&pf_rd_r=9YTFFFC12J8Q7E89NFFQ'
dd_source = requests.get(dd_url).text

daily_soup = BeautifulSoup(dd_source, 'lxml')

for data in daily_soup.find_all('div', id='center-1'):
    # genre
    fd_genre = data.find('nav').a
    genre = fd_genre.text
    genre2 = fd_genre.find_next('a').text
    print(genre)
    print(genre2)

    # Title, author
    title = data.find('li', class_='bc-list-item').h1.text
    print(title)

    author = data.find('li', class_='authorLabel').a.text
    print(author)

    # Price
    price = data.find('div', class_='adblBuyBoxPrice').p.span.span.text
    print(price)
