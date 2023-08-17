import requests
from bs4 import BeautifulSoup as bs

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        resp = requests.get(
            url=source_url,
        )
        item_detail = bs(resp.content, "html.parser").find('div', attrs={'class': 'product-detail'})
        data = {}
        data['title_jp'] = item_detail.find('div', attrs={'class': 'product-detail-name'}).h1.text
        data['purchase_price'] = int(item_detail.find('span', attrs={'class': 'product-detail-price__main'}).text.replace(',', ''))
        data['description_jp'] = []
        table= item_detail.find('div', attrs={'id': 'panel1'}).table.contents
        for row in table:
            if hasattr(row, 'contents'):
                if(len(row.contents) == 2):
                    description = convert_text(row.contents[0].text + ': ' + row.contents[1].text)
                elif(len(row.contents) == 5):
                    description = convert_text(row.contents[1].text + ': ' + row.contents[3].text)
                
                data['description_jp'].append(description)

        data['photos'] = []
        photos = item_detail.find('div', attrs={'class': 'product-detail-images-main'}).find_all('img')
        for photo in photos:
            data['photos'].append(
                {
                    'url': photo['src']
                }
            )
        
        return data
