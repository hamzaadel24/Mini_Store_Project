raw_orders = [
    {"id": 1, "customer_name": "Ahmed", "city": "Cairo", "price": 250},
    {"id": 2, "customer_name": "Sara", "city": "Alex", "price": 400},
    {"id": 3, "customer_name": "Omar", "city": "Giza", "price": -50},     
    {"id": 4, "customer_name": "Mona", "city": "Cairo", "price": None},    
    {"id": 5, "customer_name": "Ali", "city": "Alex", "price": 150},
    {"id": 6, "customer_name": "Nour", "city": "Giza", "price": 600}
]
#print(raw_orders)

def clean_orders(data):
    cleaned_list = []
    for order in data:
        price = order.get("price")
        if price is None or price <= 0:
            continue
        cleaned_list.append(order)
    return cleaned_list
cleaned_data= clean_orders(raw_orders)

print("valid orders count :", len(cleaned_data))


def generate_sql_insert(clean_data):
    print("insert statement in database")

    for order in clean_data:
        customer_sql = f"insert into customers(customer_id, name,city)values({order['id']},'{order['customer_name']}', '{order['city']}')"
        print(customer_sql)


        order_sql =f"insert into orders (order_id,customer_id,price)values({order['id']},{order['id']},{order['price']})" 
        print(order_sql) 


cleaned_data= clean_orders(raw_orders)
print("vaild orders count",len(cleaned_data))
generate_sql_insert(cleaned_data)