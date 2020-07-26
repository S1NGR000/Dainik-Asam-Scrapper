from bs4 import BeautifulSoup       #for scrapping
import requests                     #for fetching the source
import re                           #for cleaning the urls
import wget                         #for downloading the pdf
import datetime                     #for renaming the newspaper 

#fetches today's date
today = datetime.datetime.today().strftime ('%d-%b-%Y')

#two urls for both websites
arr = ['http://www.assamtribune.com/da/index.html', 'http://www.assamtribune.com/at/']

for link in arr:

    #fetches source of the webpage from links of the above array
    source1 = requests.get(link).text
    soup1 = BeautifulSoup(source1, 'lxml')

    #fetches the meta tags where the link to the daily newspaper resides
    for meta1 in soup1.find_all('meta'):
        meta = meta1['content']
    
    #cleans url
    link1 = re.sub('0; url=', '', meta)

    #fetches source of the webpage where daily newspaper is dispalyed
    source2 = requests.get(link1).text
    soup2 = BeautifulSoup(source2, 'lxml')

    #fetches the link of the download page
    link2 = soup2.find(class_= 'Toplink')['href']

    #cleans the url
    link2 = link2.replace("javascript:PopupWindow('atda.asp?id", "http://www.assamtribune.com/scripts/atda.asp?id")
    link2 = link2.replace("');", "")

    #fetches the source of the download page
    source3 = requests.get(link2).text
    soup3 = BeautifulSoup(source3, 'lxml')

    #grabs the download link
    link3 = soup3.find(id="pdfdownload")['href']

    #downloads the pdf and rename them according to the newspaper name
    if link == arr[0]:
        wget.download(link3, out=f'Dainik_Asam_{today}.pdf')
    else:
        wget.download(link3, out=f'Assam_Tribune_{today}.pdf')