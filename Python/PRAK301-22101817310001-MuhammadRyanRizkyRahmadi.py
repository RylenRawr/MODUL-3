bilA = int(input("Bilangan Pertama ="))
bilB = int(input("Bilangan Kedua ="))
bilC = int(input("Bilangan Ketiga ="))
if (bilA<bilB and bilB<bilC and bilA<bilC) :
    print(bilA, bilB, bilC)
elif (bilC<bilA and bilA<bilB and bilC<bilB):
    print(bilC, bilA, bilB)
elif (bilB<bilC and bilC<bilA and bilB<bilA):
    print(bilB, bilC, bilA)
elif (bilC<bilB and bilC<bilA and bilB<bilA):
    print(bilC, bilB, bilA)
elif (bilA<bilC and bilA<bilB and bilC<bilB):
    print(bilA, bilC, bilB)
elif (bilB<bilA and bilA<bilC and bilB<bilC):
    print(bilB, bilA, bilC)
else : bilA, bilB, bilC
