print( "LIST PENERBANGAN PESAWAT")
print("kode maskapai | tujuan           | kelas   | harga tiket | kelas    | harga tiket | kelas   | harga tiket|")
print("----------------------------------------------------------------------------------------------------------")
print("3012          | Padang - Jakarta | Ekonomi | Rp.800.000  | Bisnis   | Rp.850.000  | F. Class| Rp.900.000 |")
print("4015          | Padang - Batam   | Ekonomi | Rp.500.000  | Bisnis   | Rp.550.000  | F. Class| Rp.700.000 |")
print("4050          | Padang - Bandung | Ekonomi | Rp.700.000  | Bisnis   | Rp.750.000  | F. Class| Rp.850.000 |")
print("----------------------------------------------------------------------------------------------------------")
print("")
nama = input ("Nama Pembeli :")
umur = input ("Umur Pembeli :")
jenis_kelamin = input("Jenis Kelamin :")
kode_maskapai = input("masukkan kode maskapai anda :")

if kode_maskapai == "3012":
    tujuan = "Padang - Jakarta"
    print ("tujuan : ", tujuan)
    harga_ekonomi = 800000
    harga_bisnis = 850000
    harga_first = 900000
elif kode_maskapai == "4015":
    tujuan = "Padang - Batam"
    print (" tujuan : ", tujuan)
    harga_ekonomi = 500000
    harga_bisnis = 550000
    harga_first = 850000
elif kode_maskapai == "4050":
    tujuan = "Padang - Bandung"
    print (" tujuan :", tujuan,)
    harga_ekonomi = 700000
    harga_bisnis = 750000
    harga_first = 850000
else :
    print("tujuan tidak tersedia")

print("jenis kelas")
print("1.ekonomi",(kode_maskapai))
print("2.bisnis",(kode_maskapai))
print("3.first",(kode_maskapai))

kelas= int(input("masukan jenis kelas yanng diinginkan(1,2,3):"))
if kelas == 1 and kode_maskapai:
    jenis_kelas = "ekonomi"
    harga  = harga_ekonomi
    print ("jenis kelas :", jenis_kelas)
elif kelas == 2 and kode_maskapai:
    jenis_kelas = "bisnis"
    harga = harga_bisnis
    print ("jenis kelas :", jenis_kelas)
elif kelas == 3 and kode_maskapai:
     jenis_kelas = "first"
     harga = harga_first
     print ("jenis kelas :", jenis_kelas)

else :
     print("tidak ada kelas")

jumlah_kursi = int(input("masukan jumlah kursi yang dipesan :"))
 
if jumlah_kursi > 3 :
    total = jumlah_kursi * harga
    diskon = total * 0.2
    total = int(total - diskon )
    print ("anda harus membayar", total)
else :
    total = jumlah_kursi * harga
    print ("anda harus membayar", total)

print("=====================================STRUK PEMESANAN TIKET PESAWAT==========================================")
print(f"nama              :",nama)
print(f"umur              :",umur)
print(f"jenis kelamin     :",jenis_kelamin)
print("------------------------------------------------------------------------------------------------------------")
print(f"kode maskapai     :",kode_maskapai)
print(f"jenis kelas       :", kelas)
print(f"tujuan            :",tujuan)
print(f"jumlah kursi      :",jumlah_kursi)
print(f"total harga       : Rp",total)
print("============================================================================================================")