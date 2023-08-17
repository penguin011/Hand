import requests
from bs4 import BeautifulSoup as bs

from utils.converttext import convert_text


class ScrapingEngine:
    def scrape_data(self, source_url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': 'yuid=2E782F686320EC2F3E81E25622790573; yid=2E782F686320EC2F3E81E25622790573; yatpz=C1A17BnD7H9%2Ft5PNwCaYY5y1AQ%3D%3D; dduif=",,1,bz8PfNRS9ujVJc1eSq0vF4VSkPvNgeut,1"; newses=0; variodr=100000086601943007; _gcl_au=1.1.223143551.1683193289; _gid=GA1.2.519583435.1683193289; _abck=3C4898CC8FA576B84B7E4AE38EB7598B~0~YAAQ1/AoF9y+8eCHAQAA2r1N5wlnTzzwaE0nh4cfoa/nybSLAQNi7vF9c/2NvrTzDEH7NRb6sLMlNO+f78T8BqTcPq0ATiKzywVaF1Md2ityfWbj8EQ49oJuipj9vi03qldc9nYJogxDWs1aNyHA6ekep+1TSPYObbtVEBe5uv/pwy05zSx2h7uNuJiVn6VI2q2k/4HiVUpNCqv1pI+374XSupGBmnkcLk/tZqDOOUiK02uM0vzhHEPm+AS40AztANnBOXkJBv8CW3zwiKklJmgRgN+y6/f8xmMwT2l2jknjJO631RWgIKIvBkN3iNAYpMKAhtFKto+SMfLzkZgC9uabKlr2jWRcEpw0NIlOop204uvbVS+hNgbMVv8aCKQ/6UiwIj7bOW1zt/99d+Kn8947RNvpK52uCKsk~-1~-1~-1; bm_sz=3F27E0FBBF397916656D37BC57FCEB51~YAAQ1/AoF9++8eCHAQAA2r1N5xPNlsbNcRvHNhFK1LodIM5cViUSiNBKb2DxiP8ny9rpDvpPw1KROZvLIrsL8xEwKR45XZc/wzqlYR13hQ8nrZUM7UkQprc3lQZyavY/fUv8gD8VGOZQyN6aoXlzDCwpzQ9wicmsND8OUr05ep1HIYmc7xY36WCx2Jh/wfLegEBICB7/7QuYrjRowWz0v+cfFtkIYdzAUll/Eg2vRktZc36ul9DgACNb8ekn1wPOZw5NOc90/X1XG7hucC+5ysHHDAeTl520xxsUmSJM5XcXdhfSYCM=~3420228~3356738; ak_bmsc=2529A713ADD113EE9A20096C2BF41027~000000000000000000000000000000~YAAQ1/AoFwzB8eCHAQAAiuhN5xPcWmrJi8SisuBOUhuDMKJkeAeuK7fgO/XDeNHur0nYqLTljr2msQlmAmHkRWKYhuRV3Aq5DTo7FjBZgnVr/5mOcUWTMzvtCYyZClqaf7z151u23LWX1O/pO7ItdguToF4P9eXb5tVwCfteuxioiwrcpW7VnC7R6f4DwpSBV7Q5AMFL+n4MPMAQChCTmKT6PNjKvJfXAi8KwCFSFWoPqvcDHnSzEIgvtzamswnF0BtFRtJsADmmNdaXiHT5pRVlLcBw3LZXzo2ThqHCNXiQSOMEQt+EMpZgU28d6GZbpHV4xjrbj3yBXTRevUG91cDUYase2fIuuEt3eeXJ7sPbep5OQAg3XB+1AXjyU4ldAR/8eHtXyvfWnLDoez+/u48UqRR/BXqXF67trqXTCppBWQu1kT4tS5p8L1jiGyNlw32VGTIEDCRpkOSu+HQwrmV4dGQvJGEcTyqzms7RLpP4R44=; uq=ccaf03b650ea0ff4a4c71a1798943223f4c39c74; JSESSIONID=A60C4B1CEBD3A5139C5B7E0DF1A6DAB6; hty_logout_time="100000001007390034-1683213235492_100000086601943007-1683193465347:"; cto_bundle=_7RfyV9hbUc3ZmNaUDlTYXh1OUJhJTJCcTNnb1hnajclMkZGcTk3VGdqMmwlMkYwSG9SNHFrb0E5NnFFdXNsTCUyRmolMkZtSmIlMkJkQ2tEaU04TFpJVDROMmRRTmdTZk9yODE3dFVKNUZZaEJBMW12OHglMkJPbGdYOGpUVFBoWTJhNkdSMWVIWWVqdW10Z0tTa0xyTkQzdU5EVFQ0NEpKM0xyQldJdyUzRCUzRA; __ukwlgck=9894717.1175262003.0_6_225508242.1683213059783_225508242.513098130.1683213059783; bm_sv=2230C73EFBCD98E48169C51FAAF8BC7C~YAAQ1/AoF+0K8uCHAQAA+ONT5xPVwQ0ktCNl3UdWwzIJ98p6lqjIX0buLAFXYOOw9EAN0zjZ2hg//nFxA3YFS59BnOLkZD/omL2tTGtR98EO0VuMH08efJn0QQdNYrvLnYSQ+Cv40ly7VYllcphHjDL7yEpsjpFeSD+wUPpB5WBKBn9wBcHkcVEnFyH+p8gugNkQ6EjtWvekfTTVpfwqHgJg8strEV2dauKYu4trTkn+AkieVhPOE7uqIMCVpiwFIOM/fg==~1; _ga=GA1.1.1796502326.1683193289; _ga_HK44VQT0MD=GS1.1.1683212703.2.1.1683213111.13.0.0; RT="z=1&dm=www.yodobashi.com&si=06cbf505-0839-4760-b880-574ad105346d&ss=lh99cgxm&sl=3&tt=2nyj&obo=1&rl=1&nu=207re2x3&cl=a42e&ld=keiy&r=3cmrzs2l&ul=keiz"',
            'Referer': 'https://www.yodobashi.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
        resp = requests.get(
            url=source_url,
            headers=headers
        )
        dom = bs(resp.content, "html.parser")
        data = {}
        data['title_jp'] = convert_text(dom.find('h1', attrs={'id': 'products_maintitle'}).span.text)
        data['purchase_price'] = int(dom.find('span', attrs={'id': 'js_scl_unitPrice'}).text[1:].replace(',', ''))
        data['point'] = int(dom.find('span', attrs={'id': 'js_scl_pointValue'}).text.strip('ポイント').replace(',', ''))
        data['description_jp'] = [convert_text(dom.find('div', attrs={'id': 'pinfo_productSummury'}).contents[0].text)]
        data['photos'] = []
        photos = dom.find('div', attrs={'id': 'pImgThumbList'}).ul.find_all('li')
        for photo in photos:
            data['photos'].append(
                {
                    'url': photo.div.a.find('input', attrs={'class': 'largeUrl'})['value']
                }
            )
        
        return data
