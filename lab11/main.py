import csv
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="tester",
        user="postgres",
        password="daulet2004",
        connect_timeout=10,
        sslmode="prefer"
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(15) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def load_from_csv():
    conn = connect_db()
    cur = conn.cursor()
    with open('C:/Users/User/OneDrive/Рабочий стол/PP2/lab11/phonebook.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                row
            )
    conn.commit()
    cur.close()
    conn.close()

def add_from_console():
    conn = connect_db()
    cur = conn.cursor()
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
        (first_name, last_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    conn = connect_db()
    cur = conn.cursor()
    phone = input("Введите телефон для обновления: ")
    new_first_name = input("Введите новое имя: ")
    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE phone = %s",
        (new_first_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def query_data():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_data():
    conn = connect_db()
    cur = conn.cursor()
    phone_to_delete = input("Введите телефон для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_to_delete,))
    conn.commit()
    cur.close()
    conn.close()

def delete_by_id():
    conn = connect_db()
    cur = conn.cursor()
    try:
        id_to_delete = int(input("Введите ID для удаления: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id_to_delete,))
    if cur.rowcount == 0:
        print("Нет записи с таким ID.")
    else:
        print("Запись успешно удалена.")
    conn.commit()
    cur.close()
    conn.close()

def update_name_and_lastname():
    conn = connect_db()
    cur = conn.cursor()
    try:
        id_to_update = int(input("Введите ID для обновления: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return
    
    new_first_name = input("Введите новое имя: ")
    new_last_name = input("Введите новую фамилию: ")
    
    cur.execute(
        "UPDATE phonebook SET first_name = %s, last_name = %s WHERE id = %s",
        (new_first_name, new_last_name, id_to_update)
    )
    if cur.rowcount == 0:
        print("Нет записи с таким ID.")
    else:
        print("Запись успешно обновлена.")
    conn.commit()
    cur.close()
    conn.close()


def main():
    create_table()
    while True:
        print("\n1. Загрузить данные из CSV")
        print("2. Добавить данные через консоль")
        print("3. Обновить данные")
        print("4. Просмотреть все записи")
        print("5. Удалить данные")
        print("6. Удалить данные по ID")
        print("7. Изменить имя")
        print("8. выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            load_from_csv()
        elif choice == '2':
            add_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            delete_by_id()
        elif choice == '7':
            update_name_and_lastname()
        elif choice == '8':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()