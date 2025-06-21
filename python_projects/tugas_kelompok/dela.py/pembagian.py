def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian dengan nol tidak diperbolehkan"

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print(f"Hasil pembagian: {a} / {b} = {pembagian(a, b)}")
