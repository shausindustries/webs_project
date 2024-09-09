import requests
from bs4 import BeautifulSoup

header_a = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36","Referer":"https://www.google.com/"}
header_f = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"}


print("Welcome! \nThis software would suggest you from which e-commerce platform \nyou can buy your iPhone for the lowest price possible\n ")
choice = int(input("Choose your version:\n1) iPhone 13\n2) iPhone 14\n3) iPhone 15\n"))
if choice==1:
    sbc1 = int(input("Choose your model:\n1) iPhone 13\n2) iPhone 13 pro\n3) iPhone 13 pro max\n"))
    if sbc1==1:
        a_url = "https://www.amazon.in/s?k=iphone+13&crid=3FI6GIELIYQ72&sprefix=iphone+13%2Caps%2C404&ref=nb_sb_noss_1"
        f_url = "https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+13%7CMobiles&requestId=92465842-27f5-41e4-946b-9af78f098b9c&as-searchtext=iphone%2013"

        a_r = requests.get(a_url, headers=header_a)
        f_r = requests.get(f_url, headers=header_f)

        a_soup = BeautifulSoup(a_r.text,'html.parser')
        f_soup = BeautifulSoup(f_r.text,'html.parser')

        a_spans = a_soup.select("span.a-size-medium.a-color-base.a-text-normal")
        with open("data/amazon.txt",'w',encoding='utf-8') as f:
            for a_span in a_spans:
                f.write(f"{a_span.get_text()}\n")
        a_prices = a_soup.select("span.a-price")
        with open("data/amazon.txt",'a', encoding='utf-8') as f:
            for a_price in a_prices:
                if not("a-text-price" in a_price.get("class")):
                    f.write(f"{a_price.find('span').get_text()}\n")

        f_spans = f_soup.select("div.KzDlHZ")
        with open("data/flipkart.txt",'w',encoding='utf-8') as f:
            for f_span in f_spans:
                f.write(f"{f_span.get_text()}\n")
        f_prices = f_soup.select("div.hl05eU")
        with open("data/flipkart.txt",'a',encoding='utf-8') as f:
            for f_price in f_prices:
                f.write(f"{f_price.find("div").get_text()}\n")
    elif sbc1==2:
        f_url = "https://www.flipkart.com/search?q=iphone%2013%20pro&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        f_r = requests.get(f_url, headers=header_f)
        f_soup = BeautifulSoup(f_r.text,'html.parser')

        f_spans = f_soup.select("div.KzDlHZ")
        with open("data/flipkart.txt",'w',encoding='utf-8') as f:
            for f_span in f_spans:
                f.write(f"{f_span.get_text()}\n")
    else:
        f_url = "https://www.flipkart.com/search?q=iphone+13+pro+max&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_17_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_17_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone+13+pro+max&requestId=88d8f98b-346c-4dd5-aa89-155c6706331f&as-searchtext=iphone%2013%20pro%20max"
        f_r = requests.get(f_url, headers=header_f)
        f_soup = BeautifulSoup(f_r.text,'html.parser')

        f_spans = f_soup.select("div.KzDlHZ")
        with open("data/flipkart.txt",'w',encoding='utf-8') as f:
            for f_span in f_spans:
                f.write(f"{f_span.get_text()}\n")
elif choice==2:
    sbc2 = int(input("Choose your model:\n1) iPhone 14\n2) iPhone 14 plus\n3) iPhone 14 pro\n4) iPhone 14 pro max\n"))
    if sbc2==1:
        print("okay")
    elif sbc2==2:
        print("okay")
    elif sbc2==3:
        print("okay")
    else:
        print("okay")
else:
    sbc3 = int(input("Choose your model:\n1) iPhone 15\n2) iPhone 15 plus\n3) iPhone 15 pro\n4) iPhone 15 pro max\n"))
    if sbc3==1:
        print("okay")
    elif sbc3==2:
        print("okay")
    elif sbc3==3:
        print("okay")
    else:
        print("okay")