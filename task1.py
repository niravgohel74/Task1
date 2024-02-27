import sqlite3

#CREATEING A DATABASE
try:
    conn = sqlite3.connect("mydatabase.db")
    cur = conn.cursor()
    conn.commit()
    print("Database connected")
except Exception as err:
    print("Database not connected", err)

#CREATING TABLES
try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Products(id INTEGER PRIMARY KEY, Product_name TEXT, Product_description TEXT, Product_price FLOAT, Category TEXT, Discount REAL DEFAULT 0.0)''')
    conn.commit()
except Exception as err:
    print("Error Creating Table",err)

#ADDING PRODUCT
def add_product():
    Product_name=input("Enter the Product Name: ")
    Product_description=input("Enter Product Description: ")
    Product_price=int(input("Enter a product price: "))
    Category=input("Enter a category: ")
    Discount=float(input("Enter a discount: "))
    cur.execute('''INSERT INTO Products(Product_name, Product_description, Product_price, Category, Discount) VALUES(?,?,?,?,?)''',(Product_name, Product_description, Product_price, Category, Discount))
    conn.commit()
    print("Product Added Successfully")

#UPDATE PRODUCT
def update_product():
    id=int(input("Enter product id you want to update: "))
    Product_name=input("Enter a new name: ")
    Product_description=input("Enter a new description: ")
    Product_price=int(input("Enter a new price: "))
    Category=input("Enter a new category: ")
    Discount=float(input("Enter a new discount: "))
    cur.execute('''UPDATE Products SET Product_name=?, Product_description=?, Product_price=?, Category=?, Discount=? WHERE id=?''', (Product_name, Product_description, Product_price, Category, Discount, id))
    conn.commit()
    print(f"Product {id} has been updated")

#DELETE PRODUCT
def delete_product():
    id=int(input("Enter a Product ID you want to delete: "))
    cur.execute('''DELETE FROM Products WHERE id=?''', (id,))
    conn.commit()
    print(f"product {id} has been Deleted Successfully")

#VIEW ALL PRODUCT
def view_product():
    cur.execute('''SELECT * FROM Products''')
    Products = cur.fetchall()
    if len(Products) == 0:
        print("No Product Found")
    else:
        for product in Products:
            print(f"ID:{product[0]}, Product_name: {product[1]},Product_description: {product[2]},Product_price: {product[3]},Category: {product[4]},Discount: {product[5]}")
    
    conn.commit()

while True:
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View Product")
    print("5. Exit")

    choice=input("Enter a choice: ")

    if choice == '1':
        add_product()
    elif choice=='2':
        update_product()
    elif choice=='3':
        delete_product()
    elif choice=='4':
        view_product()
    elif choice=='5':
        print("Exiting")
        break
    else:
        print("Invalid input, Enter valid input")
    