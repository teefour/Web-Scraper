import requests
import bs4

# Prompt user to enter web URL.
print("Enter website URL:", end=' ')

main_url = input()

print(f"URL to scrape:{main_url}")

#assigning list for each category and a starting page number
titles = []
prices = []
page = 1

for page in range(486, 1000):
    scraping_url = main_url.format(page)
    res = requests.get(scraping_url)
    if 'Not Found' not in res.text:
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        price = soup.select('h4')[0]
        item_title = soup.select('h4')[1]
            prices.append(price.text)
            titles.append(item_title.text)
        print(f'\n{item_title.text} costs {price.text}')
        page += 1
    else:
        break
