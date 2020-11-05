print("---------------------------")
print("  Penjualan Tiket Pesawat  ")
print("---------------------------")

#input
nama=input("nama penumpang  :")
kopes=input("kode pesawat   :")
jumlah=int(input("masukan jumlah tiket:"))

#proses
if   kopes=="1":
    napes="Garuda Indonesia"
    kota="Denpasar"
    harga=2275000
elif kopes=="2":
    napes="Mandala"
    kota="malang"
    harga=1330000
elif kopes=="3":
    napes="Merpati"
    kota="Surabaya"
    harga=1185000
else:
    napes="Lion Air"
    kota="Pontianak"
    harga=1750000

#proses
ubay=harga * jumlah
ppn=10%+jumlah
total=ubay+ppn
ukem=ubay-total
#output
print("--------------------------------------")
print("       Program Penjualan Tiket        ")
print("          Pt. Atour & Travel          ")
print("pesawat yang di pilih : "+napes)
print("rincian penjualan tiket")
print("--------------------------------------")
print("kota tujuan : "+kota)
print("harga tiket : ",+harga)
print("harga  p: ",+harga)
print("jumlah : "+str(jumlah))
print("--------------------------------------")
print("--------------------------------------")
print("potongan yang di dapat :+,(potongan")
total=(jumlah * harga - potongan)
#input jumlah beli
print("total bayar : ",+(total))
ubay=int(input("masukan uang bayar: "))
ukem=ubay-total
print("uangkembali :",+ukem)