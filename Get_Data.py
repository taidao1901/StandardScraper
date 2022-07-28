
# In[1]:


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
    




# Sử dụng hàm này lấy giá sản phẩm hoặc các thông tin khác được bọc trong class webwoocommerce
def get_webwoocommerce_value(productlinks):
    
    s = HTMLSession()
    r = s.get(productlinks)
    # Số 2 trong dòng này có thể sửa thành số 1 hoặc 0 nếu code không chạy
    price = r.html.find('span.woocommerce-Price-amount.amount bdi')[0].full_text   
    return price


# In[5]:


# Dùng hàm này để lấy thông tin sản phẩm
def get_product_info(html_soure,productlink):
    
    soup = BeautifulSoup(html_soure,'lxml')
    kq=[]
    
    # Lấy tên sản phẩm, SỬA CODE Ở ĐÂY
    name = soup.find('h1',class_="title")
    #print(name)
    kq.append(name)
    
    # Thêm vào link sản phẩm, KHÔNG SỬA CHỖ NÀY
    kq.append(productlink)

        
    # Lấy giá gốc, SỬA CODE Ở ĐÂY
    price = get_webwoocommerce_value(productlink)
    kq.append(price)
    
    
    # Lấy giá khuyến mãi, SỬA CODE Ở ĐÂY
    try:
        print(4/0)
    except:
        Sale_price = ''
    kq.append(Sale_price)
    
    
    # Lấy size sản phẩm , SỬA CODE Ở ĐÂY
    try:
        #print(4/0)
        size=[]
        div = soup.find_all('span',class_="variable-item-span")
        
        for i in div:
            size.append(i.text)
    except:
        size = ''
    kq.append(size)
    
    
    # Lấy màu sản phẩm, SỬA CODE Ở ĐÂY
    try:
        print(4/0)
    except:
        colors=''
    kq.append(colors)
    
    
    # Lấy mô tả sản phẩm, SỬA CODE Ở ĐÂY
    try:
        #print(4/0)
        description = soup.find('div',class_="short-description").text.strip()
    except:
        description =''
    kq.append(description)
        
    
    # Lấy đánh giá sản phẩm, SỬA CODE Ở ĐÂY
    try:
        print(4/0)
    except:
        comments =''
    kq.append(comments)
    
    
    # Lấy link ảnh, SỬA CODE Ở ĐÂY.
    img = soup.find_all('div', class_="s-img")
    link = [i.get('data-bg') for i in img]
    #print(len(link))
    #print(link)
    
    
    #Tránh lặp hình ảnh trong list, không sửa chỗ này.
    links=set(link)
    linkfinal = list(links)
    
    
    
    for i in linkfinal:
        kq.append(i)
    
    return kq
        


# In[6]:


# Nhập thông tin chung của shop ở đây .
shop_name ='emswear'
stylebox_shop_id ='2'
shop_url ='https://emwear.vn'



now= datetime.now()
scrap_day = now.strftime("%m/%d/%Y %H:%M:%S")
tt=[shop_name,stylebox_shop_id,shop_url,scrap_day]
tt.reverse()


# Không chỉnh sửa chỗ này
def get_data(productlink,isdynamic,tt=tt):
    html_soure=get_html_source(productlink,isdynamic)
    data =get_product_info(html_soure,productlink)
    data.reverse()
    for i in tt:
        data.append(i)
    data.reverse()
    return data

# Không chỉnh sửa chỗ này.
def web_scraping(productlinks,isdynamic,tt=tt):
    data=[]
    data.append(['shop_name','stylebox_shop_id','shop_url','scrap_day','name','product-link','price','Sale_price','size','description','comments','pic1'])
    k=2
    print('Số sản phẩm khai thác được: ',len(productlinks))
    print('------------------------------------------------')
    print('Link các sản phẩm đã khai thác xong : ')
    c=1
    for i in productlinks:
        print(c,' : ',i)
        c+=1
        m=get_data(i,isdynamic,tt=tt)
        print(m)
        while len(data[0])<len(m):
            data[0].append('pic'+str(k))
            k+=1
        data.append(m)
    return data
