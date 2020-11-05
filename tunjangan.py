print("= = = = = = = = = = = = = = =")
print("PROGRAM HITUNG GAJI KARYAWAN")
print("PT AMAN SENTOSA")
print("= = = = = = = = = = = = = = =")
nama    = input("Nama Karyawan      ")
gol     = input("Golongan Jabaatan  ")
pend    = input("Pendidikan         ")
jumlah  = int(input("Jumlah Jam Kerja   "))
gapok   = 300000

#proses
if gol=="1":
    tunjab=0.05*gapok
elif gol=="2":
    tunjab=0.1*gapok
elif gol=="3":
    tunjab=0.15*gapok
else:
    tunjab=0

if pend=="SMA":
    tunpend=0.25 * gapok
elif pend=="D1":
    tunpend=0.05 * gapok
elif pend=="D3":
    tunpend=0.2 * gapok
elif pend=="S1":
    tunpend=0.3 * gapok
else:
    tunpend = 0

if jumlah > 8:
    lembur = (jumlah - 8) * 3500
else:
    lembur = 0 
total=gapok+ tunjab+tunpend+lembur

print("STRUK GAJI KARYAWAN")
print("= = = = = = = = = =")
print("Karyawan yang bernama",nama)
print("Honor yang diterima")
print("         Tunjangan Jabatan    RP",tunjab)
print("         Tunjangan Pendidikan RP",tunpend)
print("         Honor Lembur         RP",lembur)
print("         _______________________")
print("         Total Gaji           RP",total)
print("     (Gaji pokok + tunjangan + lembur    ")