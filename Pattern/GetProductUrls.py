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


def dynamic_web(link,parent_btn_class='',btn_class=''):
    '''
        Lấy nội dung html của dsynamic website
            link: link của website
            parent_btn_class : class của thẻ <div> cha chứa chứa button
            btn_class : class của button
            ''
    '''

    try:
        # Get infor in a dynamic page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link)
        last_height = driver.execute_script("return document.body.scrollHeight")
        cou=0
        while True:
            cou+=1
            # Scroll down to bottom
            for  i in  (2500,1000):  
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight - arguments[0]);",i)
                sleep(1)
            try:
                if parent_btn_class!="":
                    try:
                        parent_but= driver.find_element(by=By.CLASS_NAME, value=parent_btn_class)
                        if btn_class!="":           
                            more_button = parent_but.find_element(by=By.CLASS_NAME, value=btn_class)
                        else:
                            more_button = parent_but.find_element(by=By.TAG_NAME,value='a')
                        if more_button:
                            driver.execute_script("arguments[0].click();", more_button)
                    except:
                        print('Không tìm thấy nút xem thêm. Kiểm tra lại scroll_btn_type')
                        pass
            except:
                pass

            # Wait to load page
            sleep(1)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
            if cou>50:
                break
        
        # Convert to html type

        sele = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        return sele
    except Exception:
        print('Lỗi phần dynamic website')
        traceback.print_exc()


def Get_product_url(content,rootlink='',parent_atag_tag='', parent_atag_class='', atag_class='',same_string=''):
    '''
        Lấy các url sản phẩm trên 1 trang.
            content: Nội dung của trang
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_atag_class: Class của thẻ div gần nhất
            child-tag: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
    '''
    productlinks=[]
    try:
        # Convert content in page to beutifulsoup type
        soup = BeautifulSoup(content, 'html.parser')

        # find parent block that contain <a> tag
        try:
            product_list = soup.find_all(parent_atag_tag, class_= parent_atag_class)
        except:
            print("Không tìm thấy thẻ parent_atag. Kiểm tra lại parent_atag_tag, parent_atag_class")
            pass
        for product in product_list:
            # if a tag have class name then find it
            try:
                if atag_class =='':

                    temp = product.find_all('a',href=True)[0]['href']
                else: 
                    temp = product.find_all('a',class_=atag_class,href=True)[0]['href']
            except:
                print('Không tìm được atag. Kiểm tra lại atag_class')
                pass
            if (temp!='') and (temp!='#'):
                product_link = urllib.parse.urljoin(rootlink,temp)
                check_link = product_link.split('/')
                if (same_string in check_link):
                    productlinks.append(product_link)
    except Exception:
        print('Lỗi phần lấy link sản phẩm')
        traceback.print_exc()
    # return link of products
    return productlinks
    
def Normal_Website(links, rootlink='', parent_atag_tag='',parent_atag_class='', atag_class='', isdynamic = False, same_string=''):
    '''
        Hàm lấy thông tin của các trang có số trang
            links: Truyền danh sách link lấy sản phẩm. Ví dụ: ['https://hades.vn/collections/top?page={number}','https://hades.vn/collections/bottoms?page={number}']']
            rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
            parent_atag_class: Class thẻ div bên ngoài thẻ a
            atag_class: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
    '''
    product_links = []

    # excute in each link in links
    for link in links:
        num= 1
        while True:
            # get content in each page number per link
            content=''
            if isdynamic == False:
                user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
                content = requests.get(link.format(number=num),headers = user_agent,verify =False).content
            else: 
                content = dynamic_web(link.format(number=num))

            # Calculate new list length and compare with last list length
            old_list_link_count= len(product_links)
            newlink = Get_product_url(content,rootlink,parent_atag_tag, parent_atag_class, atag_class, same_string)

            for i in newlink:
                if i not in product_links:
                    product_links.append(i)
            
            # if length is changed, increase page number
            if len(product_links) > old_list_link_count:
                print(link.format(number=num))
                num +=1
            else:
                break
    # return list product links in normal website
    return product_links

def Scroll_Website(links, rootlink='', parent_atag_tag='', parent_atag_class='', atag_class='',parent_btn_class ='',btn_class='',same_string=''):
    
    product_links = []
    for link in links:
        content = dynamic_web(link,parent_btn_class,btn_class)
        new_links = Get_product_url(content,rootlink,parent_atag_tag, parent_atag_class, atag_class,same_string)
        for i in new_links:
            if i not in product_links:
                product_links.append(i)
    return product_links

def get_product_urls(config):
    '''
        Hàm chính lấy link các sản phẩm của một website
            config chứa các thông tin như:
                links: Danh sách link lấy sản phẩm.
                rootlink: Dùng cho các trang dùng địa chỉ tương đối ( Không truyển nếu trang dùng địa chỉ tuyệt đối)
                parent_atag_class: Class thẻ div bên ngoài thẻ a
                atag_class: Class của thẻ a chứa link sản phẩm (Không truyền nếu không có tên class)
                webtype: loại website, mặc định là normal ('normal': cho các website sử dụng số trang, 'scroll': cho các website dạng cuộn)
                isdynamic: Có phải dạng isdynamic website hay không, mặc đinh là False(False: cho các website không phải dạng isdynamic, True: ngược lại )
    '''
    
    product_links_config= config['product_links']

    links= str(product_links_config['links']).split(",")
    rootlink= links[0]

    product_block = product_links_config['product_block']
    parent_atag_tag = product_block['parent_atag_tag']
    parent_atag_class=product_block['parent_atag_class']
    atag_class =product_block['atag_class']

    webtype = product_links_config['webtype']

    isdynamic= bool(config['isdynamic'])
    same_string= product_links_config['same_string']
    scroll_btn_type= product_links_config['scroll_btn_type']
    parent_btn_class= scroll_btn_type['parent_btn_class']
    btn_class= scroll_btn_type['btn_class']

    if webtype== 'normal':
        product_links = Normal_Website(links, rootlink,parent_atag_tag, parent_atag_class, atag_class, isdynamic, same_string)
        product_links=list(set(product_links))

        return product_links
    elif webtype == 'scroll':
        product_links = Scroll_Website(links,rootlink,parent_atag_tag, parent_atag_class,atag_class,parent_btn_class, btn_class, same_string)
        product_links=list(set(product_links))
        return product_links
    else: 
        print('Webtype không tồn tại')
        return []
    





    



        


                   


        



