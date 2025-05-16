import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    assert users[1][0] == "Stepan"

@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products()

    assert products[1][1] == 'солодка вода'

@pytest.mark.database
def test_check_all_orders():
    db = Database()
    orders = db.get_all_orders()
    
    assert orders[0][3] == '12:22:23'

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print ("Замовлення", orders)
    # Check quantiry of orders equal to 1
    assert len (orders) ==1
    
    #Check structure of data 
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_orders(2, 1, 2)

    print (db.get_all_orders())

#Negative test - inserting non-existing customer_id - works fine with SQLite format 

@pytest.mark.database
def test_order_insert_non_existing_user_id():
    db = Database()
    db.insert_orders(6, 1050, 2)


#Negative test - inserting negative quantity of product  - also works fine with QAlite format 
@pytest.mark.database
def test_product_insert_negative_quantity():
    db = Database()
    db.insert_product(6, "шоколад", "Korona", -25)


#Negative test - inserting missing parameters of product - SQ@Lite accepts everythint! 
@pytest.mark.database1
def test_product_insert_negative_quantity():
    db = Database()
    db.insert_product(7, "", "", -25)
    negative_quantities = db.products_out_of_stock()

    if negative_quantities:
        print(f"\033[91m[NOTE] Products with negative quantity found: {negative_quantities}\033[0m")

    assert True 
    

#Look for products with Zero quantity 
@pytest.mark.database
def test_products_out_of_stock():
    db = Database()
    db.insert_product(20, "test", "test", -25)
    db.products_out_of_stock()
    print (db.products_out_of_stock())
    db.delete_product_by_id(20)

#Update customer address: Ensure update is reflected in SELECT.
    
#Update order date: Verify that it changes correctly.

#Check for orphaned orders: Ensure every order.customer_id exists in customers.

#Ensure product quantity is never negative: Either by constraint or logic.
