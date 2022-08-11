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

## Get all product informations progress
```
step 1 :  fill primary infomations

Step 2 : find all product links.

Step 3 : find product infomations

Step 4 :  export data to csv and json file.

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
 
![alt text](https://github.com/taidao1901/StandardScraper/blob/8cf22bc4f17dfcaa642c3796734e3ea46d58784f/imgs/Screenshot%20(265).png) 


    
   
    
    
    
