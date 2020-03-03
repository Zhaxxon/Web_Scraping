from pprint import pprint
from lxml import html
import requests
import time
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def request_to_yandex(str):
        try:
            time.sleep(1)
            response = requests.get('https://yandex.ru/search/',
                         params={'text':str},
                         # headers = header
                        )

            root = html.fromstring(response.text)
            result = root.xpath(
                "//a[contains(@class,'link_cropped_no')]/@href | //a[contains(@class,'organic__url_type_multiline')]/@href"
                # "////a[contains(@class,'organic__url')]"
            )
            return result
        except:
            print('Ошибка запроса')

# for i in range(50):
    # result = request_to_yandex('Шляпа')
result = request_to_yandex('Шляпа')
pprint(result)
