import requests
from unidecode import unidecode
from scrapy.selector import Selector
import pandas as pd


for j in range(12):
    data = requests.get(
        f"https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={j}")
    hxs = Selector(text=data.text)
    product = []
    price = []
    storage = []
    screen_size = []
    battery_size = []
    processor = []

    for i in hxs.xpath('.//div[@class="_3pLy-c row"]//div[@class="_4rR01T"]//text()').extract():
        product.append(i)

    for i in hxs.xpath('//div[@class="_25b18c"]//div[@class="_30jeq3 _1_WHN1"]//text()').extract():
        price.append(i)

    for i in hxs.xpath('//div[@class="fMghEO"]//ul//li[@class="rgWa7D"][1]//text()').extract():
        storage.append(i)

    for i in hxs.xpath('//div[@class="fMghEO"]//ul//li[@class="rgWa7D"][2]//text()').extract():
        screen_size.append(i)

    for i in hxs.xpath('//div[@class="fMghEO"]//ul//li[@class="rgWa7D"][4]//text()').extract():
        battery_size.append(i)

    for i in hxs.xpath('//div[@class="fMghEO"]//ul//li[@class="rgWa7D"][5]//text()').extract():
        processor.append(i)

d = {'product': product, 'storage': storage, 'screen size': screen_size, 'battery size': battery_size,
     'processor': processor, 'price': price}

pd.DataFrame(d)