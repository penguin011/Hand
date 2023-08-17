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
            loaded = dom.find('div', attrs={'data-testid': 'price'})
            time.sleep(2)

        data['product_name'] = convert_text(dom.find('div', attrs={'data-testid': 'name'}).div.h1.text)
        data['purchase_price'] = int(dom.find('div', attrs={'data-testid': 'price'}).find_all('span')[-1].text.replace(',', ''))

        # data['description_jp'] = [convert_text(dom.find('pre', attrs={'data-testid': 'description'}).text)]
        # data['photos'] = []
        # photos_wrapper = dom.find('div', attrs={'class', 'slick-track'}).contents
        # for photo_wrapper in photos_wrapper:
        #     data['photos'].append(
        #         {
        #             'url': photo_wrapper.find('img')['src']
        #         }
        #     )

        return data
