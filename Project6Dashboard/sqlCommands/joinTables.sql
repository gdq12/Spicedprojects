--where products come from and go to, lattitude/longitude retrieved from here: https://www.kaggle.com/eidanch/counties-geographic-coordinates
CREATE VIEW product_country AS SELECT t2.product_name, t1.category_name, t2.product_id, t2.supplier_id, SUM(t3.unit_price*t3.quantity), t5.initial, t4.ship_country AS destination_country, t5.latitude, t5.longitude FROM categories t1, products t2, order_details t3, orders t4, countries t5 WHERE t1.category_id=t2.category_id AND t2.product_id=t3.product_id AND t3.order_id=t4.order_id AND t4.ship_country=t5.country GROUP BY t2.product_name, t1.category_name, t2.product_id, t2.supplier_id, t5.initial, destination_country, t5.latitude, t5.longitude; 

--employee age, report to and their sales 
​CREATE VIEW employee_revenue AS SELECT t2.employee_id, t2.job_title, t2.last_name, t2.hire_date, DATE_PART('year',AGE(t2.hire_date, t2.birth_date)) AS hiring_age, t2.reports_to, SUM(t3.unit_price*t3.quantity) AS total_revenue, t3.discount FROM orders t1 JOIN employees t2 ON t1.employee_id=t2.employee_id JOIN order_details t3 ON t1.order_id=t3.order_id GROUP BY t2.employee_id, t2.job_title, t2.last_name, hiring_age, t2.reports_to, t3.discount ORDER BY total_revenue DESC;

--how fast were the products shipped and relationship on how much customer paid for it 
CREATE VIEW shipping_time AS SELECT t2.order_id, t1.order_date, t1.shipped_date, AGE(t1.shipped_date, t1.order_date) AS time_length, t1.ship_country, AVG(t2.unit_price*t2.quantity) FROM orders t1 JOIN order_details t2 ON t1.order_id=t2.order_id WHERE AGE(t1.shipped_date, t1.order_date) IS NOT NULL GROUP BY t2.order_id, t1.order_date, t1.shipped_date, t1.ship_country;

--Other interesting questions to answer:

--find the hiring age of each employee
SELECT first_name, last_name, DATE_PART('year',AGE(hire_date, birth_date)) FROM employees;

-- Which company is the best customer?
​SELECT o1.customer_id, o1.ship_country AS customer_country, o1.order_id, SUM(o2.unit_price) FROM orders o1 JOIN order_details o2 ON o1.order_id=o2.order_id GROUP BY o1.customer_id, o1.ship_country, o1.order_id ORDER BY sum DESC;

-- Which employee is making the most money?
​SELECT t2.first_name, t2.last_name, SUM(t3.unit_price*t3.quantity) FROM orders t1 JOIN employees t2 ON t1.employee_id=t2.employee_id JOIN order_details t3 ON t1.order_id=t3.order_id GROUP BY t2.first_name, t2.last_name ORDER BY sum DESC;
​
-- Which products generate the most/least revenue?
​SELECT t1.product_name, SUM(t2.unit_price*t2.quantity) FROM products t1 JOIN order_details t2 ON t1.product_id=t2.product_id GROUP BY t1.product_name ORDER BY sum;

SELECT t1.product_name, SUM(t2.unit_price*t2.quantity) FROM products t1 JOIN order_details t2 ON t1.product_id=t2.product_id GROUP BY t1.product_name ORDER BY sum DESC;

-- Are unit prices the same as unit prices per order?
SELECT t1.product_name, t1.unit_price AS price_listed, t2.unit_price AS price_sold FROM products t1 JOIN order_details t2 ON t1.product_id=t2.product_id WHERE t1.unit_price <> t2.unit_price;







