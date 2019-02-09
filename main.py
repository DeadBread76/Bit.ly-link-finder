import requests
import random
import string
from requests_html import HTMLSession



char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase

while True:
    try:
        link = 'https://bit.ly/'+(''.join(random.sample(char_set*6, 6)))
        src = requests.get(link)

        if src.status_code == 200:
            print (link)
            print (HTMLSession().get(link).html.find('title', first=True).text)
            file = open("bitlylinks.txt","a")
            file.write(str(link)+ '\n')
            file.close()
            file = open("bitlylinks.txt","a")
            file.write((HTMLSession().get(link).html.find('title', first=True).text)+ '\n' + '\n')
            file.close()

        else:
            print('Invalid link')

    except Exception:
        print('Something fucked up there') 






