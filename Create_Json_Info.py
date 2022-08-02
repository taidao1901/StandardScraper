#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


input_info = {
    
    "shop_name":"",
    "stylebox_shop_id":"",
    "shop_url":"",
    "isdynamic":"",
    "json_file_name":"",
    "csv_file_name":"",

    "product_links": {

        "links": "",
        "rootlink":"",
        "parent_tag":"",
        "child_tag":"",

    },


    "main_info": {
        
        
        "product_name": {
            "name_tag":"",
            "name_class":"",
        },

        "original_price": {
            "original_price_tag":"",
            "original_price_class":"",
            "is_woocommerce":"",
            "woocommerce_value":"",
        },

       "imgs": {
            "have_child":"",
            "img_tag":"",
            "img_class":"",
            "img_child_tag":"",
            "img_child_class":"",
            "tag_attribute":"",
        }
    },


    "sub_info": {
        "discounted_price":"",
        "review":"",
        "size": "",
        "color": "",
        "description_1":"",
        "description_2":"",
        "rating":"",

    }
    
}


json_object = json.dumps(input_info, indent=8)
with open("config.json", "w") as outfile:
    outfile.write(json_object)


# In[3]:


import pprint
pprint.pprint(input_info)


# In[ ]:





# In[ ]:




