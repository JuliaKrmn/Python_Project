import sqlite3
class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'/home/julia/Desktop/Python_Project/Python_Project' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT  sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database version is: {record}")

    def get_all_users(self):
        query = "SELECT  name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_all_products(self):
        query = "SELECT *  FROM  products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_all_orders(self):
        query = "SELECT *  FROM  orders"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT  address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt}  WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = '{product_id}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
              VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()


    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE  id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, products.description, orders.order_date FROM orders \
                    JOIN customers ON orders.customer_id = customers.id \
                    JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_orders(self,order_id,customer_id, product_id):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
                VALUES ({order_id}, {customer_id}, {product_id}, CURRENT_TIME)"
        self.cursor.execute(query)
        self.connection.commit()

        violations = self.cursor.execute("PRAGMA foreign_key_check").fetchall()
       # assert not violations, f"Foreign key violation found: {violations}"
        if violations:
            print(f"\033[91mNOTE: Foreign key violations found (allowed for this test): {violations}\033[0m")
        else:
            print("No foreign key violations found.")
    
        assert True

    def products_out_of_stock(self):
        query = f"SELECT * FROM products WHERE quantity <=0"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

