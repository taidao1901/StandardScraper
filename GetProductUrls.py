'''Import các thư viện cần thiết'''
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def Get_product_url(content,rootlink='', parent_tag='', child_tag=''):
    soup = BeautifulSoup(content, 'html.parser')
    count = 0
    product_list = soup.find_all('div', class_=parent_tag)
    productlinks=[]
    for product in product_list:
        #Lấy ra link của sản phẩm. Nếu có tồn tại class thẻ q thì tìm theo class của thẻ a
        if child_tag =='':
            productlinks.append(rootlink + product.find_all('a',href=True)[0]['href'])
        else: 
            productlinks.append(rootlink + product.find_all('a',class_=child_tag,href=True)[0]['href'])
    return productlinks
    
def Normal_Website(link, rootlink='', parent_tag='', child_tag=''):
    '''
        Hàm lấy thông tin của các trang có số trang
            link: Truyền link tổng quát của website. Ví dụ: https://laminapparel.com/shop/page/{number}/
            parent_tag: Class thẻ div bên ngoài thẻ a
            child_tag: class thẻ a ()
    '''
    num= 1
    productlinks = []
    while True:
        content = requests.get(link.format(number=num)).content
        print(link.format(number=num))
        length_link= len(productlinks)
        productlinks = productlinks + Get_product_url(content,rootlink, parent_tag, child_tag)
        if length_link< len(productlinks):
            num +=1
        else:
            return productlinks



        


                   


        



