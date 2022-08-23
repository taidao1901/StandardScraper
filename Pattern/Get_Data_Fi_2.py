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

def get_tag_config(name,config):
    tag = config[name]
    tag_config = [tag['selected_tag'],tag['value'],tag['get_text'],tag['attrs']]
    return tag_config

def remove_after(string, remove_char):
    kq=''
    for i in string:
        if i!= remove_char:
            kq+=i
        else:
            break
            return kq
    return kq

def get_tag_info(r,tag_config):
    selected_tag = tag_config[0]
    value = tag_config[1]
    get_text = tag_config[2]
    attrs = tag_config[3]
    info=[]
    
    try:
        tag_list = r.html.find(selected_tag)
    except:
        tag_list =[]
        pass
    
    try:    
        if value!=None:
            tag = [tag_list[value]]
        else :
            tag = tag_list
    except:
        tag=[]
        pass
    
    try:
        if get_text == 0:
            for i in tag:
                info.append(i.attrs[attrs])
        else:
            for j in tag:
                info.append(j.text.strip())
    except:
        pass
    unique_info = set(info)
    result = list(unique_info)
    
       
    for i in range(len(result)):
        if len(result[i])>888:
            result[i] = remove_after(result[i],'\n')
    return result

# Get value of price
def get_price(price):
    pstr=''
    try:
        for i in price:
            if i.isdigit() or i=='.':
                pstr+=i
    except:
        pass
    if pstr=='':
        pstr='0'   
    try:
        p = float(pstr)
    except:
        pass
    return p

# Check original_price and discounted_price
def check_price(original_price,discounted_price):
    try:
        o_p= get_price(original_price)
        d_p= get_price(discounted_price)
        if o_p<d_p:
            kq=[discounted_price,original_price]
        else:
            kq=[original_price,discounted_price]
    except:
        kq=[original_price,discounted_price]
        pass
    return kq
        
        
# this function use to get one product info.  
def get_product_info(productlink,config):

    # Use HTMLSession
    s = HTMLSession()
    r = s.get(productlink, verify =False)
    
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
        product_name_name='product_name'
        product_name_config = get_tag_config(product_name_name,main_info)
        product_name= get_tag_info(r,product_name_config)[0]
    except:
        product_name=''
        pass
    
    # Get original price
    try:
        original_price_name='original_price'
        original_price_config = get_tag_config(original_price_name,main_info)
        original_price= (get_tag_info(r,original_price_config))[0]
    except:
        original_price=''
    
    
    # Get product img links
    try:
        imgs_name='imgs'
        imgs_config = get_tag_config(imgs_name,main_info)
        imgs= get_tag_info(r,imgs_config)
    except:
        imgs =''
    
    
    # Sub info from here ----------------------------------------------------------------------------
    
    # Get review
    try:
        review_name='review'
        review_config = get_tag_config(review_name,sub_info)
        review= get_tag_info(r,review_config)
    except:
        review=''
        pass
    
        
    # Get sale price
    try:
        discounted_price_name='discounted_price'
        discounted_price_config = get_tag_config(discounted_price_name,sub_info)
        discounted_price= (get_tag_info(r,discounted_price_config))[0]
    except:
        discounted_price =''
        pass
    
    # Get color
    try:
        color_name='color'
        color_config = get_tag_config(color_name,sub_info)
        color= get_tag_info(r,color_config) 
    except:
        color=''
        pass
    
    # Get description_1
    try:
        description_1_name='description_1'
        description_1_config = get_tag_config(description_1_name,sub_info)
        description_1= get_tag_info(r,description_1_config)  
    except:
        description_1=''
        pass
    
    # Get description_2
    try:
        description_2_name='description_2'
        description_2_config = get_tag_config(description_2_name,sub_info)
        description_2= get_tag_info(r,description_2_config)  
    except:
        description_2=''
        pass
   
    
     # Get rating 
    try:
        rating_name='rating'
        rating_config = get_tag_config(rating_name,sub_info)
        rating= get_tag_info(r,rating_config)
    
    except:
        rating =''
      
    
    # Get size
    try:
        size_name='size'
        size_config = get_tag_config(size_name,sub_info)
        size= get_tag_info(r,size_config) 
    
    except:
        size= ''
        pass
      
    # Check price
    price_checked = [original_price,discounted_price]
    try:
        price_checked = check_price(original_price,discounted_price)
    except:
        pass

    # List product data forlow data schema
    product_data=[shop_name, stylebox_shop_id, shop_url, product_url, product_name, price_checked[0], imgs, scrape_date, price_checked[1], review, size, color, description_1, description_2, rating]   
    
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

def web_scraping(config,productlinks, path_file):
    
    print('Số sản phẩm khai thác được: ',len(productlinks))
    
    data=[]
    data.append(['shop_name','stylebox_shop_id','shop_url','product_url','product_name','original_price','imgs','scrape_date','discounted_price','review','size','color','description_1','description_2','rating'])
    
    count=1
    print('Bắt đầu lấy thông tin tất cả sản phẩm :')
    for i in productlinks:
        print(count,' : ',i)
        count+=1
        m=get_product_data(i,config)
        data.append(m)
        
    try:
        day = datetime.today().strftime('%Y-%m-%d')
        csvname = "x. SHOP_ID_"+config['stylebox_shop_id']+"_"+day+".csv"
        jsonname= "x. SHOP_ID_"+config['stylebox_shop_id']+"_"+day+".json"
        csvfilename = os.path.join(path_file,csvname)
        jsonfilename = os.path.join(path_file,jsonname)
    except:
        print("Tên file xuất ra bị sai, chương trình sẽ tự động suất ra kết quả là file result.csv và result.json.")
        csvfilename = os.path.join(path_file,"result.csv")
        jsonfilename = os.path.join(path_file,"result.json")
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




