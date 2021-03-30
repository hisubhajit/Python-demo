import requests
from bs4 import BeautifulSoup
print("Test")
#URL = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=IDEA&illiquid=0&smeFlag=0&itpFlag=0'
URL = 'https://www1.nseindia.com'
print("after url")
page = requests.get('https://www.nseindia.com/get-quotes/equity?symbol=IDEA')
print("Page Created!!!")
soup = BeautifulSoup(page.content, 'html.parser')
print("soup Created!!!")
results = soup.find(id='lastPrice')
print(results)