# twitter-scrapper
Twitter Scrapper API for Python

# Steps
```
!pip install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
!pip install aiohttp==3.7.0
!pip install nest_asyncio

from twitter_scrapper import collector

keywords = "indihome"
starting_date = None
output_filename = "indihome.csv"
limit = 1000
lang='en'
user = None
format = output_filename[-3:]
collector(keywords, output_filename, starting_date, limit=limit, lang=lang, user=user, format=format)

import pandas as pd

df = pd.read_csv("./indihome.csv", index_col=0)
df.head()
```
