import re
import requests
from bs4 import BeautifulSoup as bs

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': 'session-id=356-0993705-9222727; session-id-time=2082787201l; i18n-prefs=JPY; lc-acbjp=en_US; sp-cdn="L5Z9:RU"; ubid-acbjp=355-9629853-1549123; session-token=Yt8EhPDZPo7Dw/4MT3na9yBmnfZ20zhSanoIOp1ahYeq6wUMMlZ6eCdPLrTPJuII3WccRMxvIcQil+itCoWZBo8mB0okgTsGGnbvMEtC1uZQQfp5Vj8hamWsnomhu+kWhIIfWd5PawMwv9Wjk2aRJTgbBIYzHTt8F4y1dg9x9CpRtFG45kcBRtzBMogGpkxRafUPjvDoqKGxC0PIQ5LHgZWEAC9mzvfiIhs0xbErh3c=; csm-hit=tb:s-YQY3V7RA71VHFKGE4TTH|1683522988590&t:1683522990770&adb:adblk_yes',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        resp = requests.get(
            url=source_url,
            headers=headers
        )
        dom = bs(resp.content, 'html.parser')
        item_detail = dom.find('div', attrs={'id': 'dp-container'})
        data = {}
        data['title_jp'] = item_detail.find('span', attrs={'id': 'productTitle'}).text
        data['purchase_price'] = int(item_detail.find('span', attrs={'id': 'color_name_2_price'}).span.text.split('¥')[-1].replace(',', ''))
        data['description_jp'] = []
        descriptions = item_detail.find('div', attrs={'id': 'feature-bullets'}).ul.find_all('span', attrs={'class': 'a-list-item'})
        for description in descriptions:
            data['description_jp'].append(description.text)
        
        pattern = r'"hiRes":"https://m.media-amazon.com.*?.jpg'
        matches = re.findall(pattern, item_detail.find('div', attrs={'id': 'imageBlock_feature_div'}).find_all('script')[2].text)
        data['photos'] = []
        for item in matches:
            url = item.split('"')[-1]
            data['photos'].append(
                {
                    'url': url
                }
            )

        return data
