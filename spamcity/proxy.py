"""
spamcity.proxy
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.
"""

from random import choice
from typing import Dict, List, Tuple

import requests


DEFAULT_DOWNLOAD_PROXY_LIST = [
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/ultrafast.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt"
]


def is_proxy_working(proxy: str) -> Tuple[str, bool]:
    """Check whether a proxy is working or not

    :param proxy: The url of the proxy
    :return: The url of the proxy and it's status
    """
    try:
        response = requests.get(
            "https://api.myip.com/", proxies={"https": proxy}, timeout=5
        )
        if response.status_code == 200:
            # log.info(f"{proxy} is working")
            return (proxy, True)
    except:
        pass

    # log.info(f"{proxy} is not working")
    return (proxy, False)


def proxy_generator(proxies: List[str]) -> Dict[str, str]:
    """Randomly select a proxy from a list
    
    :param proxies: A list of proxies to select from
    :return: The proxy url at the protocol key (ie: {"https": url})
    """    
    proxy = choice(list(proxies))
    proxy = {"https": proxy}
    return proxy


def download_proxy(download_proxy: str | List[str] = DEFAULT_DOWNLOAD_PROXY_LIST) -> List[str]:
    """Download proxies from the internet

    :param download_proxy: One or multiple url were the proxies are stored, defaults to DEFAULT_DOWNLOAD_PROXY_LIST
    :return: The list of proxies
    """
    if type(download_proxy) == str:
        download_proxy = [download_proxy]
        
    responses = [requests.get(url) for url in download_proxy]
    lines = [response.text.splitlines() for response in responses]
    
    results = []
    list(map(results.extend, lines))

    return results

