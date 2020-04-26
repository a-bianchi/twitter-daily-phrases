import datetime
import os
from modules.twitterApi.index import SendTwitter
from modules.webScraper.index import ScrapProve

autors_url = "https://proverbia.net/autor/index"
base_url = "https://proverbia.net"
number_table_elements = 30

my_scrapy = ScrapProve(base_url, autors_url, number_table_elements)
li = my_scrapy.get_li_autor()
name_autor = li.a.string
href_autor = li.a['href']
quote_autor = my_scrapy.get_quote_autor(href_autor)

# print(quote_autor + ' -' + name_autor)


# try:
#     SendTwitter(quote_autor + " -" + name_autor)
#     print("Twitte sending succefuli at: " + str(datetime.datetime.now()))
# except BaseException as error:
#     print('An exception occurred: {}'.format(error))
