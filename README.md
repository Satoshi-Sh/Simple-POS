<h1 align="center">Simple POS</h1>
<p align="center" width="100%">
<img src='https://res.cloudinary.com/dmaijlcxd/image/upload/v1680989768/pos_screen_lry4xe.png' width='600' height='500'>
</p>
<p align="center">
  POS Page
</p>

## Demo
[Video](https://youtu.be/HtDdZ87K-to)

## Description:
This application gives simpe POS system to anyone. Program reads a menu Json file, and open a cash register. User can keep a note on the order if needed. Every order is recorded in the sales reacord file once the transaction is completed. 
## How to Use
#### setup environment
##### After making a env folder and activate it, 
`$pip install -r requirement.text`
##### Use the sample menu 
`$python3 projects.py felipes.json`

#### Format of Menu File 
```
{
    "restaurant":"Felipe's",
    "items":[
        {"item":"Baja Taco",
         "price":7.50,
        "available":true},
        {"item":"Tinga Tacos",
         "price":7.50,
        "available":true},]
}
```
#### Format of Sales Records
```
{
    "orders": [
        {
            "items": {
                "Baja Taco: $7.5": 1
            },
            "total": 8.25,
            "time": "04-08-2023 16:24:04",
            "cash": false,
            "comment": ""
        }]
}    
```

#### Make a new restaurant 
Make restaurnt_name.json files in the menues folder and the sales_records folider.
##### Make a Menu File with empty dictionary
```
{}
```
##### Make a Record File 
```
{
    "orders": [
        ]
}  
```


## Features 
#### Menus 
You can update your menu through Json files under menus, as such changing prices, adding new items, remove old items. And also, you can put items unavailable for the time being.
    
#### Register
Register.py is for the main page of this application. You can click buttons to add items to the order. You can search items with back and next button if ordered items are not on the screen. If you need to delete item from the order, you need to click on the del button. The del button displayed red, and you just need to click on the button of the item you need to delete. Once the order is finished, customer may pay cash or cradie/debit. If the customer pay by card, you can just click the received button and then click complete. That's the end of transaction. If the customer pay by cash, you need to type the amount you received and the screen show the change. Once complete is clicked, all the data is sent to the sales record file and the screen goes back to the original state. 
### Note
You may keep a note on the order if you press the pencil icon. This button opens another file to keep a note. You just need to type and click save. The note is added to the order information and you can check the note on the file of the sales data.

##### Sales data
Sales data is stored in a json.file under sales_records. Data shows what the customer ordered, total, time, and payment method. 
     

## Used Technolgy
- Python
- QTPY
- Python Class Object    

## Credits 
Two icons comes from this website https://p.yusukekamiyamane.com/

## Reference 
I referred to [Codemy channel](https://www.youtube.com/c/Codemycom) on Youtube, to learn how to use QTPY.
   
Lastly, I really appreciate the Harvard universiy and David Malan for such a high quality free online course. Without your support, I will not be able to make this application.  
