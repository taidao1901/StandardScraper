#!/usr/bin/env python
# coding: utf-8

# In[1]:




from datetime import datetime

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import csv
import json


# In[2]:


def get_html_source_test(productlink,config):
    isdynamic = config['isdynamic']
    
    if isdynamic == 0:
        try:
            r = requests.get(productlink)
            soup = BeautifulSoup(r.text,'lxml')
            html_soure=soup.prettify()
        except:
            html_soure =''
            print('Link sản phẩm bị sai.')
    
    else:
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
            browser.get(productlink)
            html_soure = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        except:
            html_soure =''
            print('Link sản phẩm bị sai.')
    #print(html_soure)
    return html_soure
    


# In[3]:




# Dùng hàm này để lấy thông tin sản phẩm
def get_product_info_test(html_soure,productlink,config):
    
    soup = BeautifulSoup(html_soure,'lxml')
    
    # Lấy các thông tin chung như tên shop, id ...
    product_url = productlink
    print('Link : ',product_url)

    # Thông tin phụ sẽ xử lý sau.
    discounted_price=''
    review=''
    size=''
    color=''
    description_1=''
    description_2=''
    rating=''
    
    main_info = config['main_info']
    
    #Lấy tên sản phẩm
    name = main_info['product_name']
    name_tag = name['name_tag']
    name_class = name['name_class']
    try:
        product_name= soup.find(name_tag, class_=name_class)
        print('Thẻ tên : ',product_name)
        print('Tên sản phẩm : ',product_name.text.strip())
    except:
        product_name=''
        print('\n ------------------------------------------------------ \n')
        print('name_tag hoặc name_class bị sai. ')
    print('\n ------------------------------------------------------ \n')
        
        

    #Lấy giá hiện tại
    price = main_info['original_price']
    price_tag = price['original_price_tag']
    price_class = price['original_price_class']
    is_woocommerce = price['is_woocommerce']
    woocommerce_value = price['woocommerce_value']
    if is_woocommerce=='0':
        try:
            original_price = soup.find(price_tag, class_=price_class)
            print('Thẻ giá :',original_price)
            print('Giá sản phẩm : ', original_price.text.strip())
        except:
            original_price = ''
            print('\n ------------------------------------------------------ \n')
            print('price_tag hoặc price_class bị sai. ')
    else:
        try:
            s = HTMLSession()
            r = s.get(productlink)
            original_price = r.html.find('span.woocommerce-Price-amount.amount bdi')[int(woocommerce_value)].full_text
            print('Giá sản phẩm : ', original_price)
        except: 
            original_price = ''
            print('\n ------------------------------------------------------ \n')
            print('Giá trị woocommerce_value bị sai, hãy thử một số khác từ 0 -> 2 .')
    print('\n ------------------------------------------------------ \n')
        
    # Lấy ảnh sản phẩm 
    img = main_info['imgs']
    have_parent = img['have_parent']
    img_tag = img['img_tag']
    img_class = img['img_class']
    img_parent_tag = img['img_parent_tag']
    img_parent_class = img['img_parent_class']
    tag_attribute = img['img_tag_attribute']
    
    if have_parent == 0:
        try:
            img = soup.find_all(img_tag, class_=img_class)
            print('Các thẻ ảnh :')
            for t in img :
                print(t)
                print('\n')
            link = [i[tag_attribute] for i in img]
            links = set(link)
            imgs = list(links)
            print('Link lấy được :')
            for k in imgs:
                print(k)
                
        except:
            imgs =''
            print('\n ------------------------------------------------------ \n')
            print('img_tag hoặc img_class hoặc tag_attribute bị sai. ')
    else:
        link=[]
        tag =[]
        try:
            img = soup.find_all(img_parent_tag, class_= img_parent_class)
            print('Thẻ cha lấy được : \n')
            print(img[0])
            print('\n')
            
            for i in img:
                m = i.find(img_tag, class_= img_class)
                if m != None:
                    tag.append(m)
            print('Thẻ con lấy được :')
            print(tag[0])
            print('\n')
        except:
            print('\n ------------------------------------------------------ \n')
            print('img_tag hoặc img_class hoặc img_child_tag hoặc img_child_class bị sai.')
        for j in tag:
            try:
                ha= j[img_tag_attribute]
                link.append(ha)
            except:
                pass
    if link==[] :
        print('\n ------------------------------------------------------ \n')
        print('tag_attribute bị sai.')
        print('\n ------------------------------------------------------ \n')
    links = set(link)
    imgs = list(links)
    print('Các link ảnh lấy được :')
    for m in imgs :
        print(m)

    
    return ''
        


# In[4]:




# Hàm này để kiểm tra thông tin lấy từ 1 sản phẩm.
def Test_Data(productlink,config):
    html_soure=get_html_source_test(productlink,config)
    data =get_product_info_test(html_soure,productlink,config)
    return ''
