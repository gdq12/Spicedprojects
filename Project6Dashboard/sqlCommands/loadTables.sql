CREATE TABLE categories (category_id SERIAL PRIMARY KEY, category_name VARCHAR(50), description TEXT, picture TEXT);

COPY categories FROM '/path2file/categories.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE customers (customer_id VARCHAR(15), company_name TEXT, contact_name TEXT, contact_title TEXT, address TEXT, city TEXT, region VARCHAR(100), postal_code VARCHAR(10), country VARCHAR(100), phone TEXT, fax Text);

COPY customers FROM '/path2file/customers.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE employee_territories (employee_id INTEGER, territory_id INTEGER);

COPY employee_territories FROM '/path2file/employee_territories.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE employees (employee_id SERIAL PRIMARY KEY, last_name VARCHAR(50), first_name VARCHAR(50), job_title VARCHAR(100), social_title VARCHAR(10), birth_date TIMESTAMP, hire_date TIMESTAMP, address VARCHAR(100), city VARCHAR(100), region VARCHAR(10), postal_code VARCHAR(10), country VARCHAR(10), home_phone TEXT, extension INTEGER, photo TEXT, notes TEXT, reports_to INTEGER, photo_path TEXT);

COPY employees FROM '/path2file/employees.csv' DELIMITER ',' CSV HEADER NULL as 'NULL';

CREATE TABLE order_details (order_id INTEGER, product_id INTEGER, unit_price REAL, quantity INTEGER, discount REAL);

COPY order_details FROM '/path2file/order_details.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE orders (order_id INTEGER, customer_id VARCHAR(15), employee_id INTEGER, order_date TIMESTAMP, required_date TIMESTAMP, shipped_date TIMESTAMP, ship_via REAL, freight REAL, ship_name VARCHAR(100), ship_address VARCHAR(100), ship_city VARCHAR(100), ship_region VARCHAR(15), ship_postal_code VARCHAR(10), ship_country VARCHAR(20));

COPY orders FROM '/path2file/orders.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE products (product_id INTEGER, product_name VARCHAR(100), supplier_id INTEGER, category_id INTEGER, quantity_per_unit TEXT, unit_price REAL, units_in_stock INTEGER, units_on_order INTEGER, reorder_level INTEGER, discontinued INTEGER);

COPY products FROM '/path2file/products.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE regions (region_id SERIAL PRIMARY KEY, region_description VARCHAR(20));

COPY regions FROM '/path2file/regions.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE shippers (shipper_id SERIAL PRIMARY KEY, company_name VARCHAR(50), phone TEXT);

COPY shippers FROM '/path2file/shippers.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE suppliers (supplier_id SERIAL PRIMARY KEY, company_name VARCHAR(100), contact_name VARCHAR(100), contact_title VARCHAR(100), address TEXT, city VARCHAR(50), region VARCHAR(20), postal_code VARCHAR(10), country VARCHAR(20), phone TEXT, fax TEXT, home_page TEXT);

COPY suppliers FROM '/path2file/suppliers.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE territories (territory_id INTEGER, territory_description VARCHAR(100), region_id INTEGER);

COPY territories FROM '/path2file/territories.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE countries (initial VARCHAR(2), latitude REAL, longitude REAL, country TEXT);

COPY countries FROM '/path2file/countries.csv' DELIMITER ',' CSV HEADER;

UPDATE countries SET country=REPLACE(REPLACE(country, 'United States','USA'), 'United Kingdom', 'UK');
