#from Get_Product_Info_Test import Test_Data
from GetProductUrls import get_product_urls
from Get_Data_Fi_2 import web_scraping
import concurrent.futures
import csv
import json
import sys
from datetime import datetime
import traceback
import time
import os
import urllib3
import shutil


def scraping_thread(config_file):
    print('Bat dau voi ', config_file)
    with open(config_file, encoding='utf-8') as cf:
        try:
            config = json.load(cf)
        except:
            error_text= 'Lỗi định dạng file config ' +config_file+ '. Copy lại file mẫu rồi sửa lại.'+'\n\n'
            with open('report_error.txt','a',encoding='utf8') as rf:
                rf.write(error_text)
            exit()
    #Get link products
    #print('Bắt đầu lấy link sản phẩm ....')
    #start = time.time()
    try: 
        product_links= get_product_urls(config)
        print('Đã lấy link sản phẩm xong voi ', config_file)
    except Exception:
        print('Lỗi lấy link sản phẩm')
        traceback.print_exc()
        pass
    # Get infor products

    try:
        data = web_scraping(config, product_links, result_path)
        #print('Thời gian lấy link sản phẩm: ', time.time()-start)
    except Exception:
        print('Lỗi lấy thông tin sản phẩm')
        traceback.print_exc()
        pass

    return ''





if __name__ == '__main__':
    __location__ = os.path.abspath('..')
    configs_path = os.path.join(__location__, 'Config')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    rsfd = os.path.join(__location__, 'Results')
    # Remove old data files.
    try:
        shutil.rmtree(rsfd)
    except:
        pass
    try:
        os.makedirs(rsfd)
    except:
        pass
    result_path = os.path.join(__location__, 'Results')

    config_file_list=[]

    # Get all config file directories 
    for filename in os.listdir(configs_path):
        config_file_list.append(os.path.join(configs_path, filename))
    

    t1 = time.perf_counter()
    # Use multi thread to scrap data from many shop at the same time
    with concurrent.futures.ThreadPoolExecutor(8) as executor:
        executor.map(scraping_thread, config_file_list)
    t2 = time.perf_counter()
print(f'MultiThreaded Code Took:{t2 - t1} seconds')

    
        
        
