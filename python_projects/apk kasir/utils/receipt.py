import os
import platform
import subprocess
from tkinter import messagebox

def save_and_open_receipt(transaction_id, cart, total_price, payment, change):
    folder = "receipts"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, f"receipt_{transaction_id}.txt")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("==== STRUK TRANSAKSI ====\n")
            for item in cart:
                f.write(f"{item['name']} x{item['qty']} = Rp {item['subtotal']:,}\n".replace(',', '.'))
            f.write(f"\nTotal Harga: Rp {total_price:,}\n".replace(',', '.'))
            f.write(f"Bayar: Rp {payment:,}\n".replace(',', '.'))
            f.write(f"Kembalian: Rp {change:,}\n".replace(',', '.'))
            f.write("========================\n")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan struk: {e}")
        return

    # Buka file struk otomatis sesuai OS
    try:
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", filename])
        else:  # Linux dan lainnya
            subprocess.call(["xdg-open", filename])
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka file struk: {e}")
