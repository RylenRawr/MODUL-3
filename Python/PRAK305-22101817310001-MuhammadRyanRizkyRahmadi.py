detik = int(input("Sebuah bilangan yang merepresentasikan detik ="))
hari = detik/(3600*24)
mA = detik % (3600*24)
jam = mA/3600
mB = detik % 3600
menit = mB/60
detikI = detik % 60
if (detik>=1 and detik<60):
   print('00:00:%.2d'%(detikI))
elif (detik>=60 and detik<3600):
    print('00:%.2d:%.2d'%(menit,detikI))
elif(detik>=3600 and detik<86400):
    print('%.2d:%.2d:%.2d'%(jam,menit,detikI))
else : print('%d Hari %.2d:%2d:%2d'%(hari,jam,menit,detikI))

