from kel1 import cek_kelulusan

while True:
    try:
        nilai = int(input("Masukkan nilai ujian (0-100): "))
        if 0 <= nilai <= 100:
            print("Hasil kelulusan:", cek_kelulusan(nilai))
        else:
            print("Nilai harus antara 0 sampai 100.")
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat antara 0 sampai 100.")
