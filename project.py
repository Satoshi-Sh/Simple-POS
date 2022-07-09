import json 
import sys 
import os.path
from register import *

def main():
    file = sys.argv[1]
    if check_argv(sys.argv):
         items = read_menu(file)
         items = chunks(items,9)
         app = QtWidgets.QApplication(sys.argv)
         MainWindow = QtWidgets.QMainWindow()
         ui = Ui_MainWindow(menu =items, restaurant = sys.argv[1].split(".")[0])
         ui.setupUi(MainWindow)
         MainWindow.show()
         sys.exit(app.exec_())

def read_menu(menu):
    
    with open(f"menus/{menu}", "r") as file:
        menu = json.load(file)
        # print(json.dump(menu,indent=2))
        items = [] 
        for i in menu["items"]:

            # filter out items out of stock
            if i['available'] == False:
                continue
            # formating the title to fit in the buttons
            if len(i['item'])> 8:
                label = f"{i['item']}:\n ${i['price']}"
            else:
                label = f"{i['item']}: ${i['price']}"
            items.append(label)
        return items

# make lists with length 9
# referred to https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    lsts = []
    for i in range(0, len(lst), n):
        lsts.append(lst[i:i + n])
    # to make the last list with nine elements
    while len(lsts[-1]) < n:
        lsts[-1].append('')
    return lsts

def check_argv(argv):
    if len(argv) !=2:
        print("python read_menu.py jsonfile")
        sys.exit(1)
    elif argv[1].split(".")[-1] != "json":
        print("Invalid file format")
        sys.exit(1)
    else:
        if os.path.exists(f"menus/{argv[1]}"):
            return True        
        else:
            print("File not found..")
            sys.exit(1)


if __name__ == "__main__":
    main()