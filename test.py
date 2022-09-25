import pandas as pd
import mysql.connector
df = pd.DataFrame()
conn = mysql.connector.connect(host='localhost', database='shop', user='root', password='1234',autocommit=True)
cursor = conn.cursor()
def inventory():
    results = cursor.execute('select * from  items')
    row = cursor.fetchall()
    df = pd.DataFrame(row,columns= ['name','quantity','price'])
    if df.empty ==True:
        print("There is no Items in the databases")
    else:
        print('------------------View Items------------------')
        print('The number of items in the inventory are : ',len(df),'\n')
        print('Here are all the items available in the supermarket.')
        print (df.to_string(index = False))
   
def add_items():
    print('\n','------------------Add items------------------')
    print('To add an item fill in the form')
    name = input('Item name : ')
    while True:
        try:
            qty = int(input('Item quantity : '))
            break
        except ValueError:
            print('Quantity should only be in digits')
    while True:
        price = input('Enter the price : ')
        if price.isdigit()==True: 
            if price =='0' or price <'0':
                print("Enter a non zero number ")
                continue
            else:
                break
        else:
            print("Enter a number")
    val = (name,qty,price)
    sql = "insert into items (name,quantity,price) values(%s,%s,%s)"
    cursor.execute(sql,val)
    print('Item has been successfully added.')
    
def pur():
        sum= 0
        while True:
                print('------------------purchase items------------------')
                results = cursor.execute('select * from  items')
                row = cursor.fetchall()
                df = pd.DataFrame(row,columns= ['name','quantity','price'])
                print (df.to_string(index = False))
                purchase_item = input('which item do you want to purchase? Enter name : ').lower()
                query="select * from items where name='"+purchase_item+"'"
                cursor.execute(query)
                rows=cursor.fetchall()
                s = pd.DataFrame(rows,dtype = object).squeeze()
                print(s)
                a=0
                for purchase_item in s:
                        print("The given item is present\n\n")
                        if s[1]!=0:
                                sum = sum + s[2]
                                print("The total bill is : ",sum)
                                cursor.execute('update items set quantity = quantity-1 where name ="'+purchase_item+'";')
                                t = input('would you like to continue buying: \ntype "y" or "n"').lower()
                                
                                a=a+1
                                if t=='y':
                                        break
                                if t=='n':
                                        return
                        
                        else:
                                print("The given item is out of stock")
                                t = input('would you like to continue buying: \ntype "y" or "n"').lower()
                                if t=='y':
                                        a=a+1
                                        break
                                else:
                                        a=a+1
                                        return
                if a==0:
                        print("\nthe item is not present\n\n")

def search():
        ser = input('Enter the item to be sereached ').lower()
        query="select * from items where name='"+ser+"'"
        cursor.execute(query)
        rows=cursor.fetchall()
        s = pd.DataFrame(rows,dtype = object).squeeze()
        a = 0 
        for i in s :
                print('The item named ' + ser + ' is displayed below with its details')
                print(s)
                a=+1
                break
        if a==0:
                print("The given item is not found")
                

def mod():
        print('------------------edit items------------------')
        results = cursor.execute('select * from  items')
        row = cursor.fetchall()
        df = pd.DataFrame(row,columns= ['name','quantity','price'])
        print (df.to_string(index = False))
        while True:
                item_name = input('Enter the name of the item that you want to edit : ').lower()
                query="select * from items where name='"+item_name +"'"
                cursor.execute(query)
                rows=cursor.fetchall()
                s = pd.DataFrame(rows,dtype = object).squeeze()
                a=0
                if s.empty!=True:
                        break
                else:
                        print("The given input is not valid")
                        continue

        print('\n1.   Name  ')
        print('\n2.   Quantity  ')
        print('\n3.   Price  ')
        print('\n\n')
        choice = int(input('Enter your number of choice :'))
        field=''
        if choice ==1:
                field ='name'
        if choice == 2:
                field = 'quantity'
        if choice == 3:
                field = 'price'
        value =input('Enter new value :')
        sql ='update items set '+field+' ="'+value +'" where name ="'+item_name+'";'
        cursor.execute(sql)
        print('\nStudent Record Updated\n\n')
                
               
while True:
    print('\n\n',"----------menu----------")
    print("1. View items ")
    print("2. Add items for sale ")
    print("3. purchase items ")
    print("4. Search items  ")
    print("5. Edit items ")
    print("6. Exit")
    num=int(input("enter your choice: "))
    print('\n')
    if num==1 or num==2 or num==3 or num==4 or num==5 or num==6 :
        if num==1:
            inventory()
        if num==2:
            add_items()
        if num==3:
            pur()
        if num==4:
            search()
        if num==5:
            mod()
        if num==6:
            print("Thank You")
            break
    else :
        print("!! press a correct number ")

