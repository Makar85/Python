from bs4 import BeautifulSoup
import gtts
from playsound import playsound
import pyttsx3
import requests
# make a request to google to get synthesis 
t1 = gtts.gTTS("Привет")
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "Приветствую тебя человек, введи номер телефона чтобы узнать все тайны"
engine.say(text)
#play the speech
engine.runAndWait()
#get details of speacking rate
rate = engine.getProperty("rate")
datas={'number': 'def'}
tel = input("Введите телефон: ")
text1 = "Прекрасный номер, вот информация которую вы искали"
engine.say(text1)
engine.runAndWait()
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










