#!/usr/bin/env python
# coding: utf-8

# In[13]:


from datetime import datetime

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[17]:


# Hàm này để lấy file html của trang web sản phẩm
def get_html_source(productlinks,isdynamic):
    if isdynamic!=1:
        r = requests.get(productlinks)
        soup = BeautifulSoup(r.text,'lxml')
        html_soure=soup.prettify()
    
    else:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
        browser.get(productlinks)
        html_soure = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    
    return html_soure
    


# In[ ]:


# Sử dụng hàm này lấy giá sản phẩm hoặc các thông tin khác được bọc trong class webwoocommerce
def get_webwoocommerce_value(productlinks):
    
    s = HTMLSession()
    r = s.get(productlinks)
    # Số 2 trong dòng này có thể sửa thành số 1 hoặc 0 nếu code không chạy
    price = r.html.find('span.woocommerce-Price-amount.amount bdi')[0].full_text   
    return price


# In[18]:


# Dùng hàm này để lấy thông tin sản phẩm
def get_product_info(html_soure,productlinks):
    
    soup = BeautifulSoup(html_soure,'lxml')

    kq=[]
    
    #Dòng này để lấy tên sản phẩm, SỬA CODE Ở ĐÂY
    name = soup.find('h1').text.strip()
    kq.append(name)
   
    
    
    # Dòng này để lấy giá, SỬA CODE Ở ĐÂY
    price = get_webwoocommerce_value(productlinks).strip()
    kq.append(price)
    
    # Dòng này để thêm link sản phẩm, không sửa.
    kq.append(productlinks)
    
    # Dòng này để lấy link ảnh, SỬA CODE Ở ĐÂY.
    img = soup.find_all('div', class_="s-img")
    link = [i['data-bg'] for i in img]
    #print(len(link))
    #print(link)
    
    
    #Tránh lặp hình ảnh trong list, không sửa chỗ này.
    links=set(link)
    linkfinal = list(links)
    
    
    
    for i in linkfinal:
        kq.append(i)
    
    return kq
        


# In[52]:


# Nhập thông tin chung của shop ở đây .

shop_name =''
stylebox_shop_id =''
shop_url =''

now=now = datetime.now()
scrap_day = now.strftime("%m/%d/%Y %H:%M:%S")


# In[53]:


tt=[shop_name,stylebox_shop_id,shop_url,scrap_date]

def get_data(productlinks,isdynamic,tt=tt):
    html_soure=get_html_source(productlinks,isdynamic)
    data =get_product_info(html_soure,productlinks)
    
    data.reverse()
    for i in tt:
        data.append(i)
    data.reverse()
    return data


# In[ ]:




