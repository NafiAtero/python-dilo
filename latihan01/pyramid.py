def pyramid(l):

    loopNo = 0
    a = " "
    b = "*"
    jumlahSpasi = l - 1
    jumlahBintang = 1

    
    while loopNo < l:
        
        print(a*jumlahSpasi + b*jumlahBintang)
        loopNo += 1
        jumlahSpasi -= 1
        jumlahBintang += 2

lantai = int(input("Masukan jumlah lantai piramida: "))
pyramid(lantai)