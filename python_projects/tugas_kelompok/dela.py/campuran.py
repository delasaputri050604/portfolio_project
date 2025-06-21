def operasi_campuran(a, b, c):
    return a + b * (c - b) / c

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga (untuk operasi campuran): "))

print(f"Hasil operasi campuran: {a} + {b} * ({c} - {b}) / {c} = {operasi_campuran(a, b, c)}")
