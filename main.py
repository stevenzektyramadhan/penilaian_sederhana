from libs import title_program
from libs import grade_nilai

title_program()

# meminta nilai dari user
jumlah_matkul = 10
list_nilai = []
i = 0

while i < jumlah_matkul :
    inputan = float(input(f"Masukkan nilai ke-{i+1}: "))
    i = i+1
    list_nilai.append(inputan)
    
#  Menghitung nilai rata-rata
total = sum(list_nilai)
average = total / len(list_nilai)

grade_nilai(average)
