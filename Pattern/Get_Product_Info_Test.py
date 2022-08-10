# %%
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

# %%
def get_product_info_test(productlink,config):
    # Use HTMLSession
    try:
        s = HTMLSession()
        r = s.get(productlink)
    except:
        print('Link nhập vào bị sai.')
        exit()
    print('Các thẻ đã chọn :\n')
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
        product_name_tag= r.html.find(name_selected_tag)[0]
        print('product_name : ',product_name_tag)
        product_name = product_name_tag.text.strip()
    except:
        print('selected_tag trong phần product_name bị sai .')
        product_name=''
        pass
    
    # Get original price
    print('\n')
    try:
        price = main_info['original_price']
        price_selected_tag = price['selected_tag']
        price_value = price['value']
        original_price_list = r.html.find(price_selected_tag)
        original_price_tag= original_price_list[price_value]
        print('original_price : ',original_price_tag)
        original_price= original_price_tag.text.strip()
    except:
        print('selected_tag hoặc value trong phần original_price bị sai .')
        original_price=''
    
    
    # Get product img links
    print('\n')
    try:
        img = main_info['imgs']
        img_selected_tag = img['selected_tag']
        img_attrs = img['attrs']
        img_tags = r.html.find(img_selected_tag)
        print('img_tags : ',img_tags[0])
        link = []
        for i in img_tags:
            link.append(i.attrs[img_attrs])

        links = set(link)
        imgs = list(links)
    except:
        print('selected_tag trong phần imgs bị sai .')
        imgs =''
    
    
    # Sub info from here ----------------------------------------------------------------------------
    
    # Get review
    try:
        review= 4/0
    except:
        review=''
        pass
    
        
    # Get sale price
    print('\n')
    try:
        sale = sub_info['discounted_price']
        sale_selected_tag = sale['selected_tag']
        sale_value = sale['value']
        discounted_price_list = r.html.find(sale_selected_tag)
        discounted_price_tag = discounted_price_list[sale_value]
        print('discounted_price : ',discounted_price_tag[0])
        discounted_price = discounted_price_tag.text.strip()
    except:
        discounted_price =''
        print('selected_tag hoặc value trong phần discounted_price chưa có hoặc bị sai .')
        pass
    
    # Get color
    print('\n')
    try:
        colors = sub_info['color']
        color_selected_tag = colors['selected_tag']
        color_value = colors['value']
        color_get_text = colors['get_text']
        color_attrs = colors['attrs']
        colorlist = r.html.find(color_selected_tag)
        print('color_list : ', colorlist[0])
        color=[]
        for i in colorlist:
            if color_get_text ==1:
                color.append(i.text)
            else:
                color.append(i.attrs[color_attrs])    
    except:
        print('selected_tag trong phần color chưa có hoặc bị sai .')
        color=''
        pass
    
    
    # Get description_1
    print('\n')
    try:
        des1 = sub_info['description_1']
        des1_selected_tag = des1['selected_tag']
        des1_get_text = des1['get_text']
        des1_attrs = des1['attrs']
        description_1= []
        content = r.html.find(des1_selected_tag)
        print('description_1 : ',content[0])
        for i in content:
            if des1_get_text ==1:
                description_1.append(i.text)
            else:
                description_1.append(i.attrs[des1_attrs])
            #print(description_1)
    except:
        print('selected_tag trong phần description_1 chưa có hoặc bị sai .')
        description_1=''
        pass
    
    # Get description_2
    print('\n')
    try:
        des2 = sub_info['description_2']
        des2_selected_tag = des2['selected_tag']
        des2_get_text = des2['get_text']
        des2_attrs = des2['attrs']
        description_2= []
        content = r.html.find(des2_selected_tag)
        print('description_2 : ',content[0])
        for i in content:
            if des2_get_text ==1:
                description_2.append(i.text)
            else:
                description_2.append(i.attrs[des2_attrs])
            #print(description_1)
    except:
        print('selected_tag trong phần description_2 chưa có hoặc bị sai .')
        description_2=''
        pass
   
    
     # Get rating 
    try:
        rating= 4/0
    
    except:
        rating =''
      
    
    # Get size
    print('\n')
    try:
        sizes = sub_info['size']
        sizes_selected_tag = sizes['selected_tag']
        sizes_get_text = sizes['get_text']
        sizes_attrs = sizes['attrs']
        sizes_value = sizes['value']
        si = r.html.find(sizes_selected_tag) 
        print('size : ', si[0])
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
        print('selected_tag trong phần size chưa có hoặc bị sai .')
        size= ''
        pass
      
    # List product data forlow data schema
    product_data=[shop_name, stylebox_shop_id, shop_url, product_url, product_name, original_price, imgs, scrape_date, discounted_price, review, size, color, description_1, description_2, rating]   
    
    print('------------------------------------------------------')
    print('Dữ liệu lấy được : \n ')
    name = ['shop_name', 'stylebox_shop_id', 'shop_url', 'product_url', 'product_name', 'original_price', 'imgs', 'scrape_date', 'discounted_price', 'review', 'size', 'color', 'description_1', 'description_2', 'rating']
    # Sub info từ phẩn tử thứ 8 -> discounted_price.
    print('Thông tin chính : ')
    for i in range(len(name)):
        if i==7:
            print('\n')
            print('Thông tin phụ : ')
        tittle= name[i]
        result= product_data[i]
        print(tittle ,' : ',result)
    return product_data

# %%
__location__ = os.path.abspath('..')
print(__location__)
configs_path = os.path.join(__location__, 'Config')

for filename in os.listdir(configs_path):
    with open(os.path.join(configs_path, filename), encoding='utf-8') as cf:
        try:
            config = json.load(cf)
        except:
            print('Lỗi định dạng file config. Copy lại file mẫu rồi sửa lại.')
            exit()
            
print('Nhập vào link một sản phẩm để kiểm tra.')
productlink = str(input())

# %%
test_result = get_product_info_test(productlink,config)


