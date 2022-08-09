import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
pages = 3
url_list = []
raw_urls = []
xyz = 0
Current_Entry = ''
Current_Directory = os.getcwd()
Save_Dir = os.environ['USERPROFILE'] + '/Desktop/Quarks_MP4s/'
if not (os.path.exists(Save_Dir)):
    os.makedirs(Save_Dir)
#if not os.path.exists(Current_Directory+"/SavedLinks.txt"):
Open_File = open(Current_Directory+"/SavedLinks.txt", 'w')
options = webdriver.ChromeOptions()
PATH = Current_Directory+"/chromedriver.exe"
prefs = {"download.default_directory" : os.environ['USERPROFILE'] + '\Desktop\Quarks_MP4s'} #(os.environ['USERPROFILE'] + '\Desktop'  #
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
Open_File = open(Current_Directory+"/SavedLinks.txt", 'r+') #OpensFiles #r W
def Download_File(x,Use_Name):
    urllib.request.urlretrieve(x, (Save_Dir + Use_Name+'.mp4'))

def Use_File(x):
    Open_File = open(Current_Directory+"/SavedLinks.txt", x)
    return Open_File

def Add_Entry(x):
    Use_File('a+').write(x + '\n')


if 'https://www.podbean.com/site/EpisodeDownload/DIR14237588ICA6A' not in Open_File.read():
    Use_File('a+').write('\n' + 'https://www.podbean.com/site/EpisodeDownload/DIR14237588ICA6A')
    Use_File('a+').write('\n' + 'https://www.podbean.com/site/EpisodeDownload/DIR1430B5166DJS8')
time.sleep(0.2)

##print(Use_File('r+').read())

driver.get("https://www.podbean.com/podcast-detail/abe48-3f1e/Quirks-and-Quarks-from-CBC-Radio-Podcast")
time.sleep(2)
ElementsOnPage = (driver.find_elements(By.CLASS_NAME, "download"))

def Main_Loop():
    ElementsOnPage = (driver.find_elements(By.CLASS_NAME, "download"))
    time.sleep(0.2)

    for i in ElementsOnPage:
        i = i.get_attribute("href")
        if i not in Use_File('r').read():
            raw_urls.append(i)
            time.sleep(0.2)


while xyz < pages:

    Main_Loop()
    time.sleep(3)
    if xyz < pages-1:
        driver.find_element(By.XPATH, "//li[@class='next']//child::a").click()
    time.sleep(3)
    xyz+=1

for i in raw_urls:
    print(i)
    if i not in Use_File('r').read():
        Add_Entry(i)
        driver.get(i)
        time.sleep(1)
        Append_Me = driver.find_element(By.XPATH, "//a[@class='btn btn-ios download-btn']").get_attribute("href")
        Use_Name = driver.find_element(By.XPATH,"//img[@class ='logo-img']").get_attribute("alt")
        url_list.append(Append_Me)
        Use_Name = ' '.join(Use_Name.split()[:5]) #space for words
        Download_File(Append_Me, Use_Name)
        time.sleep(0.3)

