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
import sys
import traceback
import time
import os
import urllib3


# In[2]:

def remove_after_test(string, remove_char):
    kq=''
    for i in string:
        if i!= remove_char:
            kq+=i
        else:
            break
            return kq
    return kq

def get_tag_config_test(name,config):
    tag = config[name]
    tag_config = [tag['selected_tag'],tag['value'],tag['get_text'],tag['attrs']]
    return tag_config

def get_tag_info_test(r,name,tag_config):
    selected_tag = tag_config[0]
    value = tag_config[1]
    get_text = tag_config[2]
    attrs = tag_config[3]
    info=[]
    
    print(name.upper())
    try:
        tag_list = r.html.find(selected_tag)
        print('Thẻ đã chọn : ',tag_list[0])
    except:
        tag_list =[]
        print('Không tìm được thẻ. Kiểm tra lại selected_tag của phần ',name,'.')
        pass
    
    try:    
        if value!=None:
            tag = [tag_list[value]]
        else :
            tag = tag_list
    except:
        print('Giá trị không hợp lệ. Kiểm tra lại value của phần ',name,'.')
        tag=[]
        pass
    
    try:
        if get_text == 0:
            for i in tag:
                try:
                    info.append(i.attrs[attrs])
                except:
                    print('Không tìm được thuộc tính để lấy giá trị. Kiểm tra lại attrs của phần ',name,'.')
                    pass
        else:
            for j in tag:
                try:
                    info.append(j.text.strip())
                except:
                    print('Không lấy được nội dung thẻ. Kiểm tra lại get_text của phần ',name,'.')
                    pass
    except:
        pass
    unique_info = set(info)
    result = list(unique_info)

    for i in range(len(result)):
        if len(result[i])>888:
            result[i] = remove_after_test(result[i],'\n')

    print('Thông tin lấy được :',result)
    print('\n')
    return result


# In[3]:


"""s = HTMLSession()
r = s.get(productlink)
main_info = config['main_info']
product_name_name='product_name'
product_name_config = get_tag_config_test(product_name_name,main_info)
product_name= get_tag_info_test(r,product_name_name,product_name_config)[0]"""


# In[4]:


def get_product_info_test(productlink,config):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
    
    # Use HTMLSession
    try:
        s = HTMLSession()
        r = s.get(productlink,headers=headers)
    except:
        print('Không tìm được trang web từ link này : ',productlink)
        pass
    
    # Primary shop info
    print('-------------------------------------------------')
    print('THÔNG TIN CƠ BẢN : \n')
    shop_name = config['shop_name']
    print('Tên shop : ',shop_name)
    stylebox_shop_id = config['stylebox_shop_id']
    print('Stylebox_shop_id : ',stylebox_shop_id)
    shop_url = config['shop_url']
    print('Link trang chủ của shop : ',shop_url)
    product_url= productlink
    print('Link sản phẩm : ',product_url)
    scrape_date = datetime.now()
    print('Ngày lấy thông tin sản phẩm : ',scrape_date)
    
    main_info = config['main_info']
    print('-------------------------------------------------')
    print('THÔNG TIN CHÍNH : \n')
    # Get name
    try:
        product_name_name='product_name'
        product_name_config = get_tag_config_test(product_name_name,main_info)
        product_name= get_tag_info_test(r,product_name_name,product_name_config)[0]
    except:
        product_name=''
        pass
    
    # Get original price
    try:
        original_price_name='original_price'
        original_price_config = get_tag_config_test(original_price_name,main_info)
        original_price= get_tag_info_test(r,original_price_name,original_price_config)[0]
    except:
        original_price=''
    
    
    # Get product img links
    try:
        imgs_name='imgs'
        imgs_config = get_tag_config_test(imgs_name,main_info)
        imgs= get_tag_info_test(r,imgs_name,imgs_config)
    except:
        imgs =''
    
    
    # Sub info from here ----------------------------------------------------------------------------
    print('-------------------------------------------------')
    print('THÔNG TIN PHỤ : \n')
    sub_info = config['sub_info']
    # Get review
    try:
        review_name='review'
        review_config = get_tag_config_test(review_name,sub_info)
        review= get_tag_info_test(r,review_name,review_config)
    except:
        review=''
        pass
    
        
    # Get sale price
    try:
        discounted_price_name='discounted_price'
        discounted_price_config = get_tag_config_test(discounted_price_name,sub_info)
        discounted_price= get_tag_info_test(r,discounted_price_name,discounted_price_config)[0]
    except:
        discounted_price =''
        pass
    
    # Get color
    try:
        color_name='color'
        color_config = get_tag_config_test(color_name,sub_info)
        color= get_tag_info_test(r,color_name,color_config)
    except:
        color=''
        pass
    
    # Get description_1
    try:
        description_1_name='description_1'
        description_1_config = get_tag_config_test(description_1_name,sub_info)
        description_1= get_tag_info_test(r,description_1_name,description_1_config)  
    except:
        description_1=''
        pass
    
    # Get description_2
    try:
        description_2_name='description_2'
        description_2_config = get_tag_config_test(description_2_name,sub_info)
        description_2= get_tag_info_test(r,description_2_name,description_2_config)  
    except:
        description_2=''
        pass
   
    
     # Get rating 
    try:
        rating_name='rating'
        rating_config = get_tag_config_test(rating_name,sub_info)
        rating= get_tag_info_test(r,rating_name,rating_config)
    
    except:
        rating =''
      
    
    # Get size
    try:
        size_name='size'
        size_config = get_tag_config_test(size_name,sub_info)
        size= get_tag_info_test(r,size_name,size_config) 
    
    except:
        size= ''
        pass
      
    # List product data forlow data schema
    product_data=[shop_name, stylebox_shop_id, shop_url, product_url, product_name, original_price, imgs, scrape_date, discounted_price, review, size, color, description_1, description_2, rating] 
    return product_data


# In[5]:


__location__ = os.path.abspath('..')
configs_path = os.path.join(__location__, 'Config')

for filename in os.listdir(configs_path):
    print(filename)
    with open(os.path.join(configs_path, filename), encoding='utf-8') as cf:
        try:
            config = json.load(cf)
        except:
            print('Lỗi định dạng file config. Copy lại file mẫu rồi sửa lại.')
            exit()
            
print('Nhập vào link một sản phẩm để kiểm tra.')
productlink = str(input())


# In[ ]:

# In[6]:


test_result = get_product_info_test(productlink,config)
