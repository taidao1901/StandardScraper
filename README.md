# Standard Version 
# User Guide


## Setup workspace
```
Step 1 : Dowload and install VScode via this link :
https://code.visualstudio.com/download

step 2 : create a folder and let it be your workspace folder.

Step 3 : dowload code from this link :

Step 4 : unzip it and put to your workspace folder.

Step 5 : run VScode and open your workspace folder.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/77e9b258a457045474ea701e65a6a1f34a8056fe/imgs/Screenshot%20(260).png) 
```
Step 6 : in VScode, you press Ctrl+shift+x to open extensions window.

Step 7 : search "python" in search bar .

Step 8 : install the first one.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/099c5d7740c2d0715febe34d49686ae6fc9ea5e5/imgs/Screenshot%20(262).png) 
```
Step 9 : search "Jupyter" , "Excel Viewer" and repeat step 8 respectively. 
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/83a930c579d642c3b81b57eb7125af523958768a/imgs/Screenshot%20(264).png) 

![alt text](https://github.com/taidao1901/StandardScraper/blob/a5ab3b8dc495223bc1e68e4de34d99f6f23e458c/imgs/Screenshot%20(263).png) 
```
step 10 : press Ctrl+ `  to open VScode Terminal and run this code :
pip install -r requirements.txt
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/8cf22bc4f17dfcaa642c3796734e3ea46d58784f/imgs/Screenshot%20(265).png) 
## Get all product informations progress sumary
```
Step 1 : get all products links
Step 2 : get main infomations and sub informations of all products.
Step 3 : check gained data.
Step 4 : export data to json and csv file.
```

### Get all product links
```
Step 1 : Open config folder, after that open config.json file.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/388b2b438bc3583d650de603fe809fb8a7d947d3/imgs/Screenshot%20(268).png) 

```
Step 2 : fill primary informations of shop : shop_name, stylebox_shop_id, shop_url. isdynamic parameter will be set 0 as default.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/136c79339c38acda03db0f332e30a691e8b38c51/imgs/Screenshot%20(269).png) 
```
Step 3 : Open shop's website and find page that include all products or group of link can get all products. if link has many product page, we have to change to page 2,3, etc... to see number of page on link. 
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/9d339d9ab605aefb3d30386fcdf2dc3dc2af70b9/imgs/Screenshot%20(271).png) 
```
Step 4 : Change the number of page to this syntax : {number}  and fill to "links" paremeter on "product_links" part.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/73314980b180a69c6606260025b80a557292b110/imgs/Screenshot%20(272).png) 
```
Step 5 : return to website, press F12 to see html code. Choose the tag has link product. Press Ctrl+Shift+c to see exactly html souce code of anywhere your mouse point. It will help you a lot.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/a3dfca6a9a5e498edf39caf5f9afb3769a98b4c6/imgs/Screenshot%20(274).png) 
```
Step 6 : Fill parent tag information of selected tag to "product_block" part.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/20bb517473d76ff61c126c03a5e6ff62ead3ab8b/imgs/Screenshot%20(275).png) 
```
Step 7 : fill "webtype" is "scroll" if page is scrolling page type. Otherwise, we will set "normal" as default. 
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/46d6241364bee68faaee6390f4c653e33176ad32/imgs/Screenshot%20(278).png) 
```
Notice : if scrolling page have button to show more product, we have to fill class of button and class of its parent tag to "scroll_btn_type" part. Image bellow is example.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/fabd67892744a08eb5533b94d133492e75de37cf/imgs/Screenshot%20(279).png) 

### Get main infomations and sub informations of all products.
```
Step 1 : open a random product link.
Step 2 : press F12 to see html source code.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/fc81965a5cfdc3ac1b964785b8dc37eb9b106435/imgs/Screenshot%20(280).png) 
```
Step 3 : Find the tag contains product name. Pressing Ctrl+Shift+c will help you again.
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/0a47da1efbc1727b3647bb99899a65099c38cb76/imgs/Screenshot%20(281).png) 
```
Step 4 : comback to config.json file and fill parameter on product_name part. To do this step, you have to see rule of synstax bellow.
Step 5 : repeate step 4 with all part remaining on "main_info" and "sub_info" part .
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/f9d2b152c30836dda830d3451d5e94aaad942fdf/imgs/Screenshot%20(282).png) 

#### Very impotant
```
Explain four primary parameter on "main_info" and "sub_info" part :

selected_tag :  tags you want to choose. You can config this parameter follow Get-info syntax explained bellow.

value : if selected_tag have many tags and you want to choose one of them, you can config this as ordinal number start from 0. 
if you want to get all tag from selected_tag, you have to set it is "null".

get_text : if you want to get tag content, set get_text is 1. Otherwise, it has to set 0.

attrs : if the thing you want to get is value of something attribute, you can set get_text is 0 and fill attribute name to this parameter.     
```

```
Get-info syntax :

Class :  .
Ex :  .price  -> class "price" ,   .item   -> class "item"

ID :  #
Ex :  #price  ->  ID is "price"  ,    #item   -> ID is "item"

Other Attribute : [attribute_name=attribute_value]
Ex :  [aria-label=Size]  -> "aria-label" attribute has value is "Size",
      [data-attribute_name=attribute_pa_size]  ->  "data-attribute_name" attribute has value is "attribute_pa_size"
      
Choose a tag : tag_name+Class/ID/Attibute 
Ex :   div.price    -> get tag div has class "price",
       span#price   -> get tag span has ID is "price",
       span[data-value=m]   ->   get tag span has attribute "data-value" is "m",
       div.price#item ->  get tag div has class "price" and ID is "item"
       span.price[data-value=color-red] -> 

If you can't filter out tags you want, you can get it from their parent tag. 
Parent tag is the tag that contain the tag you want to choose. Follow this syntax :  parent_tag chosen_tag
Ex : div.price#item span   ->  get tag span from their parent is tag div.price#item,
     span[data-value=m] div.price -> get tag div.price from their parent is tag span[data-value=m]
```
```
After done, "main_info" and "sub_info" part may like 
```
![alt text](https://github.com/taidao1901/StandardScraper/blob/1ce10a18daa69459894f1bdc5af8e2d29b75f54d/imgs/Screenshot%20(285).png) 
![alt text](https://github.com/taidao1901/StandardScraper/blob/1ce10a18daa69459894f1bdc5af8e2d29b75f54d/imgs/Screenshot%20(286).png) 

#### Notice
```
BE CAREFULL WITH SPACE WHEN YOU CONFIG.
```

![alt text](https://github.com/taidao1901/StandardScraper/blob/1ce10a18daa69459894f1bdc5af8e2d29b75f54d/imgs/Screenshot%20(286).png) 


    
   
    
    
    
