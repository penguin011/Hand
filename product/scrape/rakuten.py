import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        options = webdriver.ChromeOptions() 
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(source_url)
        loaded = None
        data = {}
        while loaded is None:
            dom = bs(driver.page_source, "html.parser")
            loaded = dom.find('div', attrs={'id': 'priceCalculationConfig'})['data-price']
            time.sleep(5)

        data['title_jp'] = convert_text(dom.find('span', attrs={'class': 'normal_reserve_item_name'}).b.text)
        data['purchase_price'] = int(dom.find('div', attrs={'id': 'priceCalculationConfig'})['data-price'])
        if dom.find('ul', attrs={'class': 'point-summary__campaign___2KiT- point-summary__multiplier-up___3664l point-up'}):
            point_info = dom.find('ul', attrs={'class': 'point-summary__campaign___2KiT- point-summary__multiplier-up___3664l point-up'}).find_all('li')
            multi = int(point_info[-1].text.strip('倍UP'))
            data['point'] = int(data['price_jp']*multi/100)
        data['description_jp'] = []
        descriptions = dom.find('span', attrs={'class': 'item_desc'})
        if descriptions:
            for description in descriptions:
                description = convert_text(description.text)
                if(description):
                    data['description_jp'].append(description)
        data['photos'] = []
        photos = dom.find_all('meta', attrs={'itemprop': 'image'})
        for photo in photos:
            data['photos'].append(
                {
                    'url': photo['content']
                }
            )

        return data