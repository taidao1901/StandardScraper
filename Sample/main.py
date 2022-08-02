from GetProductUrls import get_product_urls
from Get_Data_Fi import web_scraping
import csv
import json
import sys
from datetime import datetime
import traceback
import time
import os



if __name__ == '__main__':

    __location__ = os.path.abspath('..')
    print(__location__)
    configs_path = os.path.join(__location__, 'Config')
    # for filename in os.listdir(configs_path):
    filename= 'config_sobie.json'
    # Tham số cho hàm lấy link các sản phẩm, SỬA THAM SỐ Ở ĐÂY
    with open(os.path.join(configs_path, filename), encoding='utf-8') as cf:
        config = json.load(cf)
    product_links_config= config['product_links']

    links= str(product_links_config['links']).split(",")
    rootlink= links[0]
    parent_tag=product_links_config['parent_tag']
    child_tag =product_links_config['child_tag']
    webtype = product_links_config['webtype']
    dynamic= bool(product_links_config['dynamic'])
    parent_but_class= product_links_config['parent_but_class']
    button_class= product_links_config['button_class']

    # #Get link products
    start = time.time()
    try: 
        product_links= get_product_urls(links, rootlink=rootlink, parent_tag=parent_tag, child_tag=child_tag,webtype=webtype,dynamic=dynamic,parent_but_class=parent_but_class,button_class=button_class)
        try:
            if "debug_links" in sys.argv:
                print('Tổng số sản phẩm là:', len(product_links))
                print('5 link sản phẩm đầu tiên là: ')
                for i in range(5):
                    print(product_links[i])
        except:
            pass
    except Exception:
        print('Lỗi lấy link sản phẩm')
        traceback.print_exc()
        exit()
    print('Thời gian lấy link sản phẩm: ', time.time()-start)

    # Get infor products
    try:
        #Chỗ thêm tham số ở đây.
        data = web_scraping(config,product_links)
        try: 
            if "debug_infor" in sys.argv:
                print('Thông tin 5 sản phẩm đầu tiên là:')
                for i in range(5):
                    print(data[i])
        except:
            pass
    except Exception:
        print('Lỗi lấy thông tin sản phẩm')
        traceback.print_exc()
        exit()