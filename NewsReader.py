"""News Reader Bot"""
import requests
import json
from win32com.client import Dispatch
import time
class News:
    def speak(str):
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)
    if __name__=='__main__':
        print("Welcome to Shin's News Reader!!")
        speak("Welcome to Shin's News Reader!!")
        
        url="https://newsapi.org/v2/top-headlines/sources?apiKey=1dd7be28499646c7b80a79f610a068d8"
        try:
            req=requests.get(url=url)
            print(req.status_code)
        except:
            speak("Engine cant get req from News API")
        news_data=json.loads(req.text)
        print(news_data)
        all_news=news_data['sources']
        i=1
        for news in all_news:
            i+=1
            print(str(news['id']), "\n")
            speak(str(news['id']))
            
            print(str(news['description']), "\n")
            speak(str(news['description']))
            print(str(news['url']))
            speak("Visit our page for more info")
            
            #input("Press any key: ")
            if(i==10):
                break
            
        print("Thank you for using my news speaker")
        speak("Thank you for using my news speaker")

