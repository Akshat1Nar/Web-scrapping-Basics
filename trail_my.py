from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import msvcrt

page_url ="https://runningstatus.in/"
name=input("Enter full Title:")
while(True):
    
    if(msvcrt.kbhit()):
        
        break
           
    else:
        uClient = uReq(page_url)


        page_soup = soup(uClient.read(),"html.parser")
        uClient.close()

        table_body=page_soup.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols=row.find_all('td')
            cols=[x.text.strip() for x in cols]
            if cols[0]==name:
                print (cols)