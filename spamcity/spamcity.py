from multiprocessing import Pool
from os.path import exists
from random import choice
from typing import List
from unittest.mock import DEFAULT

import requests
import tqdm

from config import (
    DEFAULT_CITY,
    DEFAULT_COUNTRY,
    DEFAULT_CRIME_INCREASING,
    DEFAULT_LEVEL_OF_CRIME,
    DEFAULT_PROBLEM_CORRUPTION_BRIBERY,
    DEFAULT_PROBLEM_DRUGS,
    DEFAULT_PROBLEM_PROPERTY_CRIMES,
    DEFAULT_PROBLEM_VIOLENT_CRIMES,
    DEFAULT_SAFE_ALONE_DAYLIGHT,
    DEFAULT_SAFE_ALONE_NIGHT,
    DEFAULT_USER_AGENT,
    DEFAULT_WORRIED_ATTACKED,
    DEFAULT_WORRIED_CAR_STOLEN,
    DEFAULT_WORRIED_HOME_BROKEN,
    DEFAULT_WORRIED_INSULTED,
    DEFAULT_WORRIED_MUGGED_ROBBED,
    DEFAULT_WORRIED_SKIN_ETHNIC_RELIGION,
    DEFAULT_WORRIED_THINGS_CAR_STOLEN,
)
from proxy import download_proxy, is_proxy_working, proxy_generator
from utils import pretty_print_POST


def spam(
    proxies: List[str] | None = None,
    *,
    country: str = DEFAULT_COUNTRY,
    city: str = DEFAULT_CITY,
    ua: List[str] = DEFAULT_USER_AGENT,
    level_of_crime: List[str] = DEFAULT_LEVEL_OF_CRIME,
    crime_increasing: List[str] = DEFAULT_CRIME_INCREASING,
    safe_alone_daylight: List[str] = DEFAULT_SAFE_ALONE_DAYLIGHT,
    safe_alone_night: List[str] = DEFAULT_SAFE_ALONE_NIGHT,
    worried_home_broken: List[str] = DEFAULT_WORRIED_HOME_BROKEN,
    worried_mugged_robbed: List[str] = DEFAULT_WORRIED_MUGGED_ROBBED,
    worried_car_stolen: List[str] = DEFAULT_WORRIED_CAR_STOLEN,
    worried_things_car_stolen: List[str] = DEFAULT_WORRIED_THINGS_CAR_STOLEN,
    worried_attacked: List[str] = DEFAULT_WORRIED_ATTACKED,
    worried_insulted: List[str] = DEFAULT_WORRIED_INSULTED,
    worried_skin_ethnic_religion: List[str] = DEFAULT_WORRIED_SKIN_ETHNIC_RELIGION,
    problem_drugs: List[str] = DEFAULT_PROBLEM_DRUGS,
    problem_property_crimes: List[str] = DEFAULT_PROBLEM_PROPERTY_CRIMES,
    problem_violent_crimes: List[str] = DEFAULT_PROBLEM_VIOLENT_CRIMES,
    problem_corruption_bribery: List[str] = DEFAULT_PROBLEM_CORRUPTION_BRIBERY,
):
    """Change the safety of a selected city by sending spam request.

    :param proxies: A list of proxies
    :param country: The country where the city is, defaults to DEFAULT_COUNTRY
    :param city: The selected city , defaults to DEFAULT_CITY
    :param ua: The list of used user-agent's, defaults to DEFAULT_USER_AGENT
    :param level_of_crime: How important crime are, defaults to DEFAULT_LEVEL_OF_CRIME
    :param crime_increasing: How much does crime increase, defaults to DEFAULT_CRIME_INCREASING
    :param safe_alone_daylight: How safe is it to walk during the day, defaults to DEFAULT_SAFE_ALONE_DAYLIGHT
    :param safe_alone_night: How safe is it to walk during the night, defaults to DEFAULT_SAFE_ALONE_NIGHT
    :param worried_home_broken: How worried inhabitants are of home brokage, defaults to DEFAULT_WORRIED_HOME_BROKEN
    :param worried_mugged_robbed: How worried inhabitants are of mugged robbers, defaults to DEFAULT_WORRIED_MUGGED_ROBBED
    :param worried_car_stolen: How worried inhabitants are of car robbers, defaults to DEFAULT_WORRIED_CAR_STOLEN
    :param worried_things_car_stolen: How worried inhabitants are of things stolen from their car, defaults to DEFAULT_WORRIED_THINGS_CAR_STOLEN
    :param worried_attacked: How worried inhabitants are of being attacked, defaults to DEFAULT_WORRIED_ATTACKED
    :param worried_insulted: How worried inhabitants are of insults, defaults to DEFAULT_WORRIED_INSULTED
    :param worried_skin_ethnic_religion: How worried inhabitants are of ethnic, skin or religious tension, defaults to DEFAULT_WORRIED_SKIN_ETHNIC_RELIGION
    :param problem_drugs: How important are drugs problems, defaults to DEFAULT_PROBLEM_DRUGS
    :param problem_property_crimes: How important are property crimes, defaults to DEFAULT_PROBLEM_PROPERTY_CRIMES
    :param problem_violent_crimes: How frequents are violent crimes, defaults to DEFAULT_PROBLEM_VIOLENT_CRIMES
    :param problem_corruption_bribery: How important is corruption and bribery, defaults to DEFAULT_PROBLEM_CORRUPTION_BRIBERY
    """
    # Finding a working proxy, python should have a fo while loop :(
    proxy = proxy_generator(proxies)
    while not is_proxy_working(proxy):
        proxy = proxy_generator(proxies)

    session = requests.Session()
    url = f"https://www.numbeo.com/crime/form.jsp?country={country}&city={city}"
    jsessionid = "0"
    try:
        response = session.get(url, proxies=proxy, timeout=10)
        session_cookies = session.cookies
        cookies_dictionary = session_cookies.get_dict()
        jsessionid = cookies_dictionary["JSESSIONID"]
        print(jsessionid)
    except:
        print("connection failed")

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


if __name__ == "__main__":
    if not exists("proxies.txt"):
        print("Downloading proxies")
        lines = download_proxy()

        print("Filtering proxies")
        with Pool() as p:
            results = []
            for result in tqdm.tqdm(
                p.imap_unordered(is_proxy_working, lines), total=len(lines)
            ):
                results.append(result)

        proxies = [proxy + "\n" for proxy, valid in results if valid]

        with open("proxies.txt", mode="w") as f:
            f.writelines(proxies)

    with open("proxies.txt", mode="r") as f:
        lines = [line[:-1] for line in f.readlines()]

    while True:
        spam()
