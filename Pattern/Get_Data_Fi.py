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


# In[5]:


# Shop Sobie
#productlinks= ['https://sobie.vn/products/ao-boi-nu-tay-dai-dark-ocean','https://sobie.vn/products/ao-boi-nu-tay-dai-dark-sea','https://sobie.vn/products/ao-boi-nu-tay-ngan-short-sleeve-maple']

# Shop ananas
#productlinks2 = ['https://ananas.vn/product-detail/av00135/','https://ananas.vn/product-detail/av00104/','https://ananas.vn/product-detail/av00105/']


# In[6]:


# Hàm này để lấy file html của trang web sản phẩm
def get_html_source(productlink,config):
    isdynamic = config['isdynamic']
    
    if isdynamic == '0':
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
    


# In[7]:


# Dùng hàm này để lấy thông tin sản phẩm
def get_product_info(html_soure,productlink,config):
    
    soup = BeautifulSoup(html_soure,'lxml')
    
    # Lấy các thông tin chung như tên shop, id ...
    shop_name = config['shop_name']
    stylebox_shop_id= config['stylebox_shop_id']
    shop_url=config['shop_url']
    product_url = productlink
    scrape_date = datetime.now()

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
        product_name= soup.find(name_tag, class_=name_class).text.strip()
    except:
        product_name=''
        print('name_tag hoặc name_class bị sai. ')
        

    #Lấy giá hiện tại
    price = main_info['original_price']
    price_tag = price['original_price_tag']
    price_class = price['original_price_class']
    is_woocommerce = price['is_woocommerce']
    woocommerce_value = price['woocommerce_value']
    if is_woocommerce=='0':
        try:
            original_price = soup.find(price_tag, class_=price_class).text.strip()
        except:
            original_price = ''
            print('price_tag hoặc price_class bị sai. ')
    else:
        try:
            s = HTMLSession()
            r = s.get(productlink)
            original_price = r.html.find('span.woocommerce-Price-amount.amount bdi')[int(woocommerce_value)].full_text
        except: 
            original_price = ''
            print('Giá trị woocommerce_value bị sai, hãy thử một số khác từ 0 -> 2 .')
        
    # Lấy ảnh sản phẩm 
    img = main_info['imgs']
    have_parent = img['have_child']
    img_tag = img['img_tag']
    img_class = img['img_class']
    img_child_tag = img['img_child_tag']
    img_child_class = img['img_child_class']
    tag_attribute = img['tag_attribute']
    
    if have_parent == '0':
        try:
            img = soup.find_all(img_tag, class_=img_class)
            link = [i[tag_attribute] for i in img]
            links = set(link)
            imgs = list(links)
        except:
            imgs =''
            print('img_tag hoặc img_class hoặc tag_attribute bị sai. ')
    else:
        link=[]
        tag =[]
        try:
            img = soup.find_all(img_tag, class_= img_class)
            for i in img:
                m = i.find(img_child_tag, class_= img_child_class) 
                if m != None:
                    tag.append(m)
        except:
            print('img_tag hoặc img_class hoặc img_child_tag hoặc img_child_class bị sai.')
            
        for j in tag:
            try:
                link.append(j[tag_attribute])
            except:
                pass
    if link==[] :
        print('tag_attribute bị sai.')
    links = set(link)
    imgs = list(links)

    product_data=[shop_name, stylebox_shop_id, shop_url, product_url, product_name, original_price, imgs, scrape_date, discounted_price, review, size, color, description_1, description_2, rating]   
    
    return product_data
        


# In[8]:


# Hàm này để lấy data từ 1 sản phẩm.

def get_product_data(productlink,config):
    try:    
        html_soure=get_html_source(productlink,config)
        data =get_product_info(html_soure,productlink,config)
    except:
        data = ''
        print('Tên hoặc thông tin điền vào file json bị sai.')
    return data
    


# In[9]:


# Hàm này để lấy data từ nhiều sản phẩm.

def web_scraping(config,productlinks,path_file):
    
    print('Số sản phẩm khai thác được: ',len(productlinks))
    print('------------------------------------------------')
    print('Link các sản phẩm đã khai thác xong : ')
    
    data=[]
    data.append(['shop_name','stylebox_shop_id','shop_url','product_url','product_name','original_price','imgs','scrape_date','discounted_price','review','size','color','description_1','description_2','rating'])
    
    count=1
    for i in productlinks:
        print(count,' : ',i)
        count+=1
        m=get_product_data(i,config)
        data.append(m)
    
    csvfilename = os.path.join(path_file, config['csv_file_name'])
    jsonfilename = os.path.join(path_file, config['json_file_name'])
    export_csv_and_json(csvfilename, jsonfilename, data)
    return 'Oki we done :))'


# In[10]:


#web_scraping(productlinks2)


# In[ ]:




