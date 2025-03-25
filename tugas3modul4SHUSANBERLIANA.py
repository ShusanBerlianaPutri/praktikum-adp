n = 4
while True :
    r = int(input( f"masukan jumlah baris kursi (minimal {n}) :"))
    c = int(input( f"masukan jumlah kolom kursi (minimal {n}) :"))
    if r >= n and c >= n :
        kursi_dipesan = set()
        total_kursi = r * c  
        break
    else:
        print(f"Ukuran minimal bioskop kami adalah {n}x{n}! Silahkan anda coba lagi ")
print()
print("Layout Kursi Bioskop : ")
no_kursi = 1
for i in range(r):
    for j in range(c):
        print(no_kursi, end=" ")
        no_kursi += 1
    print()
while True:
    print()
    pilihan_anda = int(input("masukkan nomor kursi yang ingin anda pesan (atau 0 untuk selesai memilih): "))
    if  pilihan_anda == 0:
        print("Terimakasih anda telah memesan tiket kami!")
        break
    elif pilihan_anda < 1 or pilihan_anda > total_kursi:
        print("nomor kursi tidak tersedia, silahkan anda coba lagi")
    elif pilihan_anda not in kursi_dipesan:
        kursi_dipesan.add(pilihan_anda)
        print(f"kursi {pilihan_anda} berhasil dipesan.")
    else:
        print(f"kursi {pilihan_anda} sudah dipesan!, silahkan anda piih kursi lain!. ")
        
    print("Layout Kursi Bioskop : ")
    no_kursi = 1
    for i in range(r):
        for j in range(c):
            if no_kursi in kursi_dipesan:
                print("X", end=" ")
            else:
                print(no_kursi, end=" ")
            no_kursi += 1
        print()


