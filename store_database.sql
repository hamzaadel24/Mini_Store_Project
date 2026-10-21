create table customers(
customer_id int primary key,
name VARCHAR (100),
city varchar (100)
);

create table orders(
order_id int primary key,
customer_id int,
price int,
foreign key (customer_id) REFERENCES customers (customer_id)
);


insert into customers(customer_id, name,city)values(1,'Ahmed', 'Cairo')
insert into orders (order_id,customer_id,price)values(1,1,250)
insert into customers(customer_id, name,city)values(2,'Sara', 'Alex')
insert into orders (order_id,customer_id,price)values(2,2,400)
insert into customers(customer_id, name,city)values(5,'Ali', 'Alex')
insert into orders (order_id,customer_id,price)values(5,5,150)
insert into customers(customer_id, name,city)values(6,'Nour', 'Giza')
insert into orders (order_id,customer_id,price)values(6,6,600)


select *
from orders
where price > 200

select customers.name, sum(orders.price) as total_price
from customers
join orders on customers.customer_id = orders.customer_id
group by customers."name" 

