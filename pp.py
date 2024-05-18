import requests
from bs4 import BeautifulSoup
import fake_useragent
import data
ref = data.ref
def parser(ref):
    header = {'user-agent': fake_useragent.UserAgent().random}

    response = requests.get(ref, headers=header).text
    soup = BeautifulSoup(response, 'lxml')

    blocks = soup.find_all('div', {'direction': 'ltr'})

    coin = {}

    for i in blocks:
        link = i.find_next('a', {'data-bn-type': 'link'})
        name = link.find_next('div', {'class': 'body3 line-clamp-1 truncate text-t-third css-vurnku'})
        price = i.find_next('div', {'class': 'body2 items-center css-18yakpx'})
        link = 'https://www.binance.com' + link.get('href')
        name = name.text
        price = price.text
        coin[name] = price, link

    return coin

print(parser(ref))