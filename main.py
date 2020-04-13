import os
from modules.twitterApi.index import SendTwitter
from modules.webScraper.index import ScrapProve

from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

autors_url = os.environ["AUTORS_URL"]
base_url = os.environ["BASE_URL"]
number_table_elements = int(os.environ["NUMBER_TABLE_ELEMENTS"])

my_scrapy = ScrapProve(base_url, autors_url, number_table_elements)
li = my_scrapy.get_li_autor()
name_autor = li.a.string
href_autor = li.a['href']
quote_autor = my_scrapy.get_quote_autor(href_autor)

print(quote_autor + ' - ' + name_autor)
# SendTwitter(quote_autor + ' - ' + name_autor)
