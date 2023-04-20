-- SQL-команды для создания таблиц
CREATE TABLE employees (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    title VARCHAR(100),
    birth_date DATE,
    notes TEXT
);

CREATE TABLE customers (
    customer_id VARCHAR(8) unique,
    company_name VARCHAR(100),
    contact_name VARCHAR(100)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    employee_id INTEGER,
    order_date DATE,
    ship_city VARCHAR(100)
);