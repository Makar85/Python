from bs4 import BeautifulSoup
import requests
datas={'number': 'def'}
tel = input("Введите телефон: ")
datas['number'] = tel
url = "https://www.kody.su/check-tel#text"
ses = requests.Session()
l=ses.post(url, data = datas)
soup = BeautifulSoup(l.text, "html.parser")
result = soup.find_all("strong")
it=0
for i in result:
    if it==0:
        print("Страна: " + result[0].text)        
    elif it==1:
        print("Оператор [Регион]: " + result[1].text)             
    it+=1










