from importlib import import_module

from utils.scrape_site import scraping_site


def select_engine(url):
    result = ''
    for site in scraping_site.keys():
        if site in url:
            result = site
            break

    if result:
        module = import_module(f'product.scrape.{result}')
        engine = getattr(module, 'ScrapingEngine')
        return engine
    
    return None