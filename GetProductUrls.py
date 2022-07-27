'''Import các thư viện cần thiết'''
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

def Dynamic_web(link):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Kiểm tra đã load hết trang hay chưa ?
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        sleep(5)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sele = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    return sele

def Get_product_url(content,rootlink='', parent_tag='', child_tag=''):
    soup = BeautifulSoup(content, 'html.parser')
    product_list = soup.find_all('div', class_= parent_tag)
    productlinks=[]
    for product in product_list:
        #Lấy ra link của sản phẩm. Nếu có tồn tại class thẻ q thì tìm theo class của thẻ a
        if child_tag =='':
            productlinks.append(rootlink + product.find_all('a',href=True)[0]['href'])
        else: 
            productlinks.append(rootlink + product.find_all('a',class_=child_tag,href=True)[0]['href'])
    return productlinks
    
def Normal_Website(links, rootlink='', parent_tag='', child_tag=''):
    '''
        Hàm lấy thông tin của các trang có số trang
            link: Truyền link tổng quát của website. Ví dụ: https://laminapparel.com/shop/page/{number}/
            parent_tag: Class thẻ div bên ngoài thẻ a
            child_tag: class thẻ a ()
    '''
    product_links = []
    for link in links:
        num= 1
        while True:
            content = requests.get(link.format(number=num)).content
            length_link= len(productlinks)
            product_links = product_links + Get_product_url(content,rootlink, parent_tag, child_tag)
            if length_link< len(product_links):
                num +=1
            else:
                break
    return product_links
def Scroll_Website(links, rootlink='', parent_tag='', child_tag=''):
    '''
        Hàm lấy link sản phẩm từ các trang dạng cuộn
            link:
            rootlink:
            parent_tag:
            child_tag:
    '''
    product_links = []
    for link in links:
        content = Dynamic_web(link)
        product_links = product_links + Get_product_url(content,rootlink, parent_tag, child_tag)
        print(len(product_links))
    return product_links
if __name__ == '__main__':
    product_links= NỎ(links=['https://huongboutique.vn/shop-online?page={number}}'], rootlink='https://ssstutter.com', parent_tag='thumbnail', child_tag='')
    [print(x) for x in product_links]



    



        


                   


        



