import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # default kosong di XAMPP
    database="db_mahasiswa"
)

cursor = db.cursor()

# Fungsi Tambah
def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama Lengkap: ")
    jurusan = input("Masukkan Jurusan: ")
    sql = "INSERT INTO mahasiswa (nim, `Nama Lengkap`, jurusan) VALUES (%s, %s, %s)"
    val = (nim, nama, jurusan)
    cursor.execute(sql, val)
    db.commit()
    print("✅ Data berhasil ditambahkan.\n")

# Fungsi Lihat
def tampilkan_data():
    cursor.execute("SELECT nim, `Nama Lengkap`, jurusan FROM mahasiswa")
    hasil = cursor.fetchall()
    print("📄 Data Mahasiswa:")
    for row in hasil:
        print(f"NIM: {row[0]}, Nama Lengkap: {row[1]}, Jurusan: {row[2]}")
    print()

# Fungsi Edit
def edit_data():
    nim = input("Masukkan NIM yang ingin diedit: ")
    nama_baru = input("Masukkan Nama Lengkap baru: ")
    jurusan_baru = input("Masukkan Jurusan baru: ")
    sql = "UPDATE mahasiswa SET `Nama Lengkap`=%s, jurusan=%s WHERE nim=%s"
    val = (nama_baru, jurusan_baru, nim)
    cursor.execute(sql, val)
    db.commit()
    print("✅ Data berhasil diperbarui.\n")

# Fungsi Hapus
def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    sql = "DELETE FROM mahasiswa WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql, val)
    db.commit()
    print("🗑️ Data berhasil dihapus.\n")

# Menu Utama
def menu():
    while True:
        print("====== MENU CRUD MAHASISWA ======")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    menu()
