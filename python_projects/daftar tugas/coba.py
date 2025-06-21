def calculator():
    print("Calculator Sederhana")
    print("1. Penambahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    choice = input("Choose operation (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Masukan nomor pertama: "))
        num2 = float(input("Masukan nomor kedua: "))
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid input! Please choose a valid operation.")

calculator()

