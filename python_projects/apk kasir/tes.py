import mysql.connector

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Ganti jika ada password
    'database': 'cashier_db'
}

try:
    # Mencoba untuk membuat koneksi
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Contoh query untuk mengambil data
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()

    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
