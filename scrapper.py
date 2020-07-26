from bs4 import BeautifulSoup
import requests
import re
import wget
import datetime
import os

today = datetime.datetime.today().strftime ('%d-%b-%Y')

arr = ['http://www.assamtribune.com/da/index.html', 'http://www.assamtribune.com/at/']

for link in arr:
    source1 = requests.get(link).text
    soup1 = BeautifulSoup(source1, 'lxml')

    for meta1 in soup1.find_all('meta'):
        meta = meta1['content']

    link1 = re.sub('0; url=', '', meta)

    source2 = requests.get(link1).text
    soup2 = BeautifulSoup(source2, 'lxml')

    link2 = soup2.find(class_= 'Toplink')['href']
    link2 = link2.replace("javascript:PopupWindow('atda.asp?id", "http://www.assamtribune.com/scripts/atda.asp?id")
    link2 = link2.replace("');", "")

    source3 = requests.get(link2).text
    soup3 = BeautifulSoup(source3, 'lxml')
    link3 = soup3.find(id="pdfdownload")['href']

    if link == arr[0]:
        wget.download(link3, out=f'Dainik_Asam_{today}.pdf')
    else:
        wget.download(link3, out=f'Assam_Tribune_{today}.pdf')