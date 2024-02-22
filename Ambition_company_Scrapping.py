import requests
from unidecode import unidecode
# from scrapy.selector import Selector
from scrapy.selector import Selector
import pandas as pd

for i in range(12):

    headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(f'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={i}',
                           headers=headers).text

    hxs = Selector(text=webpage)
    company = []
    bad_titles = hxs.xpath('//h2[@class="companyCardWrapper__companyName"]//text()').extract()
    for i in bad_titles:
        company.append(i.strip())

    original_list = hxs.xpath('//div//a//span[@class="companyCardWrapper__ActionCount"]//text()').extract()

    sublist_size = 6
    sublists_comp = [original_list[j:j + sublist_size] for j in range(0, len(original_list), sublist_size)]
    transposed_list = list(zip(*sublists_comp))
    reviews = []
    salary = []
    interview = []
    jobs = []
    benefits = []

    #     for k in transposed_list[0]:
    #         reviews.append(k)

    for k in transposed_list[1]:
        salary.append(k)

    for k in transposed_list[2]:
        interview.append(k)

    for k in transposed_list[3]:
        jobs.append(k)

    for k in transposed_list[4]:
        benefits.append(k)

    #     reviews = transposed_list[0]
    #     salary = transposed_list[1]
    #     interview = transposed_list[2]
    #     jobs = transposed_list[3]
    #     benefits = transposed_list[4]

    rating = hxs.xpath('//div//span[@class="companyCardWrapper__companyRatingValue"]//text()').extract()

    ratings = []
    for rat in rating:
        ratings.append(rat)

d = {'company': company, 'salary': salary, 'interview': interview, 'jobs': jobs, 'benefits': benefits,
     'ratings': ratings}

df = pd.DataFrame(d)
#     print(transposed_list)