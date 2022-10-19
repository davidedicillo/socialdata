from bs4 import BeautifulSoup
import requests
import re
import time

discords = []

tam = 0

for discord in discords:
    try:
        page = requests.get(discord)
        soup = BeautifulSoup(page.content, "html.parser")
        description = soup.find("meta", property="og:description")
        discord_count = int(re.findall(r'\d+(?:\,\d+)?', description['content'])[-1].replace(',', ''))
        tam += discord_count

        print(discord_count)

    except Exception as e:
        print('failed importing discord count: ' + str(e))
        pass

    time.sleep(1)
    print('total = ' + str(tam))
