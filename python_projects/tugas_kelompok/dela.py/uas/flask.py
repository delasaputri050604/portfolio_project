import tkinter as tk
from tkinter import messagebox

produk = {
    'Powder': 45000,
    'Cushion': 53000,
    'Lipstik': 23000
}

def hitung_total():
    nama = var_produk.get()
    try:
        jumlah = int(entry_jumlah.get())
        total = produk[nama] * jumlah
        label_total.config(text=f"Total Harga: Rp {total}")
    except:
        messagebox.showerror("Error", "Jumlah harus angka!")

# Setup window
window = tk.Tk()
window.title("Aplikasi Kasir Dela")

# Pilih produk
tk.Label(window, text="Pilih Produk:").pack()
var_produk = tk.StringVar(window)
var_produk.set("Powder")  # default
tk.OptionMenu(window, var_produk, *produk.keys()).pack()

# Jumlah
tk.Label(window, text="Jumlah:").pack()
entry_jumlah = tk.Entry(window)
entry_jumlah.pack()

# Tombol hitung
tk.Button(window, text="Hitung Total", command=hitung_total).pack()

# Label total
label_total = tk.Label(window, text="Total Harga: Rp 0")
label_total.pack()

window.mainloop()
