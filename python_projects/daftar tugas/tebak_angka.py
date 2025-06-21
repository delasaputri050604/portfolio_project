import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)  # Komputer memilih angka acak antara 1-100
    percobaan = 0
    
    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih angka antara 1 sampai 100. Coba tebak!")
    
    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba lagi.")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    tebak_angka()
    input("Tekan Enter untuk keluar...")
