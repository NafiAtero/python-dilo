def hurufKeAngka(x):
    angkaKalimat = []
    for i in x:
        if i.isalpha():
            i = i.lower()
            inList = ord(i) - 96
            angkaKalimat.append(inList)
        elif i.isnumeric():
            inList = int(i)
            angkaKalimat.append(inList)
        elif i == " ":
            inList = "spasi"
            angkaKalimat.append(inList)
        else:
            angkaKalimat.append(i)
    return angkaKalimat

kalimat = input("masukan kalimat: ")
angka = hurufKeAngka(kalimat)
print(angka)
