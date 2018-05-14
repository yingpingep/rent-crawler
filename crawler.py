# -*- coding: utf8 -*-
import sys
import requests
from bs4 import BeautifulSoup

def GetDetail(url):
    # Needs user-agent to get all context.
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    detail = requests.get(url, headers=headers)

    soup = BeautifulSoup(detail.text, 'html.parser')
    # ss = soup.find_all(attrs={"class": "addr", "name": "hid_address", "id": "hid_imgArr"})

    address = soup.find_all(class_="addr")[0]
    title = soup.find_all('input', id="hid_address")[0]
    # imgs = soup.find_all(id="hid_imgArr")
    price = soup.find_all(class_="price")[0].find('i')

    print(address.text)
    print(title['value'])
    print(price.text.split(' ')[0])
    print(url)

def main():
    # print(sys.argv[1])
    url = input("Give me a url: ")
    GetDetail(url)

if __name__ == '__main__':
    main()