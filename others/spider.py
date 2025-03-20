import json
import requests
from bs4 import  BeautifulSoup




if __name__ == '__main__':

    header_str= {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

    url = "https://smzdk.top/#/"

    response_str = requests.get(url,headers=header_str).content
    print(BeautifulSoup.find(response_str))



