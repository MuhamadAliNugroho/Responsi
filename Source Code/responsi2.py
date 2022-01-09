programs = {
    "Mail" : 5,
    "Chrome" : 10,
    "Vscode" : 15
}

def jalan1(program1, proses1):
    programs[program1] = proses1
    print("Program", program1, "dengan jatah waktu", proses1, "berhasil dimasukkan!\n")

def jalan2(program2, proses2):
    programs[program2] = proses2
    print("Program", program2, "dengan jatah waktu", proses2, "berhasil dimasukkan!\n")

def jalan3(program3, proses3):
    programs[program3] = proses3
    print("Program", program3, "dengan jatah waktu", proses3, "berhasil dimasukkan!")


def sort():
    return sorted(programs.items(), key=lambda item: item[1], reverse=False)

a = True

while a != False:
    print("============================================================")
    print("~~~~~Selamat Datang Di Algortima Round Robin~~~~~")
    print("============================================================")
    print("Daftar Menu Program: ")
    print("1. Masukkan program baru")
    print("2. Daftar Program Dan Quantum Time")
    print("3. Daftar Program Lama Proses Dari Yang Terkecil")
    print("0. Keluar")

    pilihan = int(input("\nMasukkan pilihan anda: "))

    if pilihan == 0:
        print("============================================================")
        print("~~~~~~~~~~TERIMKASIH SUDAH MENGGUNAKAN PROGRAM INI~~~~~~~~~~")
        print("============================================================")
        a = False

    elif pilihan == 1:
        ("Masukkan Program Baru")
        program1 = str(input("Masukkan nama program 1: "))
        proses1 = int(input("Masukkan Quantum Time 1: \t"))
        program2 = str(input("Masukkan nama program 2: "))
        proses2 = int(input("Masukkan Quantum Time 2: \t"))
        program3 = str(input("Masukkan nama program 3: "))
        proses3 = int(input("Masukkan Quantum Time 3: \t"))
        print("============================================================")
        jalan1(program1, proses1)
        jalan2(program2, proses2)
        jalan3(program3, proses3)
        print("============================================================")

    elif pilihan == 2:
        print("============================================================")
        ("Daftar Program Berdasarkan Quantum Time")
        for key, value in programs.items():
            print('Nama Program : {}\t Waktu Pemrosesan: {}'.format(key, value))

    elif pilihan == 3:
        print("============================================================")
        ("Daftar Lama Proses Pengerjaan Program Dari Yaang Terkecil")
        MAN = sort()
        for key, value in MAN:
            print('Nama Program : {}\tWaktu Pemrosesan: {}'.format(key,value))

    else :
        print("Oupsss.. terjadi kesalahan, coba pilih 1,2,3, untuk memilih program!")

    