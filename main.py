import requests
from bs4 import BeautifulSoup
import lxml
import random
url1 ='https://allo.ua/ua/products/notebooks/'
url2 = "https://allo.ua/ua/products/notebooks/p-2/"
url3 = "https://allo.ua/ua/products/notebooks/p-3/"
url4 = "https://allo.ua/ua/products/notebooks/p-4/"
url5 = "https://allo.ua/ua/products/notebooks/p-5/"
url6 = "https://allo.ua/ua/products/notebooks/p-6/"
url7 = "https://allo.ua/ua/products/notebooks/p-7/"
url8 =  "https://allo.ua/ua/products/notebooks/p-8/"
url9 = "https://allo.ua/ua/products/notebooks/p-9/"
url10 = "https://allo.ua/ua/products/notebooks/p-10/"
url11 = "https://allo.ua/ua/products/notebooks/p-11/"
url12 = "https://allo.ua/ua/products/notebooks/p-12/"
url13 = "https://allo.ua/ua/products/notebooks/p-13/"
url14 = "https://allo.ua/ua/products/notebooks/p-14/"
url15 = "https://allo.ua/ua/products/notebooks/p-15/"
url16 = "https://allo.ua/ua/products/notebooks/p-16/"
url17 = "https://allo.ua/ua/products/notebooks/p-17/"
url18 = "https://allo.ua/ua/products/notebooks/p-18/"
url19 = "https://allo.ua/ua/products/notebooks/p-19/"
url20 = "https://allo.ua/ua/products/notebooks/p-20/"
url21 = "https://allo.ua/ua/products/notebooks/p-21/"
url22 = "https://allo.ua/ua/products/notebooks/p-22/"
url23 = "https://allo.ua/ua/products/notebooks/p-23/"
url24 = "https://allo.ua/ua/products/notebooks/p-24/"
url25 = "https://allo.ua/ua/products/notebooks/p-25/"


i = random.randint(1, 21)
if i == 1:
    url = url1
if i == 2:
    url = url2
if i == 3:
    url = url3
if i == 4:
    url = url4
if i == 5:
    url = url5
if i == 6:
    url = url6
if i == 7:
    url = url7
if i == 8:
    url = url8
if i == 9:
    url = url9
if i == 10:
    url = url10
if i == 11:
    url = url11
if i == 12:
    url = url12
if i == 13:
    url = url13
if i == 14:
    url = url14
if i == 15:
    url = url15
if i == 16:
    url = url16
if i == 17:
    url = url17
if i == 18:
    url = url18
if i == 19:
    url = url19
if i == 20:
    url = url20
if i == 21:
    url = url21
if i == 22:
    url = url22
if i == 23:
    url = url23
if i == 24:
    url = url24
if i == 25:
    url = url25


user = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}




responce = requests.get(url, headers=user)


if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, 'lxml')
    all_product = soup.find('div', class_= "products-layout__container products-layout--grid")
    product = all_product.find_all('div', class_= "product-card")
    for prod in product:
        title = prod.find('a', class_='product-card__title')
        print(title.text)
        try:
            price1 = prod.find('div', class_='v-pb__old')
            price2 = prod.find('div', class_='v-pb__cur discount')
            print(price1.text, price2.text)
        except BaseException:
            print(prod.find('div', class_='v-pb__cur').text)
            print('Немає знижки')

print(f"Сторінка: {i}")