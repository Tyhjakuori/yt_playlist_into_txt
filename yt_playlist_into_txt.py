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
    """Parsing page source and categorizing videos by title to different files + sorting them"""
    with open("source.html", 'r') as sorsa1:
        soup = BeautifulSoup(sorsa1, features="lxml")
    albumit = open("albums.txt", 'w')
    kaik_ept = open("eps.txt", 'w')
    demoja = open("demot.txt", 'w')
    splits = open("splits.txt", 'w')
    kaikki = open("all.txt", 'w')
    albums = "full album"
    albums1 = "official album"
    ept = "full ep"
    split = "full split"
    demo = "full demo"
    lista = soup.find_all(id="video-title")

    for lin in lista:
        linkit = lin.get('title').lower() + '\n'
        if albums in linkit or albums1 in linkit:
            albumit.write(linkit)
        if ept in linkit:
            kaik_ept.write(linkit)
        if split in linkit:
            splits.write(linkit)
        if demo in linkit:
            demoja.write(linkit)
        kaikki.write(linkit)

    albumit.close()
    kaik_ept.close()
    splits.close()
    demoja.close()
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

    with open("albums.txt", 'r') as albums2:
        lines = albums2.readlines()
        lines2 = jarjesta(lines)
        with open("albums_sorted.txt", 'w') as kai1:
            for line in lines2:
                kai1.write(line)
    albums2.close()
    kai1.close()

    with open("eps.txt", 'r') as eps2:
        lines = eps2.readlines()
        lines2 = jarjesta(lines)
        with open("eps_sorted.txt", 'w') as kai2:
            for line in lines2:
                kai2.write(line)
    eps2.close()
    kai2.close()

    with open("demot.txt", 'r') as demo1:
        lines = demo1.readlines()
        lines2 = jarjesta(lines)
        with open("demot_sorted.txt", 'w') as kai3:
            for line in lines2:
                kai3.write(line)
    demo1.close()
    kai3.close()

    with open("splits.txt", 'r') as splits2:
        lines = splits2.readlines()
        lines2 = jarjesta(lines)
        with open("splits_sorted.txt", 'w') as kai4:
            for line in lines2:
                kai4.write(line)
    splits2.close()
    kai4.close()


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
