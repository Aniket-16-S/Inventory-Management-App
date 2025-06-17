import sqlite3
import os

DB_FILE = 'inventory.db'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods (
        prd_info VARCHAR(100),
        supp_info VARCHAR(100),
        qty INT,
        mes_unit VARCHAR(10),
        r_p_u INT,
        total_rate INT,
        tax INT
    );
""")
cursor.execute( """
    CREATE TABLE IF NOT EXISTS sales (
        prd_info VARCHAR(100),
        cust_info VARCHAR(100),
        qty INT,
        mes_unit VARCHAR(10),
        r_p_u INT,
        total_rate INT,
        tax INT
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productmaster (
        barcode INT,
        sku_id INT,
        category VARCHAR(15),
        sub_cat VARCHAR(15),
        prd_name VARCHAR(15),
        prd_desc VARCHAR(40),
        tax INT,
        price INT,
        mes_unit VARCHAR(10)  
    );
""")

cursor.execute("""
    SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='users';
""")
result = cursor.fetchone()

if result[0] == 0 :
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(20),
            password VARCHAR(20)   
        );
    """)
    cursor.execute("""
    INSERT INTO users (username, password) VALUES (?, ?)            
    """, ("infoware1", "pass@1"))
    cursor.execute("""
    INSERT INTO users (username, password) VALUES (?, ?)            
    """, ("infoware2", "pass@2"))

conn.commit()
conn.close()

"""
    Images could be stored as binary bolbs in Mysql or Sqlite3
    as :
    with open("image_file_path.jpg", 'rb') as file : # rb -> read mode (binary)
        binary_info = file.read()
    then we can  store binary info as regular string in sql
"""

def store_product_images(image_file_path, sku_id) :
    if not os.path.exists("images"):
        os.makedirs("images")

    with open(image_file_path, 'rb') as file :
        bin_data = file.read()

    final_path = f'images/{sku_id}.jpg' 
    with open(final_path, 'wb') as file :
        file.write(bin_data)
    # os.chmod(final_path, 0o444) # 0o444 => read only. Can be used to set the file read only.

def validate_user(user:tuple) :
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    u_name = user[0]
    query = "SELECT password FROM users WHERE username = ?;"
    cursor.execute(query, (u_name,) )
    result = cursor.fetchone()
    if result != None :
        if result[0] == user[1] :
            return True
        else :
            return False
    else :
        return False
def store_goods(goods_info:tuple) :
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = "INSERT INTO goods (prd_info, supp_info, qty, mes_unit, r_p_u,  total_rate , tax) VALUES (?, ?, ?, ?, ?, ?, ?);"
    cursor.execute(query, goods_info)

    conn.commit()
    conn.close()

def store_sales(sales_info: tuple): 
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = "INSERT INTO sales (prd_info, cust_info, qty, mes_unit, r_p_u,  total_rate, tax) VALUES (?, ?, ?, ?, ?, ?, ?);"
    cursor.execute(query, sales_info)

    conn.commit()
    conn.close()
    

def store_productmaster(prod_info: tuple):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = """
        INSERT INTO productmaster 
        (barcode, sku_id, category, sub_cat, prd_name, prd_desc, tax, price, mes_unit) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cursor.execute(query, prod_info)

    conn.commit()
    conn.close()

def read_goods() :
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM goods;         
    """)
    res = cursor.fetchall()
    return res

def read_sales() :
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM sales;           
    """)
    res = cursor.fetchall()
    return res

def read_productmaster() :
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM productmaster;            
    """)
    res = cursor.fetchall()
    return res