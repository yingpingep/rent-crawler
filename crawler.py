# -*- coding: utf8 -*-
import sys
import requests
from bs4 import BeautifulSoup

# Store all detail of object.
gList = []

def GetDetail(url):   
    # TODO: Error control.

    global gList
    if url == 'done':
        f = open('ouput.txt', 'w', encoding='utf8')    
        for line in gList:
            f.write(line+ '\n')
        f.close()
        return 2

    # Needs user-agent to get all context.
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    detail = requests.get(url, headers=headers)

    soup = BeautifulSoup(detail.text, 'html.parser')

    address = soup.find_all(class_="addr")[0]
    title = soup.find_all('input', id="hid_address")[0]
    price = soup.find_all(class_="price")[0].find('i')

    gList.append("{}\t{}\t{}\t{}".format(address.text, title['value'], price.text.split(' ')[0], url))
    return 1

def GetFromFile(filePath):
    global gList
    f = open(filePath, 'r+', encoding='utf8')
    lines = f.readlines()

    # Reset position from EOF to 0
    f.seek(0)

    for i in range(len(lines)):
        if i != len(lines) - 1:
            GetDetail(lines[i][:-1])
        else:
            GetDetail(lines[i])
        f.write(gList[i] + '\n')    

    f.close()

def main():    
    filePath = ''
    url = ''
    if len (sys.argv) != 1:
        filePath = sys.argv[1]
        GetFromFile(filePath)        
    else:
        r = 1
        while r == 1:
            url = input('URL >>> ')
            r = GetDetail(url)

if __name__ == '__main__':
    main()
