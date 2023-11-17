from bs4 import BeautifulSoup
import requests

from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
import pandas as pd



#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#driver = webdriver.Firefox
#
#products=[] #List to store name of the product
#prices=[] #List to store price of the product
#ratings=[] #List to store rating of the product
#topics = []
#sub_topics = []
#driver.get("https://developer.android.com/reference/packages")
#
#
#content = driver.page_source
#soup = BeautifulSoup(content)
#for a in soup.findAll('li', attrs={'class':'devsite-nav-item devsite-nav-expandable'}):
#    topic = a.find('div', attrs={'class':'devsite-nav-title devsite-nav-title-no-path'})
#    sub_topic = a.find('span', attrs={'class':'devsite-nav-text'})
#    topics.append(topic.text)
#    sub_topics.append(sub_topic.text)
    
    
    
    



#df = pd.DataFrame({'Topics':topics,'Sub_Topics':prices}) 
#df.to_csv('Java.csv', index=False, encoding='utf-8')

topics1 = []
sub_topics1 = []

html_text = requests.get('https://developer.android.com/reference/packages').text

soup = BeautifulSoup(html_text, 'lxml')

topics = soup.find_all('li', class_ = 'devsite-nav-item devsite-nav-expandable')

#for topic in topics:
#    test = topics.find('span', class_ = 'devsite-nav-text').span.text
#    print(test)
#
#print(topics)
#topics = soup.find_all('li', class_ = 'devsite-nav-item devsite-nav-expandable')
#topic1 = topics.find_a
#for topic in topics:
#    sub_topic = topics.find()
#print(topics)
#
#categories_to_remove = ['Classes', 'Interfaces', 'Enums', 'Exceptions']
#for topic in topics:
#    topic1 = topic.find('div', class_ = 'devsite-nav-title devsite-nav-title-no-path').text
#    sub_topic = topic.find('span', class_ = 'devsite-nav-text').text
#    topics1.append(topic1)
#    sub_topics1.append(sub_topic)
#    print(f'''Main Topic: {topic1}
#    Subtopic: {sub_topic}''')
#
#    print(' ')

categories_to_remove = ['Classes', 'Interfaces', 'Enums', 'Exceptions', 'Errors', 'Annotations']

for topic in topics:
    topic1 = topic.find('div', class_='devsite-nav-title devsite-nav-title-no-path').text
    sub_topic = topic.find('span', class_='devsite-nav-text').text

    if sub_topic not in categories_to_remove:
        topics1.append(topic1)
        sub_topics1.append(sub_topic)
        print(f'''Main Topic: {topic1}
        Subtopic: {sub_topic}''')

        print(' ')



df = pd.DataFrame({'Topics':topics1,'Sub_Topics':sub_topics1}) 
df.to_csv('Java3.csv', index=False, encoding='utf-8')


#categories_to_remove = ['Classes', 'Interfaces', 'Enums', 'Exceptions']
#
## Filter out specified categories
#filtered_items = [item for item in items if item not in categories_to_remove]
#
## Print the filtered list
#print(filtered_items)