#Masukan Variabel

A = int (input (" Masukan presentase kehadiran Mahasiswa pertama : "))
B = int (input (" Masukan presentase kehadiran Mahasiswa kedua : "))
C = int (input (" Masukan presentase kehadiran Mahasiswa ketiga : "))

#Masukan Statement

if A > B and A > C :
    print ("Presentase Kehadiran Tertinggi : ", A)
if B > A and B > C :
    print ("Presentase Kehadiran Tertinggi : ", B)
if C > A and C > B :
    print ("Presentase Kehadiran Tertinggi : ", C)
