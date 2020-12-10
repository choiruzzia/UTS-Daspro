Gatot = Gaji+Bonus
Nama = input("Nama Karyawan : ")
NIK = input("NIK Karyawan : ")
Status = input("Status (Staff/Honor) : ")
Gol = input("Golongan (A/B/C) : ")
if Status=='Staff':
    Gaji = 2000000
    if Gol=='A':
        Bonus=500000
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    elif Gol=='B':
        Bonus=600000
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    elif Gol=='C':
        Bonus=700000
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    else:
        print("Input salah")
elif Status=='Honor':
    Gaji = 1000000
    if Gol=='A':
        Bonus=200000
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    elif Gol=='B':
        Bonus=300000
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    elif Gol=='C':
        print('Gaji =Rp.',Gaji)
        print('Bonus=Rp.',Bonus)
        print('Gaji total =Rp.',Gatot)
    else:
        print("Input salah")
else:
    print("Input salah")
