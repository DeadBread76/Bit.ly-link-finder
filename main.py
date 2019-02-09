import requests
import random
import string
from requests_html import HTMLSession

char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
data = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'} # found more success using a user-agent

while True:
    try:
        link = 'https://bit.ly/'+(''.join(random.sample(char_set*6, 6)))
        src = requests.get(link, data=data)
        if src.status_code == 200:
            title = src.text
            title = title[title.find('<title>')+7:title.find('</title>')]+'\n' # eh
            with open("bitlylinks.txt","a") as handle:
                try:
                    if len(title) > 100: # check here incase the site spews its guts
                        continue
                    else:
                        handle.write(title) 
                        print(title)
                    handle.write(str(link)+ '\n------------\n') #uh
                except Exception:
                    print('Error writing to disk.') # i mean I would return buuuuuuuuut
    except Exception:
        print('Something fucked up, could not connect to bit.ly!\n')
