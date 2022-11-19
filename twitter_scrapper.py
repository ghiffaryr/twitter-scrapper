import twint
import nest_asyncio
import time

def collector(keywords, output_filename, starting_date=None, end_date=None, limit=1000, lang='id', user=None, format='csv'):
    # execution date
    print('Execution Date: ', time.strftime("%Y%m%d"))

    # to avoid the event loop is already running in python error message.
    nest_asyncio.apply()

    # configure
    conf = twint.Config()
    
    # tweets from username
    if user is not None: conf.Username = tweet_user

    # get tweets published starting date
    if starting_date is not None: conf.Since = starting_date
    
    # get tweets published end date
    if end_date is not None: conf.Until = end_date

    # search criteria
    conf.Search = keywords
  
    # search languange
    conf.Lang = lang
    
    # tweet limit
    conf.Limit = limit

    # output filename
    conf.Output = output_filename

    # output file format
    if format == 'csv':
      conf.Store_csv = True
    elif format == 'json':
      conf.Store_json = True
    else:
      pass

    # run
    twint.run.Search(conf)
