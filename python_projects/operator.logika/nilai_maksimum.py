print("Nilai Maksimum dari dua bilangan")
a = int(input("\nMasukan bilangan ke-1: "))
b = int(input("Masukan bilangan ke-2: "))

if a > b:
    maks = b
else:
    maks = b

c = int(input("Masukan bilangan ke-3: "))
if c > maks:
    maks = c
else:
    maks = c

d = int(input("Masukan bilangan ke-4: "))
if d > maks:
    maks = d
else:
    maks = d

print("\nNilai maksimum adalah %d" % maks)