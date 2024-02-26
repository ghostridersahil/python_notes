from bs4 import BeautifulSoup as bs
#have to create obj for html parse

# html_content="<html><body><p>Hello,<b> Sahil Agagrwal</b> !</p></body></html>"

# #we have to create every time this soup obj while using beautiful soup
# soup=bs(html_content,'html.parser')

# bold_text=soup.find('p').get_text()  #just like find() function soup has so many functions we can explore by own

# print(bold_text)


# dynamic scraping
#from wikipedia

import requests as rq

url="https://en.wikipedia.org/wiki/Web_scraping"

response=rq.get(url)  #retriving data from url
# print(response.content)  #sara content including html 

#status code --> 200 represents --> data mil jayega 
            #--> 404 represents --> not found
        
if response.status_code==200:
    soup= bs(response.content,'html.parser')
    content=soup.find(id='content')
    para=content.findAll('p')
    
    for p in para :
        print(p.get_text())
else:
    print("req not found")


