from bs4 import BeautifulSoup
import requests

url = "https://www.ixbt.com/news/?ysclid=ldmtso9qvn646541194"
request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

news = soup.find_all("strong")

for item in news:
    print("-  "+item.text+ "\n")



