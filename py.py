umr = 2700000
jamKerja = int(input("masukkan jam kerja:   ") or 8)
if jamKerja > 8:
    lembur = jamKerja * 50000 - jamKerja
else:
    lembur = 0
tunjangan = {
"tetap": 0.25 * umr,
"kontrak": 0.1 * umr,
"magang": 0
}
print("umr =","{:,}".format(int(umr)).replace(',','.'))
print("jamkerja =",jamKerja)
print("upah lembur dari jamkerja = ",jamKerja,"x","{:,}".format(int(lembur)).replace(',','.'),'\n')
print ("status kerja: ",[key for key in tunjangan.keys()])
status = input('masukkan status kerja: ')
if status in tunjangan:
    totalGaji = umr + tunjangan [status] + lembur
    print('\nstatus kerja anda adalah',status)
    print("Total gaji yang diterima sebesar Rp","{:,}".format(int(totalGaji)).replace(',','.'))
else:
    print("Harap masukkan yang ada di list")
