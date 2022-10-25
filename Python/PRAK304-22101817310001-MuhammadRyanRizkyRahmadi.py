a = int(input("Bilangan ="))
if (a==0):
    print("Nol")
elif(a>=1 and a<=9):
    print("Satuan")
elif(a==10):
    print("Puluhan")
elif(a>=11 and a<=19):
    print("Belasan")
elif(a>=20 and a<=99):
    print("Puluhan")
else : print("Anda Mengiput Melebihi Limit Bilangan")