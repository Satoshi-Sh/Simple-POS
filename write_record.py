import os.path
import json
import datetime

def main():
    now = datetime.datetime.now()
    dt_string = now.strftime("%m-%d-%Y %H:%M:%S")
    #write_record('sushiya',data={"items":[{"Tuna":2.00},{"Salmon":4.00}],'total':6.00,"Cash":True,"time":dt_string})


def write_record(restaurant, data):
    with open(f'sales_records/{restaurant}.json','r+') as file:
           file_data = json.load(file)
           file_data["orders"].append(data)
           file.seek(0)
           json.dump(file_data,file, indent=4)

  
if __name__ =="__main__":
    main()