# twitter-scrapper
Twitter Scrapper API for Python

# Steps
```
!pip install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
!pip install aiohttp==3.7.0
!pip install nest_asyncio

from twitter_scrapper import collector

keywords = "indihome"
starting_date = None # "2022-11-10 00:00:00"
end_date = None # "2022-11-11 00:00:00"
output_filename = "indihome_predict.csv"
limit = 1000
lang='id'
user = None
format = output_filename[-3:]
collector(keywords, output_filename, starting_date=starting_date, end_date=end_date, limit=limit, lang=lang, user=user, format=format)

import pandas as pd

df = pd.read_csv("./indihome.csv", index_col=0)
df.head()
```
