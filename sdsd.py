print("======================================================")
print("                PROGRAM PENJUAL BARANG                ")
print("======================================================")

#PROSES INPUT
kodebarang=str(input("Masukan Kode Barang                   : "))
namabarang=str(input("Masukan Nama Barang                   : "))
harga=int(input("Harga Barang                          : "))
jmlbrg=int(input("Jumlah                                : "))

#PROSES OUTPUT 
print("======================================================")

print("               STRUK PEMBAYARAN BARANG                ")
print("======================================================")
#proses Output
print("Kode Barang yang anda input           : "  +str(kodebarang))
print("Nama yang anda input                  : "  +str(namabarang)) 
print("Harga Barang yang anda input          :"  ,"Rp.",+(harga))
print("Jumlah Barang yang anda input         :"  ,+(jmlbrg))
totalharga=harga*jmlbrg
print("======================================================")
print("HARGA JUAL                            :","Rp.",totalharga)

#PROSES DISKON
if totalharga >=100000:
    diskon=totalharga*(10/100)
    totalbelanja_setelahdiskon=totalharga-diskon
    print("POTONGAN HARGA/ DISKON                :","Rp.",diskon)
    print("TOTAL                                 :","Rp.",totalbelanja_setelahdiskon)
    uangkembalidiskon=totalharga-totalbelanja_setelahdiskon
    print("KEMBALI                               :","Rp.",uangkembalidiskon)
#END OF PROSES DISKON

uangbayar=int(input("Cash                                  : Rp. "))
print("======================================================")
uangkembali=uangbayar-totalharga
print("KEMBALI                               :","Rp.",uangkembali)