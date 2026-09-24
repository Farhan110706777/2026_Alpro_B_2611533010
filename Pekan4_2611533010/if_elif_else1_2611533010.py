# Buat file dengan nama if_elif_else1_NIM.py
# Buat program untuk kondisional if
# Buat variabel ditambah 4 digit nim terakhir contoh : ipk_3010
# Program ini menggunakan fungsi input ()

umur_3010 = int(input("Input umur anda: "))
sim_3010 = input("Apakah Anda Sudah Punya sim C : ")[0]

if umur_3010 >= 17 and sim_3010 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

elif umur_3010 >= 17 and sim_3010 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

elif umur_3010 < 17 and sim_3010 == 'y':
    print("Anda Belum Cukup Umur punya sim_3010")

else:
    print("Anda Belum Cukup Umur bawa motor")
print ("Program Selesai")