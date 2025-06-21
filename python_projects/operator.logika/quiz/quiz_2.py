nama = input("Masukkan Nama: ")
nilai_kehadiran = input("masukan kehadiran:")
nilai_tugas = input("Masukkan Nilai Tugas: ")
nilai_uts = input("Masukkan Nilai UTS: ")
nilai_uas = input("Masukkan Nilai UAS: ")

nilai_akhir = (float(nilai_tugas) + float(nilai_uts) + float(nilai_uas)) / 3

if 80 <= nilai_akhir <= 100:
    grade = 'A'
elif 70 <= nilai_akhir < 80:
    grade = 'B'
elif 60 <= nilai_akhir < 70:
    grade = 'C'
elif 50 <= nilai_akhir < 60:
    grade = 'D'
else:
    grade = 'E'

print("\nHasil Program:")
print(f"Nama: {nama}")
print(f"Nilai kehadiran: {nilai_kehadiran}")
print(f"Nilai Tugas: {nilai_tugas}")
print(f"Nilai UTS: {nilai_uts}")
print(f"Nilai UAS: {nilai_uas}")
print(f"Nilai Akhir (Rata-rata): {nilai_akhir}")
print(f"Grade: {grade}")
