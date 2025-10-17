import sqlite3

# ✅ ডাটাবেজ কানেকশন তৈরি
conn = sqlite3.connect('form_database.db')
cursor = conn.cursor()

# ✅ টেবিল না থাকলে তৈরি করা
cursor.execute('''
    CREATE TABLE IF NOT EXISTS forms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
''')
conn.commit()

# ✅ ডেটা ইনসার্ট করার ফাংশন
def insert_form_data():
    name = input("Name: ")
    email = input("Email: ")
    message = input("Message: ")
    cursor.execute('INSERT INTO forms (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    print("Data saved successfully!\n")

# ✅ সব ডেটা দেখা
def view_all_data():
    cursor.execute('SELECT * FROM forms')
    rows = cursor.fetchall()
    if rows:
        print("\nAll records in the database:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Message: {row[3]}")
    else:
        print("\nNo data found.")
    print()

# ✅ ডেটা আপডেট করার ফাংশন
def update_data():
    view_all_data()
    update_id = input("Enter the ID to update: ")
    new_name = input("New Name: ")
    new_email = input("New Email: ")
    new_message = input("New Message: ")
    cursor.execute('UPDATE forms SET name=?, email=?, message=? WHERE id=?', (new_name, new_email, new_message, update_id))
    conn.commit()
    print("Data updated successfully!\n")

# ✅ ডেটা ডিলিট করার ফাংশন
def delete_data():
    view_all_data()
    delete_id = input("Enter the ID to delete: ")
    cursor.execute('DELETE FROM forms WHERE id=?', (delete_id,))
    conn.commit()
    print("Data deleted successfully!\n")

# ✅ মেনু সিস্টেম
def menu():
    while True:
        print("========= Form Database Menu =========")
        print("1. Insert Data")
        print("2. View All Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        print("======================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert_form_data()
        elif choice == '2':
            view_all_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

# ✅ প্রোগ্রাম চালু করা
menu()

# ✅ কানেকশন বন্ধ করা
conn.close()
