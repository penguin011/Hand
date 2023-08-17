from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

APPLICATION_ID = 'YoshikoI-test-SBX-a17c3c2ad-15aacac8'

def get_results(payload):
    try:
        api = Finding(siteid='EBAY-GB', appid=APPLICATION_ID, config_file=None)
        response = api.execute('findItemsAdvanced', payload)
        return response.dict()
    except ConnectionError as e:
        print(e)
        print(e.response.dict())

payload = {
        'keywords': 'Defender', 
        'categoryId': ['29748'],
        'itemFilter': [
            {'name': 'LocatedIn', 'value': 'GB'},
        ],
        'sortOrder': 'StartTimeNewest',
}

results = get_results(payload)