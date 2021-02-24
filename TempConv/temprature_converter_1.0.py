def CtoK(x):
    return x + 273 / 1
def CtoR(x):
    return x * 4/5
def CtoF(x):
    return (x * 9/5) + 32

def KtoC(x):
    return x - 273 / 1
def KtoR(x):
    return (x - 273) * 4/5
def KtoF(x):
    return ((x - 273) * 9/5 ) + 32

def RtoC(x):
    return x * 5/4
def RtoF(x):
    return (x * 9/4) + 32
def RtoK(x):
    return (x * 5/4) + 273

def FtoC(x):
    return (x - 32) * 5/9
def FtoK(x):
    return ((x- 32) * 5/9) + 273
def FtoR(x):
    return (x - 32) * 4/9

print("")

print("Temprature Converter v1.0")
tempIn = input("Input number to convert: ")
tempIn = int(tempIn)

print("")

print("[1] Celsius")
print("[2] Kelvin")
print("[3] Reaumur")
print("[4] Fahrenheit")
unit = input("Select temprature unit: ")

print("")

if unit  == "1":
    unitIn = "Celsius"
    tempOut1 = CtoK(tempIn)
    tempOut2 = CtoR(tempIn)
    tempOut3 = CtoF(tempIn)
    unitOut1 = "Kelvin"
    unitOut2 = "Reaumur"
    unitOut3 = "Fahrenheit"
elif unit == "2":
    unitIn = "Kelvin"
    tempOut1 = KtoC(tempIn)
    tempOut2 = KtoR(tempIn)
    tempOut3 = KtoF(tempIn)
    unitOut1 = "Celsius"
    unitOut2 = "Reaumur"
    unitOut3 = "Fahrenheit"
elif unit == "3":
    unitIn = "Reaumur"
    tempOut1 = RtoC(tempIn)
    tempOut2 = RtoK(tempIn)
    tempOut3 = RtoF(tempIn)
    unitOut1 = "Celsius"
    unitOut2 = "Kelvin"
    unitOut3 = "Fahrenheit"
elif unit == "4":
    unitIn = "Fahrenheit"
    tempOut1 = FtoC(tempIn)
    tempOut2 = FtoK(tempIn)
    tempOut3 = FtoR(tempIn)
    unitOut1 = "Celsius"
    unitOut2 = "Kelvin"
    unitOut3 = "Reaumur"
else:
    print("Please pick a number between 1 and 4")
    print("")
    exit()

print("[1] {}".format(unitOut1))
print("[2] {}".format(unitOut2))
print("[3] {}".format(unitOut3))
unitOut = input("Select temprature unit: ")

print("")

if unitOut == "1":
    print("{} {} is {} {}".format(tempIn,unitIn,tempOut1,unitOut1))
elif unitOut == "2":
    print("{} {} is {} {}".format(tempIn,unitIn,tempOut2,unitOut2))
elif unitOut == "3":
    print("{} {} is {} {}".format(tempIn,unitIn,tempOut3,unitOut3))
else:
    print("Please pick a number between 1 and 4")
    print("")
    exit()

print("")