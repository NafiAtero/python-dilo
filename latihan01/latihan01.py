movList = []

movList.append("Star Wars")
movList.append("Lord of the Rings")
movList.append("Star Trek")
movList.append("Transformers")
movList.append("Harry Potter")

hitung = 0

"""
for x in movList[1:3]:
    print("Movie: " + x)
    hitung = hitung + 1

print("Fav movie: " + movList[0])
print(hitung)

angka = 1 + 1
print(angka)

evenNumbers = [2,4,6,8]
oddNumbers = [1,3,5,7]

allNumbers = oddNumbers + evenNumbers

print(allNumbers)
"""

myString = "Luke Skywalker"
myInt = 12
myFloat = 4.8

"""
print("My string is %s" % myString)
print("My string is %s and my interger is %d" % (myString, myInt))
print("My string is {} and my interger is {}".format(myString, myInt))
print("My string is {1} and my interger is {0}".format(myInt, myString))
"""

listAngka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""
for x in listAngka:
    if(x % 2 == 1) :
        print(x)

    if(x % 3 == 0) :
        print(x)

print(len(myString))
print(len(listAngka))

for movLen in movList:
    print(len(movLen))
"""

#

"""
Ls = "LLLLLilLL"
helloWorld = "Hello World"

#print(Ls.count("L")) #7
#print(helloWorld[2:7]) # [startFrom:endBefore:step]
#print(helloWorld[2:7].count("l"))
#print(helloWorld[::-1]) #dlroW olleH
#print(helloWorld.upper()) #HELLO WORLD
#print(helloWorld.lower()) #hello world
#print(helloWorld.startswith("Hello")) #True
#print(helloWorld.endswith("orld")) #True
splithello = helloWorld.split(" ") #['Hello','World']
print(splithello)
"""


#BOOLEAN OPERATION

"""
x = 2
y = 3
movie = "Star Wars"

if (x == 2) and (y < 2):
    print("y is less than 2")
elif (x == 2) and (y != 2):
    print("y is not 2")
else:
    print("y is not less than 2")

if (x == 2) and (y < 4):
    print("y is less than 4")

if (x == 3) or (y == 3):
    print("either x or y is 3")

if (x == 3) or (y == 3):
    print("either x or y is 3")
"""

#INPUT

"""
userData = ["Atero" , "nafi"]
passData = ["1234" , "ayam"]

userIn = input("Username: ")
passIn = input("Password: ")

if (userIn == "Atero") and (passIn == "1234"):
    print("You are logged in.")
"""

"""
x = [1,2,3]
y = [1,2,3]
a = 2
b = 2
print(x is y)
print(a is b)
"""

#LOOPING

"""
#for
primeNumbers = [2 , 3 , 5 , 7, 11, 13]
for prime in primeNumbers:
    if prime == 3:
        continue
    print(prime)

print("")

for rangeNum in range(5):
    print(rangeNum)

print("")

for rangeNum in range(3, 7):
    print(rangeNum)

print("")

for rangeNum in range(2, 16, 2):
    print(rangeNum)

#while
count = 0
while count < 4:
    print(count)
    if prime == 3:
        break
    count += 1 #count = count + 1

print("")

for genNum in range(10):
    if genNum % 2 == 1:
        continue
    print(genNum)

print("")
"""

#FUNCTION

"""
def my_function():
    print("This is from my function")

def penjumlahan(x,y):
    return x + y

hasil = penjumlahan(10,3)
print(hasil)
"""

#print angka gajil dibawah (input)
"""
def ganjilin(panjang):

    panjang = int(panjang)
    hasil = 1
    
    while hasil <= panjang:
        print(hasil)
        hasil += 2
    
    return "a"
    
pilihPanjang = input("panjang: ")
ganjilin(pilihPanjang)
"""

#angka terkecil dari (list)
"""
def urutPertama(x):
    x = sorted(x)
    return x[0]

angka = [3,5,6,9]
terkecil = urutPertama(angka)

print(terkecil)
"""

#min function
"""
def minimum(a):
    x = a[0]
    for i in a:
        if x > i:
            x = i
    return x

listAngka = [25,8,42,25,5,15]
terkecil = minimum(listAngka)
print(terkecil)
"""

#input jari2 lingkaran
"""
def hitungLingkaran(x):
    pi = math.pi
    if x > 0:
        hasil = pi * (x ** 2)
        return hasil
    else:
        return "ini titik"

import math
radius = input("masukan jari-jari: ")
radius = int(radius)
lingkaran = hitungLingkaran(radius)
print(lingkaran)
"""

#alphToNum 1 line
"""
def alphanumeric(txt):
    return "".join(str(ord(x) - 96) for x in txt.lower() if x.isalpha())

kalimat = input("masukan kalimat: ")
angka = alphanumeric(kalimat)
print(angka)
"""

#CLASS
"""
class Cars:
    def __init__(self,speed,mileage):
        self.speed = speed
        self.mileage = mileage
        
    def getSpeed(self):
        return self.speed
    def getMileage(self):
        return self.mileage

car = Cars(50,10000)
print(car.getSpeed())
print(car.getMileage())
"""
#month name
"""
class Month:

    monthName = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    def __init__(self,index):
        self.index = index

    def getName(self):
        return self.monthName[self.index - 1]

inputBulan = int(input("masukan urut bulan: "))
namaBulan = Month(inputBulan)
print(namaBulan.getName())
"""

#camel case
"""
def toCamelCase(txt):

    splitList = txt.split(" ")
    wordCount = len(splitList)

    camel = splitList[0].lower()

    cameledCount = 1
    while cameledCount < wordCount:
        kata = splitList[cameledCount]

        cameled = kata.capitalize()

        #kapital = kata[0].upper()
        #kata = kata[1:]
        #cameled = kapital + kata

        camel = camel + cameled
        cameledCount += 1

    return camel

text = input("Masukan kalmat: ")
print(toCamelCase(text))
"""

#SECONDS MINUTES HOURS CONVERT
"""
def secondsTominuteAndHours(x):

    second = x % 60
    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)

    minute = x / 60
    minute = math.floor(minute)

    if minute >= 60:
        hour = minute / 60
        hour = math.floor(hour)
        
        minute = minute % 60

        if minute < 10:
            minute = "0" + str(minute)

        hour = str(hour)
        minute = str(minute)
        return hour + ":" + minute + ":" + second

    elif minute < 10:
        minute = "0" + str(minute)
        return str(minute) + ":" + second     

    else:
        return str(minute) + ":" + second


def minutesToHours(x):
    hour = x / 60
    hour = math.floor(hour)
    hour = str(hour)
    hour = hour[:-2]

    minute = x % 60
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    return hour + ":" + minute
"""