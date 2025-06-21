import mysql.connector

# Koneksi ke database
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Ganti dengan username MySQL Anda
        password='',  # Ganti dengan password MySQL Anda jika ada
        database='cashier_db'
    )
    cursor = connection.cursor()

    # Nama produk yang ingin dicari
    product_name = "Facial Wash"  # Ganti dengan nama produk yang sesuai

    # Mencetak nama produk yang dicari
    print(f"Mencari harga untuk produk: {product_name}")

    # Query untuk mengambil harga produk
    try:
        cursor.execute("SELECT price FROM products WHERE name=%s", (product_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"Harga untuk produk '{product_name}' tidak ditemukan.")
        else:
            price = result[0]
            print(f"Harga produk '{product_name}': {price}")

    except mysql.connector.Error as err:
        print(f"Error saat mengambil data: {err}")

except mysql.connector.Error as err:
    print(f"Error saat koneksi ke database: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
