import json
import requests
from bs4 import BeautifulSoup as bs

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        resp = requests.get(
            url=source_url,
        )
        dom = bs(resp.content, "html.parser")
        data = {}
        data['title_jp'] = convert_text(dom.find('h1', attrs={'id': 'item_title'}).text)
        data['purchase_price'] = int(json.loads(dom.find('div', attrs={'class': 'item-price form-inline'}).div.input['data-zaiko'])['baika'])
        data['description_jp'] = []
        descriptions = dom.find('div', attrs={'id': 'item_detailInfo'}).find('p', attrs={'class': 'note text-break'}).contents
        for description in descriptions:
            if(isinstance(description, str) and description.isspace() is not True):
                data['description_jp'].append(convert_text(description))
        data['photos'] = []
        photos = dom.find('div', attrs={'class': 'product_zoom'}).find_all('div', attrs={'class': 'swiper-slide'})
        for photo in photos:
            data['photos'].append({
                'url': photo.a['data-standard']
            })

        return data
