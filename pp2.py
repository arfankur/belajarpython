umr = 2700000
jamKerja = int(input("masukkan jam kerja:\t") or 8)
if jamKerja > 8 :
    lembur = jamKerja * 50000 - jamKerja
else:
    lembur = 0
print('T = Tetap\nK = Kontrak\nM = Magang')
status = input("masukan status kerja:\t")

if status == "T":
    tunjangan = 0.25 * umr
    stat = "Tetap"
elif status == "K":
    tunjangan = 0.1 * umr
    stat = "Kontrak"
elif status == "M":
    tunjangan = 0
    stat = "Magang"
totalGaji = umr + tunjangan + lembur
print("\nUMR \t\t\t :","{:,}".format(int(umr)).replace(',','.'))
print("Jam Kerja \t\t :",jamKerja)
print("Upah Lembur \t\t :",lembur)
print('Status Kerja \t\t :',stat)
print("Gaji Yang Diterima\t : Rp","{:,}".format(int(totalGaji)).replace(',','.'),'\n')