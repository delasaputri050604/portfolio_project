import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os
import sys

# Import kelas 

from kasir import CashierApp

# Konfigurasi koneksi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cashier_db'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry("350x400")
        self.root.configure(bg="#B3D9FF")  # Warna biru pastel

        self.create_widgets()

    def create_widgets(self):
        try:
            self.logo_img = tk.PhotoImage(file="logo.png")
            logo_label = tk.Label(self.root, image=self.logo_img, bg="#B3D9FF")
            logo_label.pack(pady=20)
        except Exception as e:
            print("Logo tidak ditemukan:", e)

        tk.Label(self.root, text="Username:", bg="#B3D9FF", font=("Helvetica", 10)).pack(pady=5)
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#B3D9FF", font=("Helvetica", 10)).pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack(pady=5)

        login_btn = tk.Button(self.root, text="Login", command=self.check_login, bg="#ff99cc", fg="white", width=15)
        login_btn.pack(pady=20)

    def check_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
            return

        conn = get_db_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Sukses", "Login berhasil!")
                self.open_cashier()
            else:
                messagebox.showerror("Gagal", "Username atau password salah!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error DB", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def open_cashier(self):
        # Tutup jendela login
        self.root.destroy()
        # Buka jendela baru untuk kasir
        root_kasir = tk.Tk()
        app = CashierApp(root_kasir)
        root_kasir.mainloop()


def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
