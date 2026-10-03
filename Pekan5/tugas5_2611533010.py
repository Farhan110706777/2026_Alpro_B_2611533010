print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_3010 = int(input("Masukkan ukuran skala jam pasir (N): "))

# 1. Bingkai Pembatas Horizontal (Border Atas)
print("#", end="")
for i_3010 in range(4 * n_3010 + 5):
    print("=", end="")
print("#")

# 2. Fase 1: Jam Pasir Atas (Reduksi Angka Menurun: Baris N turun s.d. 1)
for baris_3010 in range(n_3010, 0, -1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for spasi_3010 in range(2 * (n_3010 - baris_3010)):
        print(" ", end="")
        
    # Deret angka mundur
    for angka_3010 in range(baris_3010, 0, -1):
        print(angka_3010, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju
    for angka_3010 in range(1, baris_3010 + 1):
        print(" ", end="")
        print(angka_3010, end="")
        
    # Spasi penyeimbang kanan
    for spasi_3010 in range(2 * (n_3010 - baris_3010)):
        print(" ", end="")
        
    print(" |")

# 3. Fase 2: Poros Titik Pusat Jam Pasir (Singularity)
print("|", end="")
for spasi_3010 in range(2 * n_3010 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3010 in range(2 * n_3010 + 1):
    print(" ", end="")
print("|")

# 4. Fase 3: Jam Pasir Bawah (Ekspansi Angka Naik: Baris 1 naik s.d. N)
for baris_3010 in range(1, n_3010 + 1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for spasi_3010 in range(2 * (n_3010 - baris_3010)):
        print(" ", end="")
        
    # Deret angka mundur
    for angka_3010 in range(baris_3010, 0, -1):
        print(angka_3010, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju
    for angka_3010 in range(1, baris_3010 + 1):
        print(" ", end="")
        print(angka_3010, end="")
        
    # Spasi penyeimbang kanan
    for spasi_3010 in range(2 * (n_3010 - baris_3010)):
        print(" ", end="")
        
    print(" |")

# 5. Bingkai Pembatas Horizontal (Border Bawah)
print("#", end="")
for i_3010 in range(4 * n_3010 + 5):
    print("=", end="")
print("#")