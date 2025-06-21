import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# -------------------------------
# Koneksi ke Database MySQL
# -------------------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # sesuaikan jika ada password
        database="kasir_db"
    )

# -------------------------------
# Aplikasi Kasir
# -------------------------------
class AplikasiKasir:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#fce4ec")

        self.kategori_var = tk.StringVar()
        self.produk_var = tk.StringVar()
        self.jumlah = tk.IntVar(value=1)
        self.total_harga = 0

        self.setup_style()
        self.setup_ui()
        self.load_kategori()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Custom.TCombobox", fieldbackground="white", background="white", foreground="#333", bordercolor="#4d90fe", relief="solid", borderwidth=1, padding=5)
        style.map("Custom.TCombobox", fieldbackground=[("readonly", "white")])

        style.configure("Custom.Treeview", background="white", fieldbackground="white", foreground="#333", rowheight=24, font=("Arial", 10))
        style.layout("Custom.Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

    def setup_ui(self):
        # Frame Kiri
        frame_kiri = tk.Frame(self.root, bg="white", highlightbackground="#4d90fe", highlightthickness=2)
        frame_kiri.place(x=0, y=0, width=350, height=300)

        tk.Label(frame_kiri, text="Kategori:", bg="white", fg="#333", font=("Helvetica", 11)).place(x=10, y=10)
        self.kategori_cb = ttk.Combobox(frame_kiri, textvariable=self.kategori_var, state="readonly", style="Custom.TCombobox")
        self.kategori_cb.place(x=10, y=35, width=200)
        self.kategori_cb.bind("<<ComboboxSelected>>", self.load_produk)

        tk.Label(frame_kiri, text="Produk:", bg="white", fg="#333", font=("Helvetica", 11)).place(x=10, y=75)
        self.produk_cb = ttk.Combobox(frame_kiri, textvariable=self.produk_var, state="readonly", style="Custom.TCombobox")
        self.produk_cb.place(x=10, y=100, width=200)

        tk.Label(frame_kiri, text="Jumlah:", bg="white", fg="#333", font=("Helvetica", 11)).place(x=10, y=140)
        jumlah_frame = tk.Frame(frame_kiri, bg="white")
        jumlah_frame.place(x=10, y=165)

        tk.Button(jumlah_frame, text="−", bg="#ff8bb3", fg="white", font=("Arial", 11, "bold"), command=self.kurang_jumlah).pack(side="left")
        tk.Entry(jumlah_frame, width=3, textvariable=self.jumlah, justify="center", font=("Arial", 10)).pack(side="left", padx=5)
        tk.Button(jumlah_frame, text="+", bg="#ff8bb3", fg="white", font=("Arial", 11, "bold"), command=self.tambah_jumlah).pack(side="left")

        tk.Button(frame_kiri, text="Tambah ke Keranjang", bg="#ff5fa2", fg="white", font=("Helvetica", 11, "bold"), command=self.tambah_keranjang).place(x=10, y=220, width=220, height=35)

        # Frame Kanan
        frame_kanan = tk.Frame(self.root, bg="#cfe9ff", highlightbackground="#4d90fe", highlightthickness=2)
        frame_kanan.place(x=370, y=0, width=350, height=300)

        tk.Label(frame_kanan, text="Keranjang", bg="#cfe9ff", font=("Helvetica", 12, "bold")).place(x=10, y=10)
        self.keranjang = ttk.Treeview(frame_kanan, columns=("Produk", "Jumlah"), show="headings", style="Custom.Treeview")
        self.keranjang.heading("Produk", text="Produk")
        self.keranjang.heading("Jumlah", text="Jumlah")
        self.keranjang.column("Produk", width=180)
        self.keranjang.column("Jumlah", width=80)
        self.keranjang.place(x=10, y=40, width=330, height=240)

        # Frame Bawah
        frame_bawah = tk.Frame(self.root, bg="white", highlightbackground="#4d90fe", highlightthickness=2)
        frame_bawah.place(x=0, y=310, width=720, height=110)

        tk.Label(frame_bawah, text="Total Harga:", bg="white", font=("Helvetica", 11)).place(x=10, y=10)
        self.label_total = tk.Label(frame_bawah, text="Rp 0", bg="white", font=("Helvetica", 11, "bold"))
        self.label_total.place(x=120, y=10)

        tk.Label(frame_bawah, text="Bayar:", bg="white", font=("Helvetica", 11)).place(x=10, y=50)
        self.bayar_entry = tk.Entry(frame_bawah, font=("Arial", 10))
        self.bayar_entry.place(x=120, y=50, width=150)

        tk.Button(frame_bawah, text="Bayar", bg="#4d90fe", fg="white", font=("Helvetica", 11, "bold"), command=self.bayar).place(x=350, y=15, width=100, height=35)
        tk.Button(frame_bawah, text="Bersihkan", bg="#ff8bb3", fg="white", font=("Helvetica", 11, "bold"), command=self.bersihkan).place(x=350, y=60, width=100, height=35)

    def load_kategori(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nama_kategori FROM kategori")
        hasil = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.kategori_cb['values'] = hasil

    def load_produk(self, event=None):
        kategori = self.kategori_var.get()
        conn = connect_db()
        cursor = conn.cursor()
        query = """SELECT p.nama_produk FROM produk p JOIN kategori k ON p.id_kategori = k.id_kategori WHERE k.nama_kategori = %s"""
        cursor.execute(query, (kategori,))
        hasil = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.produk_cb['values'] = hasil
        self.produk_cb.set("")

    def tambah_jumlah(self):
        self.jumlah.set(self.jumlah.get() + 1)

    def kurang_jumlah(self):
        if self.jumlah.get() > 1:
            self.jumlah.set(self.jumlah.get() - 1)

    def tambah_keranjang(self):
        produk = self.produk_var.get()
        jumlah = self.jumlah.get()
        if not produk:
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT harga FROM produk WHERE nama_produk = %s", (produk,))
        result = cursor.fetchone()
        conn.close()
        if result:
            harga = result[0]
            self.keranjang.insert("", "end", values=(produk, jumlah))
            self.total_harga += harga * jumlah
            self.label_total.config(text=f"Rp {self.total_harga:,.0f}".replace(",", "."))
            self.jumlah.set(1)

    def bayar(self):
        try:
            bayar = int(self.bayar_entry.get() or 0)
        except ValueError:
            messagebox.showwarning("Kesalahan", "Masukkan angka di kolom Bayar!")
            return

        kembalian = bayar - self.total_harga
        if kembalian < 0:
            messagebox.showwarning("Kurang", "Uang bayar kurang!")
        else:
            messagebox.showinfo("Sukses", f"Transaksi berhasil!\nKembalian: Rp {kembalian:,.0f}".replace(",", "."))
            self.bersihkan()

    def bersihkan(self):
        for item in self.keranjang.get_children():
            self.keranjang.delete(item)
        self.total_harga = 0
        self.label_total.config(text="Rp 0")
        self.bayar_entry.delete(0, tk.END)
        self.produk_cb.set("")
        self.kategori_cb.set("")

# -------------------------------
# Jalankan Aplikasi Fullscreen Tengah
# -------------------------------
# -------------------------------
# Jalankan Aplikasi Fullscreen Tengah
# -------------------------------
def run_kasir():
    root = tk.Tk()
    root.title("Aplikasi Kasir")
    root.attributes("-fullscreen", True)
    root.configure(bg="#fce4ec")
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

    canvas = tk.Frame(root, width=720, height=420, bg="#fce4ec")
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    app = AplikasiKasir(canvas)
    root.mainloop()

if __name__ == "__main__":
    run_kasir()
