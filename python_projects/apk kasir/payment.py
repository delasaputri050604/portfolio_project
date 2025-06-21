import mysql.connector
from tkinter import messagebox
from db import get_db_connection
from utils.receipt import save_and_open_receipt

def process_payment(cart, total_price, payment_str):
    if not cart:
        messagebox.showwarning("Keranjang Kosong", "Keranjang masih kosong!")
        return False

    try:
        # Bersihkan input dari tanda baca sebelum konversi
        payment = float(payment_str.replace(".", "").replace(",", ""))
    except ValueError:
        messagebox.showwarning("Input Salah", "Jumlah pembayaran tidak valid.")
        return False

    if payment < total_price:
        messagebox.showwarning("Pembayaran Kurang", "Uang yang dibayar kurang dari total.")
        return False

    change = payment - total_price

    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO transactions (total_price, payment, change_amount) VALUES (%s, %s, %s)",
            (total_price, payment, change)
        )
        transaction_id = cursor.lastrowid

        for item in cart:
            cursor.execute(
                "INSERT INTO transaction_items (transaction_id, product_name, quantity, price) VALUES (%s, %s, %s, %s)",
                (transaction_id, item['name'], item['qty'], item['price'])
            )
        conn.commit()

        # Panggil fungsi simpan dan buka struk
        save_and_open_receipt(transaction_id, cart, total_price, payment, change)
        messagebox.showinfo("Sukses", "Transaksi berhasil dan struk tersimpan.")
        return True

    except mysql.connector.Error as err:
        conn.rollback()
        messagebox.showerror("Error Database", f"Gagal menyimpan transaksi: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
