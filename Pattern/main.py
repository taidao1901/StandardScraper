#from Get_Product_Info_Test import Test_Data
from GetProductUrls import get_product_urls
from Get_Data_Fi_2 import web_scraping
import csv
import json
import sys
from datetime import datetime
import traceback
import time
import os
import urllib3




if __name__ == '__main__':
    __location__ = os.path.abspath('..')
    configs_path = os.path.join(__location__, 'Config')
    result_path = os.path.join(__location__, 'Results')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    for filename in os.listdir(configs_path):
        # Tham số cho hàm lấy link các sản phẩm, SỬA THAM SỐ Ở ĐÂY
        with open(os.path.join(configs_path, filename), encoding='utf-8') as cf:
            try:
                config = json.load(cf)
            except:
                print('Lỗi định dạng file config. Copy lại file mẫu rồi sửa lại.')
                exit()
        result_folder_name = config['stylebox_shop_id'] +'_'+config['shop_name']
        #Get link products
        print('Bắt đầu lấy link sản phẩm ....')
        #start = time.time()
        try: 
            product_links= get_product_urls(config)
            print('Đã lấy link sản phẩm xong .')
            try:
                if "debug_links" in sys.argv:
                    print('Tổng số sản phẩm lấy được link là:', len(product_links))
                    print('5 link sản phẩm đầu tiên là: ')
                    for i in range(5):
                        print(product_links[i])
            except:
                pass
        except Exception:
            print('Lỗi lấy link sản phẩm')
            traceback.print_exc()
            exit()

    
        # Get infor products
        try:
            if "debug_infor" in sys.argv:
                Test_Data(product_links[0], config)
            else:
                if os.path.exists(os.path.join(result_path, result_folder_name))==False:
                    os.mkdir(os.path.join(result_path, result_folder_name))
                data = web_scraping(config, product_links, os.path.join(result_path, result_folder_name))
            #print('Thời gian lấy link sản phẩm: ', time.time()-start)
            exit()
        except Exception:
            print('Lỗi lấy thông tin sản phẩm')
            traceback.print_exc()
            exit()
        
