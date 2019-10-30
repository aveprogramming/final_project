import requests
from bs4 import BeautifulSoup
from time import sleep


def get_html(url):
    sleep(0.5)
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    headline = soup.find('h1', class_='ArticleHeader_headline').text
    content = ''.join([text.text for text in soup.find('div', class_='StandardArticleBody_body').find_all('p')])
    date = soup.find("div", class_= 'ArticleHeader_date').text.split('/')[0].strip()

    headlines.append(headline)
    contents.append(content)
    dates.append(date)


def make_all(url):  # РґР»СЏ РјСѓР»СЊС‚РёРїСЂРѕС†РµСЃСЃРёРЅРіР°
    text = get_html(url)
    get_data(text)


def receive_news():

    global dictionary, headlines, contents, dates, urls
    headlines, contents, dates, links = [], [], [], []

    urls = ["https://www.reuters.com/politics",
            "https://www.reuters.com/news/technology",
            "https://www.reuters.com/finance"]

    links = []

    for url in urls:
        soup = BeautifulSoup(get_html(url), 'lxml')

        if url == "https://www.reuters.com/politics":
            for link in soup.find_all('h2', class_='FeedItemHeadline_headline FeedItemHeadline_full'):
                links.append(link.a.get('href'))
        else:
            for link in soup.find_all('div',class_="story-content"):
                links.append(url+link.a.get('href'))

    for link in links[:20]:
        try:
            get_data(get_html(link))
        except:
            continue
    dictionary = list(zip(headlines, contents, dates, links))
    posts_new = []
    for article in dictionary:
        dict_post = {'headline': article[0], 'content': article[1], 'date': article[2], 'url': article[3]}
        posts_new.append(dict_post)
    return posts_new


print(receive_news())
