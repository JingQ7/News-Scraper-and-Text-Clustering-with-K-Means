# Scraping News Articles

import urllib.request
import urllib.error
import re
import time

def get_proxy(url, addr):
    # Create a proxy
    proxy = {'http':addr}
    handler = urllib.request.ProxyHandler(proxy)
    # Get a opener
    opener = urllib.request.build_opener(handler, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    # Open URLs
    try:
        response = urllib.request.urlopen(url, timeout=10)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('Error' + str(e))
        time.sleep(5)
    # Get data
    data = response.read().decode('utf-8', 'ignore')
    return data

myaddr = ['181.129.140.226:39977',
        '182.253.204.155:57463',
        '103.12.161.194:52138',
        '181.30.95.163:33078',
        ]
myurl = 'https://globalnews.ca/toronto/'
data = get_proxy(myurl, myaddr)

each_news = '<a href="(https://globalnews.ca/news/.*?")'
all_news = re.compile(each_news).findall(data)
#print(all_news)

for i in range(0, len(all_news)):
    try:
        print('This is the ' + str(i) + 'th news')
        each = all_news[i]
        path = '/Users/jingjing/Documents/Python_file/spider/projects/news_html/' + str(i) + '.html'
        urllib.request.urlretrieve(each, path)
        print('Finished')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('Error' + str(e))
        time.sleep(5)

for i in range(0, len(all_news)):
    try:
        each = all_news[i]
        data2 = get_proxy(each, myaddr)
        para_key = '<p>(.*?)</p>'
        para = re.compile(para_key).findall(data2)
        #print(para)
        with open('/Users/jingjing/Documents/Python_file/DS/projects/news/news.csv', 'w') as file:
            file.write(str(para[2:-1]))
            file.close()
    except Exception as e:
        print(e)
