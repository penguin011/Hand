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
        data['title_jp'] = convert_text(dom.find('h1', attrs={'class': 'ProductTitle__text'}).text)
        data['purchase_price'] = int(convert_text(dom.find('dd', attrs={'class': 'Price__value'}).contents[0].strip('円')).replace(',', ''))
        data['description_jp'] = []
        descriptions = dom.find('div', attrs={'class': 'ProductExplanation__commentBody js-disabledContextMenu'}).contents
        for description in descriptions:
            if(isinstance(description, str) and description.isspace() is not True):
                data['description_jp'].append(convert_text(description))
        data['photos'] = []
        photos = dom.find('ul', attrs={'class': 'ProductImage__images'}).find_all('li')
        for photo in photos:
            data['photos'].append(
                {
                    'url': photo.div.img['src']
                }
            )

        return data
