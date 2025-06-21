# login.py
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import main  # pastikan file main.py ada di folder yang sama

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry("350x400")
        self.root.configure(bg="#B3D9FF")  # pastel biru

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

        login_btn = tk.Button(self.root, text="Login", command=self.check_login,
                              bg="#ff99cc", fg="white", width=15)
        login_btn.pack(pady=20)

    def check_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kasir_db"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                messagebox.showinfo("Sukses", "Login berhasil!")
                self.root.destroy()  # tutup login window
                main.run_kasir()     # jalankan aplikasi kasir dari main.py
            else:
                messagebox.showerror("Gagal", "Username atau password salah!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error DB", f"Error: {err}")

def main_login():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main_login()
