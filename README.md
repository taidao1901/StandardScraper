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
Step 5 : return to website, press F12 to see html code. Choose the tag has link product.
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
Step 3 :
```

## Work with config.json file
```
Step 1 : copy file config.json to config folder and make sure just only this file in config folder.

Step 2 : fill in parameters follow guide bellow.
```
  1. Primary infomations.
```
 Shop_name, stylebox_shop_id, shop_url can filled base on infomation from '0. Online_shop_link' file.
 isdynamic : default value is 0, if use didn't get any infomations after run tool, change it to 1 and try again.
```

  2. Get all product links.
  ```
   
   In product_links part  :
   links : link of page which include all product and . If you can't find all product page, you can get a group of link that you thought can get all product. 
   ex :
   
  ```
 
![alt text](https://github.com/taidao1901/StandardScraper/blob/fabd67892744a08eb5533b94d133492e75de37cf/imgs/Screenshot%20(279).png) 


    
   
    
    
    
