print("=================================")
print("RESPONSI Sistem Operasi")
print("=================================")

a = True
while a != False:
    print("\nKRITERIA PROGRAM")
    print("1. Masukkan Kapasitas RAM")
    print("2. Masukan Total Petabit")
    print("3. RAM Yang Digunakan Oleh Sistem Operasi")
    print("4. RAM Yang Digunakan Oleh Program 1")
    print("5. RAM Yang Digunakan Oleh Program 2")
    print("0. Keluar")

    pilihan = int(input("\nMasukkan pilihan anda: "))

    if pilihan == 0:
        print("====================================")
        print("........TERIMAKASIH........")
        print("====================================")
        a = False

    elif pilihan == 1:
        ("Kapasitas RAM")
        totalRAM = int(input("Kapasitas RAM: "))
        print("Total RAM : ", totalRAM, "(MB)")

    elif pilihan == 2:
        ("Total Petabit")
        totalPetabit = int(input("Total Petabit: "))
        print("Total Petabit: ", totalPetabit, "(MB)")
        petaBit = totalRAM / totalPetabit
        print("Kapasitas per petabit adalah ",petaBit, "MB")

    elif pilihan == 3:
        ("Kapasitas RAM")
        kapsitasRAM = int(input("Kapasitas RAM Sistem Operasi: "))
        print("Kapasitas RAM Sistem Operasi : ", kapsitasRAM, "(MB)")
        RAM = totalPetabit + kapsitasRAM
        print("RAM yang terpakai : ",RAM, "MB")
        sisaRAM = totalRAM - totalPetabit - kapsitasRAM
        print("RAM Yang Tidak Terpakai : ", sisaRAM, "MB")

    elif pilihan == 4:
        ("Kapasitas RAM Program 1")
        ramProgram1 = int(input("RAM yang digunakan Program 1: "))
        petabitnilai1 = int(input("Blok : "))
        blok1  = (totalRAM),ramProgram1, petabitnilai1 
        print("Jumlah Blok Yang Bernilai 1: ", (blok1), "(MB)")

    elif pilihan == 5:
        ("Kapasitas RAM Program 2")
        ramProgram2 = int(input("RAM yang digunakan Program 2: "))
        petabitnilai2 = int(input("Blok : "))
        blok2  = (totalRAM),ramProgram2, petabitnilai2 
        print("Jumlah Blok Yang Bernilai 1: ", (blok2), "(MB)")

    else :
        print("Oupsss.. terjadi kesalahan, coba pilih 1,2,3,4,5 untuk memilih kriteria program!")




