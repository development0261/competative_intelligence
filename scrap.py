
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from selenium.webdriver.common.by import By
import random
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("competitive-intelligence-4a07d-firebase-adminsdk-s6a5i-2a74042bdc.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


def get_rand():
    return random.uniform(2.0, 2.9)

def scrape():
    website = 'https://www.facebook.com/ads/library/'
    path = 'F:\company projects\web_scapping\webscrap\chromedriver' 

    # driver initialization 
    driver = webdriver.Chrome(path)
    # open Google Chrome with chromedriver
    driver.get(website)
    # time to wait(in sec) till page gets loaded 
    time.sleep(get_rand())

    # selecting the country 
    country = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div') 
    country.click()
    time.sleep(get_rand())
    search_country=driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/input[1]')
    search_country.click()
    time.sleep(get_rand())
    search_country.send_keys("India")
    time.sleep(get_rand())
    select_country=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]')
    select_country.click()
    time.sleep(get_rand())

    # selecting the ads type 
    ads_type = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div') 
    ads_type.click()
    time.sleep(get_rand())
    all_ads=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div[1]')
    all_ads.click()
    time.sleep(get_rand())

    # Search specific key word
    Search_key=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/input')
    time.sleep(get_rand())
    Search_key.send_keys("flower")
    time.sleep(get_rand())
    Search_key.send_keys(Keys.ENTER)
    time.sleep(get_rand())

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(60)
    
    # _9b9p _99s6- div class

    content = driver.find_elements(By.CLASS_NAME, '_99s5')
    return content

def data_fetch(content):
    import json
    k = []
    i=0
    for elements in content:
        try:
            print(i)
            # print("--------------------------------!!")
            obj_html_str = elements.get_attribute('innerHTML')
            soup = BeautifulSoup(obj_html_str, "html.parser")

            ads_owner_idlink_full = soup.find(href=True)
            ads_owner_idlink=ads_owner_idlink_full['href']
            data = elements.text.split('\n')
            sp_index = elements.text.split('\n').index("Sponsored")
            ads_owner_name=data[int(sp_index)-1]
        
            # print("--------------------------------")
            string=elements.text
            
            x=[x for x in string .split("\n")]
    #         k.append(x)
            # print(x)
            ads_status=x[0]
            if ads_status=="Active":
                ads_date_text=(x[1])[19:]
                
                ads_date= datetime.strptime(ads_date_text,"%d %b %Y").date()
                try:
                    ads_id_check=str((x[3])[:2])
                    # ads_owner_name=str(x[(3+3)][:3])
                    if ads_id_check=="ID":
                        ads_id=int((x[3])[3:])

                        
                except:
                    ads_id_check=str((x[4])[:2])
                    if ads_id_check=="ID":
                        ads_id=int((x[4])[3:])
                                        
            else:
                ads_date_text=(x[1])[:11]
                ads_date= datetime.strptime(ads_date_text,"%d %b %Y").date()
                try:
                    ads_id_check=str((x[3])[:2])
                    if ads_id_check=="ID":
                        ads_id=int((x[3])[3:])                                     
                except:
                    ads_id_check=str((x[4])[:2])
                    if ads_id_check=="ID":
                        ads_id=int((x[4])[3:])
                        
    #         print(ads_date, ads_status,ads_id,ads_owner_name,ads_owner_idlink)
    #                     print("------------------- Inside InActive except----------")
            d={"ads_date":str(ads_date),
                "ads_status":str(ads_status),
                "ads_id":int(ads_id),
                "ads_owner_name":str(ads_owner_name),
                "ads_owner_idlink":str(ads_owner_idlink)
            }
            k.append(d)
            i=i+1
            time.sleep(get_rand())
        except:
            print("End of the recordes")
            i=i+1
            break
    return k 


content=scrape()
data_for_insert=data_fetch(content)
print(data_for_insert)
    
