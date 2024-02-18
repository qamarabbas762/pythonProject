for j in range(1):
    headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(f'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={j}',
                           headers=headers).text
    soup = BeautifulSoup(webpage, 'lxml')
    company = soup.find_all('div', class_='companyCardWrapper')

    company_name = []
    sectors = []
    city = []
    salary = []
    ratings = []
    suitability = []
    for i in company:
        try:
            company_name.append(i.find('h2').text.strip())
        except:
            company_name.append(np.nan)
        try:
            salary.append(i.find('span', class_='companyCardWrapper__ActionCount').text)
        except:
            salary.append(np.nan)
        try:
            ratings.append(i.find('span', class_='companyCardWrapper__companyRatingValue').text)
        except:
            ratings.append(np.nan)

            suitability.append(i.find('span', class_='companyCardWrapper__ratingValues').text)
            sectors.append(i.find('span', class_='companyCardWrapper__interLinking').text.split('|')[0].strip())
            city.append(i.find('span', class_='companyCardWrapper__interLinking').text.split('|')[-1].split(' ')[1])

    d = {'company_name': company_name, 'sectors': sectors, 'city': city, 'rating': ratings, 'suitability': suitability,
         'salary': salary}
    df = pd.DataFrame(d)
