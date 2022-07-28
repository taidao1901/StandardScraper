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
      # Đối với  web dạngcó số trang
      links = ['https://hades.vn/collections/top?page={number}','https://hades.vn/collections/bottoms?page={number}']
      # Đối với web dạng cuộn
      links = ['https://ssstutter.com/c/for-him','https://ssstutter.com/c/for-her']
      
    ```
    
