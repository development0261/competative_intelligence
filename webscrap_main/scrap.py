
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from sys import platform
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import time
import requests
import json
import random

import os




# Setup
cred = credentials.Certificate("competitive-intelligence-4a07d-firebase-adminsdk-s6a5i-2a74042bdc.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


def get_rand():
    return random.uniform(2.0, 2.9)

def scrape(country_name,search_keyword):
    # print("+++++++++++++++++++++++++++",platform)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    website = 'https://www.facebook.com/ads/library/'
    # print("++++++++++++++",platform)
    # if platform =="win32":
    #     path = 'chromedriver.exe' 
    # else:
    #     path= "chromedriver"

    # # # driver initialization 
    # driver = webdriver.Chrome(path)
    # open Google Chrome with chromedriver
    driver.get(website)
    # time to wait(in sec) till page gets loaded 
    time.sleep(get_rand())
    insert_data = driver.find_elements(By.CLASS_NAME, 'j1p9ls3c.hmv1tv54.tes86rjd.kr054jk4.i6uybxyu.qm54mken.lq84ybu9.hf30pyar.oshhggmv.nnmaouwa.aeinzg81')
    # selecting the country 
    # country = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div') 
    country=insert_data[0]
    country.click()
    time.sleep(get_rand())
    
    search_country = driver.find_element(By.CLASS_NAME, '_58al')
    # search_country=driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/input[1]')
    search_country.click()
    time.sleep(get_rand())
    search_country.send_keys(country_name)
    time.sleep(get_rand())
    
    select_country= driver.find_element(By.CLASS_NAME, 'j1p9ls3c.hmv1tv54.tes86rjd.kr054jk4.i6uybxyu.qc5lal2y.l4uc2m3f.gh25dzvf.t7p7dqev.aeinzg81.cgu29s5g')
    # select_country=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]')
    select_country.click()
    time.sleep(get_rand())

    # selecting the ads type 
    # ads_type = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div') 
    ads_type=insert_data[1]
    ads_type.click()
    time.sleep(get_rand())
    # all_ads=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div[1]')
    all_ads= driver.find_element(By.CLASS_NAME, 'j1p9ls3c.hmv1tv54.tes86rjd.kr054jk4.i6uybxyu.qc5lal2y.ztn2w49o.nnmaouwa.aeinzg81')
    all_ads.click()
    time.sleep(get_rand())
    # Search specific key word
    Search_key= driver.find_element(By.CLASS_NAME, 'f5m7p0br.iwso50tu.ggolc4ur.js4msrqk.p5mefues.j32recxq.j94dm2s7.trbvugp6.kxpv3n1v.aglvbi8b.c61n2bf6.sds2k780.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.icdlwmnq.lq84ybu9.hf30pyar.q46jt4gp.r227ecj6.r5g9zsuq.gt60zsk1.om3e55n1.oshhggmv.mfclru0v.j7qd3pol')

    # Search_key=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/input')
    time.sleep(get_rand())
    Search_key.send_keys(search_keyword)
    time.sleep(get_rand())
    Search_key.send_keys(Keys.ENTER)
    time.sleep(get_rand())

    for i in range(1,25):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)

    
    # _9b9p _99s6- div class

    content = driver.find_elements(By.CLASS_NAME, '_99s5')
    return content

def data_fetch(content):
    scrapitem_list=[]
    i=0
    for elements in content:
        try:
            try:
                obj_html_str = elements.get_attribute('innerHTML')

                soup = BeautifulSoup(obj_html_str, "html.parser")
            except:
                print("HTML object or Soup error")
            
            try:
                ads_owner_idlink_full = soup.find(href=True)
                ads_owner_idlink=ads_owner_idlink_full['href']
            except:
                print("link getting error")
            try:
                data = elements.text.split('\n')
                sp_index = elements.text.split('\n').index("Sponsored")

                ads_owner_name=data[int(sp_index)-1]
            except:
                print(" data split error")
        
            ads_status=data[0] 
    #         print(type(data[1]))
            try:
                
                ads_date_full=data[1].split("-")
                
                if len(ads_date_full)==1:
                    
                    ads_date=(ads_date_full[0])[19:]
                   
                else:
                    ads_date=ads_date_full[0]
            except:
                print("ads_date error")
            
            try:

                if "ID:" in data[3]:
                    ads_id=data[3][3:]
                elif "ID:" in data[4]:
                    ads_id=data[4][3:]
                elif "ID:" in data[5]:
                    ads_id=data[5][3:]
                elif "ID:" in data[6]:
                    ads_id=data[6][3:]
                else:
                    pass
            except:
                print("ID Error")
        

            d={"ads_date":str(ads_date),
                "ads_status":str(ads_status),
                "ads_id":int(ads_id),
                "ads_owner_name":str(ads_owner_name),
                "ads_owner_idlink":str(ads_owner_idlink)
            }

            scrapitem_list.append(d)
        except:
            print(i)
            print("error in this iteration")
            break
        i=i+1

    return scrapitem_list 


def messaging(message,token_list):
    serverToken = 'AAAA2lYEqXg:APA91bFVm5S5o7DY87Y1He-DAad4ePqOPQQttObJRkUbjogm1DJR7otEX6R0DBkBMVGnn7d7AvzVPl_R-S6SC1E3KMkzg0yHd6fDzNfb6QYzkMnoawhWxX4Alga_n_V07VCFOtwk-a4i'
    deviceToken = token_list

    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
          }

    body = {
              'notification': {'title': 'New Record Found',
                                'body': message
                                },
              "registration_ids":deviceToken,
              'priority': 'high',
            #   'data': dataPayLoad,
            }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(message,response.status_code)
    print(response.json())


def data_insert(search_keyword,scrapitem_list,token_list):
    cred = credentials.Certificate("competitive-intelligence-4a07d-firebase-adminsdk-s6a5i-2a74042bdc.json")

    try:
        app = firebase_admin.initialize_app(cred)
        db=firestore.client()
    except:
        db=firestore.client()
  
    for batched_data in scrapitem_list:
        try:
            print("!")
            doc_id=str(batched_data["ads_id"])
            print("!!")
            batch_status=str(batched_data["ads_status"])
            print("!!!")
            collection_name=str(search_keyword)
            print("!!!!")
            collection_ref = db.collection(collection_name)
            print("-------------------",collection_ref)
            col = collection_ref.get()
            print("+++++++++++++++++++")
            if len(col)==0:
                print("Inside if ")
                doc_ref = db.collection(collection_name).document(doc_id)
                doc_ref.set(batched_data)
            else:
                print("Inside else ")
                doc_ref = db.collection(collection_name).document(doc_id)
        except:
             print("connection error")
            

        doc = doc_ref.get()
        try:
            if doc.exists:
                doc_status=doc.to_dict()['ads_status']
                if doc_status=="Active" and batch_status=="Inactive":
                    messaging("this ad is inactive now",token_list)
                    doc_ref.update({"ads_status":"Inactive"})
                elif doc_status=="Inactive" and batch_status=="Active":
        #             print("this ad is inactive now")
                    messaging("this ad is Active now",token_list)
                    doc_ref.update({"ads_status":"Active"})
                elif doc_status=="Inactive" and batch_status=="Active":
                    print("this is still Inactive and in database")
                else:
                    print("this is still active and in database")
            else:
                if batch_status=="Inactive":
                    print("ID NOT EXISTs----------this ad is inactived and not needed")
                else:
                    doc_ref.set(batched_data)
                    messaging("new ad is inserted",token_list)
        except:
            print("record access error")
    
