'''Import các thư viện cần thiết'''
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import traceback
import urllib.parse
from selenium.webdriver.common.by import By


def Dynamic_web(link,button_class=''):
    '''
        Lấy nội dung html của dynamic website
            link: link của website
    '''

    try:
        # Get infor in a dynamic page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
            if button_class!="":           
                more_button = driver.find_element(by=By.CLASS_NAME, value=button_class)
                driver.execute_script("arguments[0].click();", more_button)
            # Wait to load page
            sleep(5)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Convert to html type
        sele = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        return sele
    except Exception:
        print('Lỗi phần dynamic website')
        traceback.print_exc()


def Get_product_url(content,rootlink='', parent_tag='', child_tag=''):
    '''
        Lấy các url sản phẩm trên 1 trang.
            content: Nội dung của trang
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_tag: Class của thẻ div gần nhất
            child-tag: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
    '''
    productlinks=[]
    try:
        # Convert content in page to beutifulsoup type
        soup = BeautifulSoup(content, 'html.parser')

        # find parent block that contain <a> tag
        product_list = soup.find_all('div', class_= parent_tag)
        for product in product_list:
            # if a tag have class name then find it
            try:
                if child_tag =='':
                    temp = product.find_all('a',href=True)[0]['href']

                else: 
                    temp = product.find_all('a',class_=child_tag,href=True)[0]['href']
                if (temp!='') and (temp!='#'): 
                    productlinks.append(urllib.parse.urljoin(rootlink,temp))
            except:
                print('Không lấy được link sản phẩm.')
                pass
    except Exception:
        print('Lỗi phần lấy link sản phẩm')
        traceback.print_exc()
    # return link of products
    return productlinks
    
def Normal_Website(links, rootlink='', parent_tag='', child_tag='', dynamic = False):
    '''
        Hàm lấy thông tin của các trang có số trang
            links: Truyền danh sách link lấy sản phẩm. Ví dụ: ['https://hades.vn/collections/top?page={number}','https://hades.vn/collections/bottoms?page={number}']']
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_tag: Class thẻ div bên ngoài thẻ a
            child_tag: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
    '''
    product_links = []

    # excute in each link in links
    for link in links:
        num= 1
        while True:
            # get content in each page number per link
            content=''
            print(link.format(number=num))
            if dynamic == False:
                content = requests.get(link.format(number=num)).content
            else: 
                content = Dynamic_web(link.format(number=num))

            # Calculate new list length and compare with last list length
            length_link= len(product_links)
            product_links = product_links + Get_product_url(content,rootlink, parent_tag, child_tag)

            # if length is changed, increase page number
            if length_link< len(product_links):
                num +=1
            else:
                break
    # return list product links in normal website
    return product_links
def Scroll_Website(links, rootlink='', parent_tag='', child_tag='',button_class=''):
    '''
        Hàm lấy link sản phẩm từ các trang dạng cuộn
            links: Danh sách link lấy sản phẩm. Ví dụ: ['https://ssstutter.com/c/for-him','https://ssstutter.com/c/for-her']
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_tag: Class thẻ div bên ngoài thẻ a
            child_tag: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
    '''
    # excute in each link in links
    product_links = []
    for link in links:
        content = Dynamic_web(link,button_class)
        product_links = product_links + Get_product_url(content,rootlink, parent_tag, child_tag)
    return product_links

def get_product_urls(links, rootlink='', parent_tag='', child_tag='',webtype='normal',dynamic=False,button_class=""):
    '''
        Hàm chính lấy link các sản phẩm của một website
            links: Danh sách link lấy sản phẩm.
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_tag: Class thẻ div bên ngoài thẻ a
            child_tag: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
            webtype: loại website, mặc định là normal ('normal': cho các website sử dụng số trang, 'scroll': cho các website dạng cuộn)
            dynamic: Có phải dạng dynamic website hay không, mặc đinh là False(False: cho các website không phải dạng dynamic, True: ngược lại )
    '''
    if webtype== 'normal':
        product_links = Normal_Website(links, rootlink, parent_tag, child_tag, dynamic)
        return product_links
    elif webtype == 'scroll':
        product_links = Scroll_Website(links,rootlink,parent_tag,child_tag,button_class)
        return product_links
    else: 
        print('Webtype không tồn tại')
        return []
    





    



        


                   


        



