"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2


def main():
    # Подключение к базе данных
    conn = psycopg2.connect(database="north", user="postgres", password="12345", host="localhost", port="5432")

    try:
        # Загрузка данных из первого CSV-файла
        with open('north_data/customers_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # пропускаем заголовок
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                                (row[0], row[1], row[2]))
            print_data(conn, 'customers')

        # Загрузка данных из второго CSV-файла
        with open('north_data/employees_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # пропускаем заголовок
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES"
                                "(%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))
            print_data(conn, 'employees')

        # Загрузка данных из третьего CSV-файла
        with open('north_data/orders_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # пропускаем заголовок
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES"
                                "(%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))
            print_data(conn, 'orders')

        # Сохранение изменений
        conn.commit()
        print('Данные успешно загружены в базу данных!')

    except Exception as e:
        print(f'Ошибка: {e}')

    finally:
        conn.close()


def print_data(conn, table_name):
    """Вывод данных из таблицы"""
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        print(f"Вывод данных из таблицы {table_name}:")
        for row in rows:
            print(row)


if __name__ == '__main__':
    main()
