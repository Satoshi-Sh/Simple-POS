# Simple POS
#### Video Demo:  https://youtu.be/HtDdZ87K-to

#### Description:
This application gives simpe POS system to anyone. Program reads a menu file(json), and provide a virtual cash register. You can keep a note on the order. Every order detail are recorded to the a record file. If you are interested, please check the video above. 

#### Background 
This project was made for the CS50P final project. Througout the course, one assignment was about Mexican Taqueria cash register. I enjoyed that problem set so decided to develop from there.

#### Features 
##### menus 
You can update your menu through Json files under menus, as such changing prices, adding new items, remove old items. And also, you can put items unavailable for the time being.
    
##### Register.py and note.py
Register.py is for the main page of this application. You can click buttons to add items to the order. You can search items with back and next button if ordered items are not on the screen. If you need to delete item from the order, you need to click on the del button. The del button displayed red, and you just need to click on the button of the item you need to delete. Once the order is finished, customer may pay cash or cradie/debit. If the customer pay by card, you can just click the received button and then click complete. That's the end of transaction. If the customer pay by cash, you need to type the amount you received and the screen show the change. Once complete is clicked, all the data is sent to the sales record file and the screen goes back to the original state. 

You may keep a note on the order if you press the pencil icon. This button opens another file to keep a note. You just need to type and click save. The note is added to the order information and you can check the note on the file of the sales data.

##### Sales data
Sales data is stored in a json.file under sales_records. Data shows what the customer ordered, total, time, and payment method. 
     

#### Used Technolgy

Python was used for the application. QTPY was used for the user interface. QT designer was also used to user interface. Json was used to read the menu file and record the order detail. 
    
#### Features to be Implemented

Right now the screen space which shows order items is limited. If I spend more time on this project, I will make the screen scrollable first. Adding more useful features will be interesting, like separating the bill for the customers and so on.   

#### Conclusion
    
This was the final project of CS50 Python as mentioned before. I didn't have experience to make a GUI so this was a good start point for me to develop user-friendly applications. When it comes to QTPY, I need to have better understanding of object oriented language. This project definitely suplemented my knoledge about classes. I'm working on web development course as well. So see you there.  



#### Credits 
Two icons comes from this website https://p.yusukekamiyamane.com/


I referred to Codemy channel on Youtube, to make what I want.
    https://www.youtube.com/c/Codemycom ( PyQt5 GUI Thursday) I've never used QTPY before, so it will be impossible to make this application without his tutorial.

Lastly, I really appreciate the Harvard universiy and David Malan for such a high quality free online course. Without your support, I will not be able to make this complicating application. I learned a lot of things. 
