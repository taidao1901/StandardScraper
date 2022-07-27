from GetProductUrls import get_product_urls
#from Get_Product_Data import web_scraping
import csv
import json
import sys
def export_csv(file, kq):
    with open(file , 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in kq:
            writer.writerow(i)
        f.close()
    return 0
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)  
            
        for i in jsonArray:
            empty_keys = [k for k,v in i.items() if not v]
            for k in empty_keys:
                del i[k]
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        
        jsonString = json.dumps( jsonArray, ensure_ascii=False, indent=4).encode('utf8')
        jsonf.write(jsonString.decode('utf-8'))
def export_csv_and_json(csvfilename, jsonfilename, data):
    export_csv(csvfilename, data)
    csv_to_json(csvfilename, jsonfilename)



if __name__ == '__main__':
    # Tên file cần xuất
    csvfilename  = 'gemclothing.csv'
    jsonfilename = 'gemclothing.json'
    # Tham số cho hàm lấy link các sản phẩm
    links=['https://hades.vn/collections/all?page={number}']
    rootlink='https://hades.vn'
    parent_tag='product-img'
    child_tag = 'image-resize'
    webtype = 'normal'
    dynamic= False
    # Tham số cho hàm lấy thông tin sản phẩm


    # Get link products
    try: 
        product_links= get_product_urls(links, rootlink=rootlink, parent_tag=parent_tag, child_tag=child_tag,webtype=webtype,dynamic=dynamic)
        try:
            if sys.argv[1]=="debug_links":
                print('5 link sản phẩm đầu tiên là: ')
                for i in range(5):
                    print(product_links[i])
            else:
                pass
        except:
            pass
    except:
        print('Lỗi lấy link các sản phẩm')
        exit()

    # Get infor products
    try:
        #Chỗ thêm tham số ở đây.
        data = web_scraping(productlinks)
        try: 
            if sys.argv[1]=="debug_infor":
                print('Thông tin 5 sản phẩm đầu tiên là:')
                for i in range(5):
                    print(data[i])
        except:
            pass
    except:
        print('Lỗi lấy thông tin sản phẩm')
        exit()

    # Export data to csv&json file
    try: 
        export_csv_and_json(csvfilename, jsonfilename, data)
    except:
        print('Lỗi trong quá trình xuất file. Có thể do chưa sửa tên shop.')

    
        
