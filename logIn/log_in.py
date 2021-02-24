userData = ["admin" , "salt"]
passData = ["1234" , "ayam"]
nameData = ["admin" , "Nafi"]
import getpass


userIn = input("Username: ")

if userIn in userData:
    userIdx = userData.index(userIn)
    
    passIn = getpass.getpass("Password: ")

    if passIn in passData:
        passIdx = passData.index(passIn)

        if passIdx == userIdx:
            name = nameData[userIdx]
            print("Welcome back {}.".format(name))
            
        else:
            print("Wrong password.")
    else:
        print("Wrong password.")
else:
    print("Username not found.")