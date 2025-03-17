print ("Tebak - Tebakan  Angka BOM ")
print ("pemain 1")
n = int (input ("pilih angka positif sampai berapa : "))
k = int (input ( "angka bom : "))
for i in range(1,n+1) :
    if i % k == 0 :
        print ("BOM" , end = " ")
    else:
        print(i, end =  " " )

print("\n")
print ("pemain 2")

while True :
    m= int(input (f"tebak angka dari 1 - {n} : "))
    if m < 1 or m > n :
        print ("anda di luar jangkauan , silahkan coba lagi ")
        continue
    elif m  % k == 0 :
        print ("angka" , m, " adalah  BOM , anda  kalah!!")
        break
    else :
        print ("angka", m ,"adalah  bukan BOM, anda menang!!")
        break
