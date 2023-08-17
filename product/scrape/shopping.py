import re
import requests
from bs4 import BeautifulSoup as bs

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        resp = requests.get(
            url=source_url,
        )
        dom = bs(resp.content, 'html.parser')
        data = {}
        data['title_jp'] = convert_text(dom.find('p', attrs={'class': 'elName'}).text)
        data['purchase_price'] = int(dom.find('span', attrs={'class': 'elPriceNumber'}).text.replace(',', ''))
        pattern = r'\d+'
        data['point'] = int(re.findall(pattern, dom.find('span', attrs={'class', 'elPaypayPointText'}).text))
        data['description_jp'] = []
        # descriptions = dom.find('div', attrs={'class': 'ProductExplanation__commentBody js-disabledContextMenu'}).contents
        # for description in descriptions:
        #     if(isinstance(description, str) and description.isspace() is not True):
        #         data['description_jp'].append(convert_text(description))
        data['photos'] = []
        photos = dom.find('ul', attrs={'class': 'elThumbnailItems'}).find_all('li')
        for photo in photos:
            data['photos'].append(
                {
                    'url': photo.a.img['src']
                }
            )

        return data
