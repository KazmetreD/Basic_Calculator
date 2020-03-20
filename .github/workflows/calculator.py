print("Welcome to My Basic Calculator")
print("Select the math process you want to do.")
print(">Collection[1]")
print(">Extraction[2]")
print(">Multiplication[3]")
print(">Division[4]")
process = input("> ")

while True:
    if(int(process) == 1):
        sayitoplam1 = input("Please enter the first number: ")
        sayitoplam2 = input("Please enter the second number: ")
        tdeger1 = float(sayitoplam1)
        tdeger2 = float(sayitoplam2)
        tsonuc = tdeger1 + tdeger2
        print("Result= " + str(tsonuc))
        break
    if(int(process) == 2):
        cikarma1 = input("Please enter the first number: ")
        cikarma2 = input("Please enter the second number: ")
        cideger1 = float(cikarma1)
        cideger2 = float(cikarma2)
        cisonuc = cideger1 - cideger2
        print("Result= " + str(cisonuc))
        break
    if(int(process) == 3):
        carpma1 = input("Please enter the first number: ")
        carpma2 = input("Please enter the second number: ")
        cadeger1 = float(carpma1)
        cadeger2 = float(carpma2)
        casonuc = cadeger1 * cadeger2
        print("Result= " + str(casonuc))
        break
    if(int(process) == 4):
        bolme1 = input("Please enter the first number: ")
        bolme2 = input("Please enter the second number: ")
        bdeger1 = float(bolme1)
        bdeger2 = float(bolme2)
        bsonuc = bdeger1 / bdeger2
        print("Result= " + str(bsonuc))
        break
    if(int(process) < 0 or int(process) > 4):
        print("Please select a valid number.")
        break
