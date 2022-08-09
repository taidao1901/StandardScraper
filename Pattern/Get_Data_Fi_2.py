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




# Hàm này để xuất file csv
def export_csv(file, kq):
    with open(file , 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in kq:
            writer.writerow(i)
        f.close()
    return ''


# In[3]:




# Hàm này để chuyển file csv qua json
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)  
        
        # Chỗ này xóa phần tử rỗng trong file json 
        #for i in jsonArray:
         #   empty_keys = [k for k,v in i.items() if not v]
          #  for k in empty_keys:
           #     del i[k]
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        
        jsonString = json.dumps( jsonArray, ensure_ascii=False, indent=4).encode('utf8')
        jsonf.write(jsonString.decode('utf-8'))
    return ''


# In[4]:



# Hàm này để suất ra file csv và json
def export_csv_and_json(csvfilename, jsonfilename, data):
    export_csv(csvfilename, data)
    csv_to_json(csvfilename, jsonfilename)
    return ''


# In[6]:


# this function use to get one product info.
def get_product_info(productlink,config):

    # Use HTMLSession
    s = HTMLSession()
    r = s.get(productlink)
    
    # Sub-info
    discounted_price=''
    review=''
    size=''
    color=''
    description_1=''
    description_2=''
    rating=''

    # Main-info from here
    
    # Primary shop info
    shop_name = config['shop_name']
    stylebox_shop_id = config['stylebox_shop_id']
    shop_url = config['shop_url']
    product_url= productlink
    scrape_date = datetime.now()
    main_info = config['main_info']
    sub_info = config['sub_info']
    
    # Get name
    try:
        name = main_info['product_name']
        name_selected_tag = name['selected_tag']
        product_name= r.html.find(name_selected_tag)[0].text.strip()
    except:
        print()
        product_name=''
        pass
    
    # Get original price
    try:
        price = main_info['original_price']
        price_selected_tag = price['selected_tag']
        price_value = price['value']
        original_price = r.html.find(price_selected_tag)[price_value].text.strip()
    except:
        original_price=''
    
    
    # Get product img links
    try:
        price = main_info['original_price']
        price_selected_tag = price['selected_tag']
        price_value = price['value']
        img = main_info['imgs']
        img_selected_tag = img['selected_tag']
        img_attrs = img['attrs']
        img_tags = r.html.find(img_selected_tag)
        link = []
        for i in img_tags:
            try:
                link.append(i.attrs[img_attrs])
            except:
                pass

        links = set(link)
        imgs = list(links)
    except:
        imgs =''
    
    
    # Sub info from here ----------------------------------------------------------------------------
    
    # Get review
    try:
        review= 4/0
    except:
        review=''
        pass
    
        
    # Get sale price
    try:
        sale = sub_info['discounted_price']
        sale_selected_tag = sale['selected_tag']
        sale_value = sale['value']
        discounted_price = r.html.find(sale_selected_tag)[sale_value].text.strip()
    except:
        discounted_price =''
        pass
    
    # Get color
    #try:
    colors = sub_info['color']
    color_selected_tag = colors['selected_tag']
    color_value = colors['value']
    color_get_text = colors['get_text']
    color_attrs = colors['attrs']
    colorlist = r.html.find(color_selected_tag)
    color=[]
    for i in colorlist:
        if color_get_text ==1:
            color.append(i.text)
        else:
            color.append(i.attrs[color_attrs])
    print('hahaha',color)
        
    #except:
    #    color=''
     #   pass
    
    # Get description_1
    try:
        des1 = sub_info['description_1']
        des1_selected_tag = des1['selected_tag']
        des1_get_text = des1['get_text']
        des1_attrs = des1['attrs']
        description_1= []
        content = r.html.find(des1_selected_tag)
        for i in content:
            if des1_get_text ==1:
                description_1.append(i.text)
            else:
                description_1.append(i.attrs[des1_attrs])
            #print(description_1)
    except:
        description_1=''
        pass
    
    # Get description_2
    try:
        des2 = sub_info['description_2']
        des2_selected_tag = des2['selected_tag']
        des2_get_text = des2['get_text']
        des2_attrs = des2['attrs']
        description_2= []
        content = r.html.find(des2_selected_tag)
        for i in content:
            if des2_get_text ==1:
                description_2.append(i.text)
            else:
                description_2.append(i.attrs[des2_attrs])
            #print(description_1)
    except:
        description_2=''
        pass
   
    
     # Get rating 
    try:
        rating= 4/0
    
    except:
        rating =''
      
    
    # Get size
    try:
        sizes = sub_info['size']
        sizes_selected_tag = sizes['selected_tag']
        sizes_get_text = sizes['get_text']
        sizes_attrs = sizes['attrs']
        
        sizes_value = sizes['value']
        si = r.html.find(sizes_selected_tag) 
        size = []
        for i in si:
            try:
                size.append(i.attrs[sizes_attrs])
            except:
                pass
        k = set(size)
        size = list(k)
        #print(size)
    
    except:
        size= ''
        pass
      
    # List product data forlow data schema
    product_data=[shop_name, stylebox_shop_id, shop_url, product_url, product_name, original_price, imgs, scrape_date, discounted_price, review, size, color, description_1, description_2, rating]   
    
    return product_data
        


# In[7]:




# Hàm này để lấy data từ 1 sản phẩm.

def get_product_data(productlink,config):
    try:    
        data =get_product_info(productlink,config)
    except:
        data = ''
        print('Tên hoặc thông tin điền vào file json bị sai.')
    return data
    


# In[8]:




# Hàm này để lấy data từ nhiều sản phẩm.

def web_scraping(config,productlinks):
    
    print('Số sản phẩm khai thác được: ',len(productlinks))
    
    data=[]
    data.append(['shop_name','stylebox_shop_id','shop_url','product_url','product_name','original_price','imgs','scrape_date','discounted_price','review','size','color','description_1','description_2','rating'])
    
    count=1
    for i in productlinks:
        #print(count,' : ',i)
        count+=1
        m=get_product_data(i,config)
        data.append(m)
    
    csvfilename = config['csvfilename']
    jsonfilename = config['jsonfilename']
    export_csv_and_json(csvfilename, jsonfilename, data)
    print('Oki we done :))')
    return ''


# In[9]:


#with open("config.json", encoding='utf-8') as js:
    #config = json.load(js)


# In[10]:


#productlinks=['https://chodole.com/products/ao-thun-unisex-cotton-in-hinh-smile-and-rise']


# In[11]:




#web_scraping(config,productlinks)


# In[ ]:




