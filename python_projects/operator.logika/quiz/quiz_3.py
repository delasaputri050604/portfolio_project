data = {
    1: "Nama: Andi",
    2: "NIM: 123456",
    3: "sistem informasi",
    4: "Mata Kuliah: apos",
    5: "Kelas: 4 sia 8"
}

while True:

    print("\nPilih data yang ingin ditampilkan:")
    print("1. Nama")
    print("2. NIM")
    print("3. Jurusan")
    print("4. Mata Kuliah")
    print("5. Kelas")

    pilihan = int(input("Masukkan nomor pilihan (1-5): "))

    if pilihan in data:
        print(data[pilihan])
    else:
        print("Pilihan tidak valid!")
