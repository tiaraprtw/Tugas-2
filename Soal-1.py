#Program menyimpan kontak
print ("Selamat Datang")
print ("Silakan pilih menu yang tersedia")
menu = ["1. Daftar Kontak", "2. Tambah Kontak", "3. Keluar"]
for x in menu:
    print (x)
print (" ")

teks = int(input("Masukkan pilihan: "))
print(" ")


if teks == 1:
    print ("DAFTAR KONTAK")
elif teks == 2:
    nama = str(input("Nama: "))
    nomor = int(input("nomor: "))
    print ("Kontak berhasil ditambahkan.")

kontak = []
def print_kontak():
    for buah in kontak:
        print(buah)
    print("---")
def tambah(nama):
     kontak.append(nama)
     print_kontak()


