# Standard Version

## Setup Enviroment
```
# using pip
pip install -r requirements.txt

# using Conda
conda create --name <env_name> --file requirements.txt
```
## Hướng dẫn sử dụng.
### Lấy link các sản phẩm có trong website.
  1. Xác định web thuộc dạng có số trang ('normal') hay dạng cuộn ('scroll') : Chỉnh tham số webtype
  ```
    # web thuộc dạng có số trang
    webtype= 'normal' 
    # web thuộc thạng cuộn
    webtype= 'scroll'
  ```
  2. Xác định website dạng bình thường (False) hay động (True): Chỉnh tham số dynamic
  ```
      # website dạng bình thường
      dynamic= False
      # website dạng động
      dynammic = True
  ```
  3. Xác định (các) link trên website cần thu thập: Chỉnh tham số links
  ```
      # Đối với  web dạng có số trang
      links = ['https://hades.vn/collections/top?page={number}','https://hades.vn/collections/bottoms?page={number}']
      # Đối với web dạng cuộn
      links = ['https://ssstutter.com/c/for-him','https://ssstutter.com/c/for-her']
      
  ```
  4. Xác định tên các class cần thiết.
    * Ví dụ: 
    ```
    
    ```
    
### Các bước thao tác với file Get_Data.py .
  
  1. Quy ước
    
    
    - Tên_biến : các tên dùng để lưu trữ một giá trị như : name để lưu trữ tên, price để lưu trữ giá tiền 
    - Tên_thẻ : tên các thẻ trong html như div, span, h1, img ...
    - Tên_class : tên các class được đặt trong thẻ 
    **Chú ý :** 
    - Khi lấy class ưu tiên chọn những tên có ý nghĩa khi dịch ra tiếng Việt như : product, item ...
    - Tránh lấy các class có tên vô nghĩa, hoặc thuộc về định dạng như : slick-slide, container, col-6, col-md-4, col-lg-3 ...
    
  2. Các cú pháp thường dùng khi sửa file  :
    
    
    
    **Lấy các thẻ**
    - Lấy một thẻ :
      > Tên_biến = soup.find('Tên_thẻ', class_="Tên_class")
    - Lấy nhiều thẻ :
      > Tên_biến = soup.find_all('Tên_thẻ', class_="Tên_class")
    
 
   
    
     ** Lấy thuộc tính của thẻ**
    - Lấy một thuộc tính nào đó ( cái này tùy trường hợp có thể lấy được hoặc không)
    - Lấy từng phần tử trong một biến chứa danh sách thẻ :
      for i in Tên_biến :
          Câu lệnh muốn dùng để sử lý các thẻ có trong danh sách thẻ.
    - Lấy một thẻ trong nhiều thẻ
   
   
  3. Các chỗ cần sửa
    
    
   
    
    
    
