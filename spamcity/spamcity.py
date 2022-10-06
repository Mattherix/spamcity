import urllib
from itertools import count
from multiprocessing import Pool
from random import choice, randint
from time import sleep
from typing import Tuple
import requests
from bs4 import BeautifulSoup
import tqdm
from os.path import exists
from proxy import download_proxy, is_proxy_working, proxy_generator


def pretty_print_POST(req):
    print(
        "{}\n{}\r\n{}\r\n\r\n{}".format(
            "-----------REQUEST-----------",
            req.method + " " + req.url,
            "\r\n".join("{}: {}".format(k, v) for k, v in req.headers.items()),
            req.body,
        )
    )


def spam():
    status_code = 0
    while status_code != 200:
        proxy = proxy_generator(lines)
        try:
            response = requests.get("https://api.myip.com/", proxies=proxy, timeout=5)
            print(response.json())
            status_code = response.status_code
        except:
            print("Proxy is not responding, trying another one")

    session = requests.Session()
    country = "France"
    city = "Rennes"
    url = f"https://www.numbeo.com/crime/form.jsp?country={country}&city={city}"
    jsessionid = "0"
    try:
        response = session.get(url, proxies=proxy, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        checking = soup.find("input", {"name": "checking"}).get("value")
        print(checking)
        session_cookies = session.cookies
        cookies_dictionary = session_cookies.get_dict()
        jsessionid = cookies_dictionary["JSESSIONID"]
        print(jsessionid)
    except:
        print("connection failed")

    ua = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    ]

    level_of_crime = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    crime_increasing = ["-2.0", "-2.0", "-2.0", "-2.0"]
    safe_alone_daylight = ["2.0", "2.0", "2.0", "1.0", "1.0"]
    safe_alone_night = ["2.0", "2.0", "2.0", "2.0", "2.0"]
    worried_home_broken = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    worried_mugged_robbed = [
        "-2.0",
        "-2.0",
        "-2.0",
        "-2.0",
        "-2.0",
        "-1.0",
        "-2.0",
        "-1.0",
    ]
    worried_car_stolen = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    worried_things_car_stolen = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    worried_attacked = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0"]
    worried_insulted = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    worried_skin_ethnic_religion = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    problem_drugs = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    problem_property_crimes = ["-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    problem_violent_crimes = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
    problem_corruption_bribery = [
        "-2.0",
        "-2.0",
        "-2.0",
        "-2.0",
        "-2.0",
        "-2.0",
        "-1.0",
    ]

    headers = {
        "Host": "fr.numbeo.com",
        "User-Agent": choice(ua),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.numbeo.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://fr.numbeo.com/criminalit%C3%A9/modifier?returnUrl=https%3A%2F%2Ffr.numbeo.com%2Fcriminalit%25C3%25A9%2Fville%2FRennes&tracking=getEnterDataHtml2ForExtendedModuos&locCity=Rennes&locCountry=France",
        "Cookie": "JSESSIONID=" + jsessionid,
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
    }
    data = {
        "locCountry": "France",
        "locCity": "Rennes",
        "level_of_crime": choice(level_of_crime),
        "crime_increasing": choice(crime_increasing),
        "safe_alone_daylight": choice(safe_alone_daylight),
        "safe_alone_night": choice(safe_alone_night),
        "worried_home_broken": choice(worried_home_broken),
        "worried_mugged_robbed": choice(worried_mugged_robbed),
        "worried_car_stolen": choice(worried_car_stolen),
        "worried_things_car_stolen": choice(worried_things_car_stolen),
        "worried_attacked": choice(worried_attacked),
        "worried_insulted": choice(worried_insulted),
        "worried_skin_ethnic_religion": choice(worried_skin_ethnic_religion),
        "problem_drugs": choice(problem_drugs),
        "problem_property_crimes": choice(problem_property_crimes),
        "problem_violent_crimes": choice(problem_violent_crimes),
        "problem_corruption_bribery": choice(problem_corruption_bribery),
        "checking": jsessionid,
        "returnUrl": "https://fr.numbeo.com/criminalit%C3%A9/ville/Rennes",
    }

    url = "https://fr.numbeo.com/crime/i18n-save"

    req = requests.Request("POST", url, headers=headers, data=data)
    prepared = req.prepare()
    pretty_print_POST(prepared)
    try:
        response = session.send(prepared, proxies=proxy, timeout=10)
        print(response.status_code)
    except:
        print("connection failed")


if __name__ == '__main__':
    if not exists("proxies.txt"):
        print("Downloading proxies")
        lines = download_proxy()

        print("Filtering proxies")
        with Pool() as p:
            results = []
            for result in tqdm.tqdm(p.imap_unordered(is_proxy_working, lines), total=len(lines)):
                results.append(result)

        proxies = [proxy + '\n' for proxy, valid in results if valid]

        with open("proxies.txt", mode='w') as f:
            f.writelines(proxies)

    with open("proxies.txt", mode="r") as f:
        lines = [line[:-1] for line in f.readlines()]

    while True:
        spam()
