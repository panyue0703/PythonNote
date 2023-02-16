import requests
from lxml import etree

city = str(input('请输入城市：'))
cities = {'北京': 'bj', '上海': 'sh', '武汉': 'wh', '成都': 'cd'}

house_list = []
pages = range(1, 5)
for j in pages:
    url = f'https://{cities[city]}.zu.ke.com/zufang/pg{j}/#contentList'
    resp = requests.get(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Cooike': 'select_city=510100; lianjia_ssid=6684dd44-0486-41a7-8955-3d3a9a47f185; lianjia_uuid=8aaebf9b-ab20-4b32-8a7f-f88a7f4bf9d1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzJlYjFjNjk4MzQ5MmVmMzI2ZmUyZDE3YTRhN2YzYzU1N2VmM2Q0Y2UwNmUzYjlmYWRhMDg5NWNjZDdiNGY4NjI5MDE5YjI4ZTI3NjgxOWVhMDgxYjMyODYzN2FlOTlmZjZmZjQ4MmE3ZGRlOThhNGRkZmJhMWE5Y2YyMTgwYzdjNzViMmE3NGIzMzUyZTI3OWQ4MTFhOGQ0NTJhMzNiYWU2YmZlOTMxZmJiMDdiNjBhNGEyZTY5MjdiMTQ4ZWFlOTQzYjZlNzVhODM5NjQzMDhiNWIzMTg5ZTUzYjk3MmFiYWQ4MzUxMzFmY2RiYjYwMTA4YjY1ZDgzNTRlMTA5NVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI4ZDk0ZmE3ZlwifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='}
    resp = requests.get(url, headers=headers)
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.XML(resp.text, parser=parser)

    elements_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div')
    try:
        for elements in elements_list:
            title = (elements.xpath('./div/p[1]/a/text()')[0]).strip()
            price = (elements.xpath('./div/span/em/text()')[0]).strip()
            area = (elements.xpath('./div/p[2]/a[2]/text()')[0]).strip()
            sub = (elements.xpath('./div/p[2]/a[3]/text()')[0]).strip()
            house_size = (elements.xpath('./div/p[2]/text()[last()-1]')[0]).strip()
            tow = (elements.xpath('./div/p[2]/text()[last()-2]')[0]).strip()
            house_type = (elements.xpath('./div/p[2]/text()[last()-3]')[0]).strip()
            house_list.append([title, price, area, sub, house_size, tow, house_type])
    except:
        pass
    for num in house_list:
        print(num)
