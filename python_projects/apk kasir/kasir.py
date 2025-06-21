import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
import platform
import subprocess

# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cashier_db'
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        messagebox.showerror("Koneksi Gagal", f"Error: {err}")
        return None

class CashierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir Pastel")
        self.cart = []
        self.total_price = 0

        # Set warna latar belakang utama
        self.root.configure(bg="#B3D9FF")  # biru pastel

        self.setup_style()
        self.create_widgets()
        self.load_products()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("default")

        # Styling frame dan label sesuai tema biru pastel
        style.configure("TLabelframe", background="#B3D9FF", foreground="#000080", font=("Arial", 10, "bold"))
        style.configure("TLabelframe.Label", background="#B3D9FF", foreground="#000080")
        style.configure("TLabel", background="#B3D9FF", foreground="#000080", font=("Arial", 10))
        style.configure("TButton", background="#FFFFFF", foreground="#000080", font=("Arial", 10, "bold"), padding=5)
        style.map("TButton", background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")])

    def create_widgets(self):
        # Frame produk untuk pilih produk dan jumlah
        frame_produk = ttk.LabelFrame(self.root, text="Pilih Produk")
        frame_produk.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame_produk, text="Produk:").grid(row=0, column=0, padx=5, pady=5)
        self.product_cb = ttk.Combobox(frame_produk, state="readonly", width=35)
        self.product_cb.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_produk, text="Jumlah:").grid(row=0, column=2, padx=5, pady=5)
        self.qty_var = tk.IntVar(value=1)
        self.qty_spin = ttk.Spinbox(frame_produk, from_=1, to=100, textvariable=self.qty_var, width=5)
        self.qty_spin.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(frame_produk, text="Tambah ke Keranjang", command=self.add_to_cart).grid(row=0, column=4, padx=10)

        # Frame keranjang
        frame_cart = ttk.LabelFrame(self.root, text="Keranjang")
        frame_cart.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        columns = ("Produk", "Harga", "Jumlah", "Subtotal")
        self.cart_tree = ttk.Treeview(frame_cart, columns=columns, show="headings", height=8)
        for col in columns:
            self.cart_tree.heading(col, text=col)
            self.cart_tree.column(col, anchor="center")
        self.cart_tree.pack(fill="both", expand=True)

        # Frame pembayaran
        frame_bayar = ttk.Frame(self.root)
        frame_bayar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame_bayar, text="Total Harga:").grid(row=0, column=0, padx=5, sticky="w")
        self.total_label = ttk.Label(frame_bayar, text="Rp 0")
        self.total_label.grid(row=0, column=1, sticky="w")

        ttk.Label(frame_bayar, text="Bayar:").grid(row=1, column=0, padx=5, sticky="w")
        self.pay_var = tk.StringVar()
        self.pay_entry = ttk.Entry(frame_bayar, textvariable=self.pay_var)
        self.pay_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_bayar, text="Bayar", command=self.process_payment).grid(row=1, column=2, padx=10)

        ttk.Label(frame_bayar, text="Kembalian:").grid(row=2, column=0, sticky="w")
        self.change_label = ttk.Label(frame_bayar, text="Rp 0")
        self.change_label.grid(row=2, column=1, sticky="w")

        ttk.Button(frame_bayar, text="Bersihkan Keranjang", command=self.clear_cart).grid(row=3, column=0, columnspan=3, pady=10)

        # Agar frame keranjang bisa stretch vertikal
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def load_products(self):
        conn = get_db_connection()
        if not conn:
            return
        cursor = conn.cursor()
        # Ambil produk berdasarkan nama, ID minimal agar unik
        cursor.execute("SELECT MIN(id), name FROM products GROUP BY name ORDER BY name")
        rows = cursor.fetchall()
        self.products = {name: pid for pid, name in rows}
        self.product_cb['values'] = list(self.products.keys())
        if rows:
            self.product_cb.current(0)
        cursor.close()
        conn.close()

    def add_to_cart(self):
        name = self.product_cb.get()
        qty = self.qty_var.get()
        if not name or qty < 1:
            messagebox.showwarning("Peringatan", "Pilih produk dan jumlah yang benar.")
            return

        conn = get_db_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT price FROM products WHERE id=%s", (self.products[name],))
        result = cursor.fetchone()
        conn.close()

        if not result:
            messagebox.showerror("Error", "Produk tidak ditemukan.")
            return

        price = float(result[0])
        subtotal = price * qty

        # Tambah ke list keranjang
        self.cart.append({'name': name, 'qty': qty, 'price': price, 'subtotal': subtotal})
        self.update_cart()

    def update_cart(self):
        # Hapus isi treeview dulu
        for i in self.cart_tree.get_children():
            self.cart_tree.delete(i)

        self.total_price = 0
        for item in self.cart:
            self.total_price += item['subtotal']
            self.cart_tree.insert("", "end", values=(
                item['name'],
                f"Rp {item['price']:,}".replace(',', '.'),
                item['qty'],
                f"Rp {item['subtotal']:,}".replace(',', '.')
            ))
        self.total_label.config(text=f"Rp {self.total_price:,.0f}".replace(',', '.'))

    def clear_cart(self):
        self.cart.clear()
        self.update_cart()
        self.pay_var.set("")
        self.change_label.config(text="Rp 0")

    def process_payment(self):
        if not self.cart:
            messagebox.showwarning("Kosong", "Keranjang masih kosong!")
            return

        try:
            # Hapus format ribuan dan ubah ke float
            bayar = float(self.pay_var.get().replace(".", "").replace(",", ""))
        except ValueError:
            messagebox.showwarning("Salah", "Input pembayaran tidak valid.")
            return

        if bayar < self.total_price:
            messagebox.showwarning("Kurang", "Pembayaran kurang dari total.")
            return

        kembalian = bayar - self.total_price
        self.change_label.config(text=f"Rp {kembalian:,.0f}".replace(',', '.'))

        conn = get_db_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            # Simpan transaksi
            cursor.execute("INSERT INTO transactions (total_price, payment, change_amount) VALUES (%s, %s, %s)",
                           (self.total_price, bayar, kembalian))
            trans_id = cursor.lastrowid

            # Simpan detail transaksi
            for item in self.cart:
                cursor.execute(
                    "INSERT INTO transaction_items (transaction_id, product_name, quantity, price) VALUES (%s, %s, %s, %s)",
                    (trans_id, item['name'], item['qty'], item['price'])
                )
            conn.commit()

            # Simpan struk ke file dan buka otomatis
            self.save_receipt(trans_id, bayar, kembalian)

            messagebox.showinfo("Berhasil", "Transaksi disimpan.")
            self.clear_cart()
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"Gagal menyimpan transaksi.\n{e}")
        finally:
            cursor.close()
            conn.close()

    def save_receipt(self, trans_id, bayar, kembalian):
        filename = f"struk_{trans_id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== STRUK PEMBELIAN ===\n")
            for item in self.cart:
                f.write(f"{item['name']} x{item['qty']} @ Rp {item['price']:,.0f} = Rp {item['subtotal']:,.0f}\n".replace(',', '.'))
            f.write(f"\nTotal: Rp {self.total_price:,.0f}\n".replace(',', '.'))
            f.write(f"Bayar: Rp {bayar:,.0f}\n".replace(',', '.'))
            f.write(f"Kembali: Rp {kembalian:,.0f}\n".replace(',', '.'))
            f.write("=========================\n")

        # Buka file struk otomatis sesuai OS
        try:
            if platform.system() == "Windows":
                os.startfile(filename)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", filename])
            else:  # Linux dan lainnya
                subprocess.run(["xdg-open", filename])
        except Exception as e:
            messagebox.showwarning("Warning", f"Struk sudah disimpan tapi gagal dibuka otomatis.\n{e}")

def main():
    root = tk.Tk()
    app = CashierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
