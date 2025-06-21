while True:
    user_input = input("Masukkan angka (atau ketik 'exit' untuk keluar): ")
    
    if user_input.lower() == 'exit':
        print("Program selesai. Terima kasih!")
        break

    try:
        angka = int(user_input)
        if angka % 2 == 0:
            print(f"Angka {angka} adalah genap\n")
        else:
            print(f"Angka {angka} adalah ganjil\n")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka atau 'exit' untuk keluar.\n")
