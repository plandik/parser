# Import requests
import requests
from bs4 import BeautifulSoup
import json

# Url the site you want to parse
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l2632&_nkw=rtx+3080&_sacat=175673"

# headers in order not to request a captcha
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.113 Safari/537.36",
    "cookie": "ak_bmsc=36DAF1FABA484A4A4F00FEA953267A01~000000000000000000000000000000~YAAQTn8WAi8w5rR9AQAAobND1A5ZNJXeUbwFDybJ03jRPKlTXJEbJNN1IO5Gyz4WLgWH7GWN83OGPyvX54gLH1NLt670NezTBuBKvWG+3T/KOcRYLz60edXgxnGCzDeVMQ7FLlVviSWDdDT7ARbhfQWBek3RIkHB72OGUUgp3VR+Dhxj9yCmi7tlznzHIvB1uaKb5axzNB5cpPyOxrSSUP+JtjMmy1DmnK11ETkbvQZIudpe0pmMyfPQ/348LIoF1B+AChFVzDtMs64Q/DOf3e5gjgwhYyyGkVcGWOH0Vx0+8pmCvOdcB3jaMpHWfV2CqCcCcBzqW469ZODPaYzL7PRjBeifayuhIQErt0o6i1ce8lb0GROZhrNFbmk+GexTpGSz/wIznqI=; npii=btguid/d443b2f817d0a77d84e6e746ffed49fc6581f555^cguid/d443b78417d0a764b92360d3ffc9631e6581f555^; dp1=bu1p/QEBfX0BAX19AQA**6581f555^pbf/%238000e0000000000000000063a0c1d5^bl/ES6581f555^; ns1=BAQAAAXw0ACieAAaAANgASmOgwdVjNjl8NjAxXjE2Mzk5NDM3NjEyNDVeXjFeM3wyfDV8NHw3fDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3NSrPBF6ogRhwzrjvfYcbUREFLQM3; s=CgAD4ACBhwN/UZDQ0M2IyZjgxN2QwYTc3ZDg0ZTZlNzQ2ZmZlZDQ5ZmNTNx+a; nonsession=BAQAAAXw0ACieAAaAADMABWOgwdUwMzAxNQDKACBlgfVVZDQ0M2IyZjgxN2QwYTc3ZDg0ZTZlNzQ2ZmZlZDQ5ZmMAywACYb+VXTEwGiwc1njG1hIYPOl37LxCtPs0WL4*; bm_sv=7CA0DC826A7D18349F1D4542B70BED25~5EoGL2/01WkWhTxwjb+WfJsySaf9AS1DSaE3n/rEKbAKCXY5nKCKKooPZtqmjCjS8XJSxNqEDyCNfy4c/R5w4oa0I6U3cBXvqynAK/LtifJ42g0mUE4QHoO3w0JzJhzZpXXLaF3UMac3xWQklGAMsw==; ebay=%5Ejs%3D1%5Esbf%3D%23%5Epsi%3DAQ%2B1X8tg*%5E; ds2=sotr/b8_5azzzzzzz^",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}
req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")

# settings for in order to take the articles
all_div_2 = soup.find_all('li', class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
all_div_3 = soup.find_all('h3', class_="s-item__title")

all_article = {}
for item in all_div_3:
    item_text = item.text
    item_print_h3 = print(item_text)

    all_article[item_text] = item_print_h3

# save everything in a json file
with open('articles.json', 'w') as file:
    json.dump(all_article, file, indent=4)

# settings for in order to take the price
all_price_1 = soup.find_all('div', class_="s-item__detail s-item__detail--primary")
all_price_2 = soup.find_all('span', class_="s-item__price")

all_price = {}
for item in all_price_2:
    item_price = item.text
    item_print_price = print(item_price)

    all_price[item_price] = item_print_price

# save everything in a json file
with open('price.json', 'w') as file:
    json.dump(all_price, file, indent=4)

# settings for in order to take where does this come from
from_1 = soup.find_all('div', class_="s-item__detail s-item__detail--primary")
from_2 = soup.find_all('span', class_="s-item__location s-item__itemLocation")

from_3 = {}
for item in from_2:
    item_from = item.text
    item_print_from = print(item_from)

    from_3[item_from] = item_print_from

# save everything in a json file
with open('from.json', 'w') as file:
    json.dump(from_3, file, indent=4)

# print all
print(f'{all_article}' + f'{all_price}' + f'{from_3}')





