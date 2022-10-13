"""
spamcity.config
~~~~~~~~~~~~~~

This module contain all default constant
"""

DEFAULT_DOWNLOAD_PROXY_LIST = [
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/ultrafast.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
]

DEFAULT_COUNTRY = "France"
DEFAULT_CITY = "Rennes"

DEFAULT_USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
]

DEFAULT_LEVEL_OF_CRIME = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_CRIME_INCREASING = ["-2.0", "-2.0", "-2.0", "-2.0"]
DEFAULT_SAFE_ALONE_DAYLIGHT = ["2.0", "2.0", "2.0", "1.0", "1.0"]
DEFAULT_SAFE_ALONE_NIGHT = ["2.0", "2.0", "2.0", "2.0", "2.0"]
DEFAULT_WORRIED_HOME_BROKEN = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_WORRIED_MUGGED_ROBBED = [
    "-2.0",
    "-2.0",
    "-2.0",
    "-2.0",
    "-2.0",
    "-1.0",
    "-2.0",
    "-1.0",
]
DEFAULT_WORRIED_CAR_STOLEN = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_WORRIED_THINGS_CAR_STOLEN = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_WORRIED_ATTACKED = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0"]
DEFAULT_WORRIED_INSULTED = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_WORRIED_SKIN_ETHNIC_RELIGION = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_PROBLEM_DRUGS = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_PROBLEM_PROPERTY_CRIMES = ["-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_PROBLEM_VIOLENT_CRIMES = ["-2.0", "-2.0", "-2.0", "-2.0", "-2.0", "-1.0"]
DEFAULT_PROBLEM_CORRUPTION_BRIBERY = [
    "-2.0",
    "-2.0",
    "-2.0",
    "-2.0",
    "-2.0",
    "-2.0",
    "-1.0",
]
