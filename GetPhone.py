from bs4 import BeautifulSoup
import gtts
from playsound import playsound
import pyttsx3
import tkinter as tk
from tkinter import *
import requests

window = tk.Tk()
window.geometry("150x150")
window.title("GetPhoneByMakar")
def print_window():
    print(" Добро пожаловать в номерной узнаватель \n Введите телефон:")
    window.destroy()
but = Button(text = "Начать" ,width=10, command=print_window)
but.pack(side=RIGHT, padx=30, pady=10)
but.pack()
window.mainloop()

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
tel = input()
if len(tel) > 12 and any(c.isalpha() for c in tel)==False:
    text2 = "Вы набрали слишком длинный номер, попробуйте еще раз"
    print(text2) 
    engine.say(text2)
    engine.runAndWait()      
elif len(tel) < 12 and any(c.isalpha() for c in tel)==False:
    text3 = "Вы набрали слишком короткий номер, попробуйте еще раз" 
    print(text3)
    engine.say(text3)
    engine.runAndWait()    
elif any(c.isalpha() for c in tel):
    text4 = "Номер набран некорректно, попробуйте еще раз" 
    print(text4)
    engine.say(text4)
    engine.runAndWait()    
else: 
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












