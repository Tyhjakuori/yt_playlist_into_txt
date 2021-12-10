import re
import time
from time import sleep
from random import choice
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def jarjesta(arvo):
    """Sorts the text files"""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    arvo.sort(key = alphanum_key)
    return arvo

def random_headers():
    """Returns random choice user-agent"""
    return choice(agents)
    
def nuku():
    """Sleeps for random time and returns"""
    aika = range(3,9)
    time.sleep(choice(aika))
    return
    
def write_files():
    """Parsing page source and writing videos by title into a file + sorting it"""
    with open("source.html", 'r') as sorsa1:
        soup = BeautifulSoup(sorsa1, features="lxml")
    kaikki = open("all.txt", 'w')
    lista = soup.find_all(id="video-title")

    for lin in lista:
        linkit = lin.get('title').lower() + '\n'
        kaikki.write(linkit)

    kaikki.close()
    sorsa1.close()
    
    with open("all.txt", 'r') as kaikki1:
        lines = kaikki1.readlines()
        lines2 = jarjesta(lines)
        with open("all_sorted.txt", 'w') as kai:
            for line in lines2:
                kai.write(line)
    kaikki1.close()
    kai.close()


# Defining random user-agents
agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

print("Insert what is after this 'https://www.youtube.com/playlist?list='")
playlist_id = input("Playlists id: ")
url = "https://www.youtube.com/playlist?list="+playlist_id

# Defining capabilities
capabilities = DesiredCapabilities.FIREFOX
capabilities['platform'] = "LINUX"
#capabilities['platform'] = "WINDOWS"

# Defining options
options = Options()
#options.add_argument('--headless')
options.add_argument("window-size=1400,600")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.overdrive", random_headers())

driver = webdriver.Firefox(capabilities=capabilities, options=options)
driver.get(url)
nuku()

# Clicking i agree button
nothanks = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
nothanks.click()
nuku()

i = 1
for i in range(30):
    elm = driver.find_element(By.TAG_NAME, 'html')
    elm.send_keys(Keys.END)
    time.sleep(1)
    i += 1
    print(i)
	
sorsa = driver.page_source
file1 = open("source.html", "w")
file1.write(sorsa)
file1.close()
nuku()
driver.quit()

write_files()

