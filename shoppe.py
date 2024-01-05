import requests
import json
from datetime import datetime

def get_url():
    headers = {
        'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'REC_T_ID=1bfa38f7-aa25-11ee-b1d3-92a5a0afc8dd; SPC_R_T_ID=J7v2A22noUxmrajRZS4fptbGCoLZrA8jBDaUM/D9OdsL6dksh/jOL+4qCdi1ZtYgFlzZcGTUc0nQRvv5GJ14+S9S8uZB+bnR/3IgOhIv7yQTLDeITwtEApyuijkMwgeXhYW9jHjmLIGwRUe9e+x+eMCxzCyG0xXzWC03R/J4Xdc=; SPC_R_T_IV=U3NJb200NXlDU1hDU1NQTg==; SPC_T_ID=J7v2A22noUxmrajRZS4fptbGCoLZrA8jBDaUM/D9OdsL6dksh/jOL+4qCdi1ZtYgFlzZcGTUc0nQRvv5GJ14+S9S8uZB+bnR/3IgOhIv7yQTLDeITwtEApyuijkMwgeXhYW9jHjmLIGwRUe9e+x+eMCxzCyG0xXzWC03R/J4Xdc=; SPC_T_IV=U3NJb200NXlDU1hDU1NQTg==; SPC_SI=/cWTZQAAAAAyT2pYVGNKRPp5FAAAAAAAbExnVlNkZXA=; SPC_SEC_SI=v1-Vk9UbDZtMnczREVLTURROQ2C8f1YbZIzbI92G5M7rbJoKjgB4oxu+6frNzhGBO2yZgU9gyqQsD8exnwjUkatwUTM8lLv8HzW9UyxmaiYpLc=; SPC_F=Dudr47YWpZIJ5zdkZ6nAlRqYcF95lRUx:; REC_T_ID=01e92f0d-a972-11ee-96c1-66f89c1377f4; SPC_F=P6KVYH3ZeQ53k8QiEQL7LASqM4kAuJsX; SPC_R_T_ID=J7v2A22noUxmrajRZS4fptbGCoLZrA8jBDaUM/D9OdsL6dksh/jOL+4qCdi1ZtYgFlzZcGTUc0nQRvv5GJ14+S9S8uZB+bnR/3IgOhIv7yQTLDeITwtEApyuijkMwgeXhYW9jHjmLIGwRUe9e+x+eMCxzCyG0xXzWC03R/J4Xdc=; SPC_R_T_IV=U3NJb200NXlDU1hDU1NQTg==; SPC_SI=/cWTZQAAAAAyT2pYVGNKRPp5FAAAAAAAbExnVlNkZXA=; SPC_T_ID=J7v2A22noUxmrajRZS4fptbGCoLZrA8jBDaUM/D9OdsL6dksh/jOL+4qCdi1ZtYgFlzZcGTUc0nQRvv5GJ14+S9S8uZB+bnR/3IgOhIv7yQTLDeITwtEApyuijkMwgeXhYW9jHjmLIGwRUe9e+x+eMCxzCyG0xXzWC03R/J4Xdc=; SPC_T_IV=U3NJb200NXlDU1hDU1NQTg==; __LOCALE__null=VN',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120":',
        'Sec-Ch-Ua-Mobile': '?0:',
        'Sec-Ch-Ua-Platform': '"Windows":',
        'Sec-Fetch-Dest': 'document:',
        'Sec-Fetch-Mode': 'navigate:',
        'Sec-Fetch-Site': 'none:',
        'Sec-Fetch-User': '?1:',
        'Upgrade-Insecure-Requests': '1:',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36:',
        'Postman-Token': '82d64365-a611-4f3a-b259-2a0e09502140',
        'Host': 'shopee.vn',
        'Connection': 'keep-alive',
    }
    params = {
        'bundle': 'category_landing_page',
        'cat_level': 1,
        'catid': 11036132,
        'limit': 10000,
        'offset': 0,
    }
    # url = requests.get('https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11036132&limit=60&offset=0',headers=headers)
    url = requests.get('https://shopee.vn/api/v4/recommend/recommend',headers=headers,params=params)
    get_data = json.loads(url.text)
    item = get_data['data']['sections'][0]['data']['item']
    return item
items = get_url()
# print(type(items))
product = []
for i, j in enumerate(items):
    # print(items[i]['name'])
    get_item = {}
    get_item['date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    get_item['name'] = items[i]['name']
    get_item['image'] = items[i]['image']
    get_item['stock'] = items[i]['stock']
    get_item['sold'] = items[i]['sold']
    product.append(get_item)
#     product[i]['name'] = items[i]['name']
#     product[i]['image'] = items[i]['imamge']
#     product[i]['stock'] = items[i]['stock']
#     product[i]['sold'] = items[i]['sold']
# print(product[3]['name'])
# for i , j in enumerate(product):
#     print(product[i]['name'])
print(len(product))


    