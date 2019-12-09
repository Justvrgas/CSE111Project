import os
import sqlite3
# import tkinter as tk
# from tkinter import *

# top = tk.Tk()

# # Set size of window
# top.geometry("500x700")
# top.resizable(0,0)


# # create background and line that splits the sections
# c = Canvas(top, width=500, height=700, bd=0, highlightthickness=0)
# c.configure(bg = "white")
# c.pack()
# c.create_line(50000,50,0,350, fill = "black")

# # Frame for Query Buttons


# top.mainloop()



# conncect to db
conn = sqlite3.connect("/Users/hectorsmacbookpro/Desktop/FoodTrack/CSE111Project/Phase_2/FoodTracks.db")
c = conn.cursor()
print("CONNECTED TO DB")


def insert():
    print("INSERTED\n")

def delete():
    print("DELETED\n")

def update():
    print("UPDATED\n")

def users():
    query = "SELECT u_name FROM user WHERE u_priority = 'users' "
    c.execute(query)
    # print("USERS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# users()

def admins():
    query = "SELECT u_name FROM user WHERE u_priority = 'admin' "
    c.execute(query)
    print("ADMINS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# admins()

def vendors():
    query = "SELECT v_name FROM vendor "
    c.execute(query)
    print("VENDORS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# vendors()

def truckNames():
    query = "SELECT t_name FROM truck "
    c.execute(query)
    print("TRUCK NAMES: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# truckNames()
    
def listNames():
    query = "SELECT l_name FROM lists"
    c.execute(query)
    print("LIST NAMES: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# listNames()


def joseLists():
    query = "SELECT l_name FROM lists WHERE l_userID = 6"
    c.execute(query)
    print("LIST NAMES: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# joseLists()

def foodType():
    query = "SELECT DISTINCT(ft_name) FROM foodtype"
    c.execute(query)
    print("FOOD TYPES: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# foodType()


def italianTrucks():
    query = "SELECT t_name FROM truck, foodType WHERE t_truckID = ft_truckID AND ft_name = 'italian' "
    c.execute(query)
    print("ITALIAN TRUCKS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# italianTrucks()

def americanTrucks():
    query = "SELECT t_name FROM truck, foodType WHERE t_truckID = ft_truckID AND ft_name = 'american' "
    c.execute(query)
    print("AMERICAN TRUCKS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# americanTrucks()

def chineseTrucks():
    query = "SELECT t_name FROM truck, foodType WHERE t_truckID = ft_truckID AND ft_name = 'chinese' "
    c.execute(query)
    print("CHINESE TRUCKS: \n")
    for i in c.fetchall():
        print(i[0])
    print("\n")

# chineseTrucks()

def truckWithMultipleDrinks():
    query = " SELECT t_name FROM menu, truck WHERE m_truckID = t_truckID GROUP BY m_truckID HAVING COUNT(m_drinks) > 1;"
    c.execute(query)
    print("TRUCKS WITH MULTIPLE DRINKS: \n")
    for i in c.fetchall():
        print(i[0])
       
    print("\n")

# truckWithMultipleDrinks()


def list_count():
    query = "SELECT l_userID, COUNT(*) FROM lists GROUP BY l_userID HAVING COUNT(*) > 1;"
    c.execute(query)
    print("UserID, Number of lists:")
    
    for i in c.fetchall():
        print(i[0], i[1])
    print("\n")

#def get_admins():
#    query = "SELECT u_userID, u_priority FROM user GROUP BY u_userID HAVING u_priority = 'admin';"
#    c.execute(query)
#    print("Users with more than one list:")
#
#    for i in c.fetchall():
#        print(i[0], i[1])
#    print("\n")
#
#def get_users():
#    query = "SELECT u_userID, u_priority FROM user GROUP BY u_userID HAVING u_priority = 'users';"
#    c.execute(query)
#    print("Users with more than one list:")
#
#    for i in c.fetchall():
#        print(i[0], i[1])
#    print("\n")

def truck_greater_one():
    query = "SELECT t_name FROM truck GROUP BY t_name HAVING COUNT(*) > 2;"
    c.execute(query)
    print("Trucks with more than one truck:")
    
    for i in c.fetchall():
        print(i[0])
    print("\n")

def truck_less_one():
    query = "SELECT t_name FROM truck GROUP BY t_name HAVING COUNT(*) < 2;"
    c.execute(query)
    print("Trucks with one truck:")

    for i in c.fetchall():
        print(i[0])
    print("\n")
    
    
def max_vendor():
    query = "SELECT s_vendorID, s_drinks, s_food FROM supplier WHERE s_vendorID IN (SELECT s_vendorID FROM supplier GROUP BY s_vendorID ORDER BY s_vendorID DESC LIMIT 1) ;"
    
    c.execute(query)
    print("Max Foodtruck food/drink purchaser: ")

    for i in c.fetchall():
        print(i[0], i[1], i[2])
    print("\n")
    
    

    
    
#    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#    print("~~~~~~~~~~~MAIN MENU~~~~~~~~~~")
#    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#    print("~~~ENTER NUMBER FROM 1 - 9 ~~~")
#    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#    print()
#
#    print("~~~ 1. INSERT")
#    print("~~~ 2. DELETE")
#    print("~~~ 3. UPDATE")
#    print("~~~ 4. PRINT ALL USER NAMES IN USER TABLE ")
#    print("~~~ 5. PRINT ALL ADMIN NAMES IN USER TABLE ")
#    print("~~~ 6. PRINT ALL VENDOR NAMES IN THE USER TABLE ")
#    print("~~~ 7. PRINTS USERS WITH MORE THAN ONE LIST ~~~")
#    print("~~~ 8. PRINTS TRUCK NAMES WITH MORE THAN ONE TRUCK ")
#    print("~~~ 9. PRINTS TRUCKS NAMES WITH ONE TRUCK")
#    print("~~~10. PRINTS MAX VENDOR WITH PRODUCTS ")
    
   
i = 0

while i != 11:

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~MAIN MENU~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~ENTER NUMBER FROM 1 - 9 ~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    print("~~~ 1. INSERT")
    print("~~~ 2. DELETE")
    print("~~~ 3. UPDATE")
    print("~~~ 4. PRINT ALL USER NAMES IN USER TABLE ")
    print("~~~ 5. PRINT ALL ADMIN NAMES IN USER TABLE ")
    print("~~~ 6. PRINT ALL VENDOR NAMES IN THE USER TABLE ")
    print("~~~ 7. PRINTS USERS WITH MORE THAN ONE LIST ~~~")
    print("~~~ 8. PRINTS TRUCK NAMES WITH MORE THAN ONE TRUCK ")
    print("~~~ 9. PRINTS TRUCKS NAMES WITH ONE TRUCK")
    print("~~~10. PRINTS MAX VENDOR WITH PRODUCTS ")

    i = input("")


    if i == '1':
        insert()
    elif i == '2':
        delete()
    elif i == '3':
        update()
    elif i == '4':
#        print("THE QUERY YOU SELECETED WILL DISPLAY ALL OF THE USERS NAMES IN THE USERS TABLE\nUSERS:")
        users()
    elif i == '5':
        admins()
    elif i == '6':
        vendors()
    elif i == '7':
        list_count()
    elif i == '8':
        truck_greater_one()
    elif i == '9':
        truck_less_one()
    elif i == '10':
        max_vendor()
        
