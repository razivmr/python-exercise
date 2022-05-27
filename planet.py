#__Muhammad Raziv Maulana Ranie__#
#__2010512093__#

print("\nProgram menghitung berat dimasing planet.")
print("________________________________________\n")
print("Opsi planet :\n")
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Pluto")
print("5. Jupiter")
print("6. Neptune")
print("7. Saturn")
print("8. Uranus")
print("________________________________________")

pilihan = 'y'
x = 0
y = 0

while (pilihan != 'n'):
    def function(x,y):
            if (int(y) == 1):
                M = int(x)*0.38
                print("Saat di Mercury menjadi " + str(M) + "\n")
            elif (int(y) == 2):
                M = int(x)*0.91
                print("Saat di Venus menjadi " + str(M) + "\n")
            elif (int(y) == 3):
                M = int(x)*0.38
                print("Saat di Mars menjadi " + str(M) + "\n")
            elif (int(y) == 4):
                M = int(x)*0.04
                print("Saat di Pluto menjadi " + str(M) + "\n")
            elif (int(y) == 5):
                M = int(x)*2.34
                print("Saat di Jupiter menjadi " + str(M) + "\n")
            elif (int(y) == 6):
                M = int(x)*1.12
                print("Saat di Neptune menjadi " + str(M) + "\n")
            elif (int(y) == 7):
                M = int(x)*0.93
                print("Saat di Saturn menjadi " + str(M) + "\n")
            elif (int(y) == 8):
                M = int(x)*0.92
                print("Saat di Uranus menjadi " + str(M) + "\n")
            else:
                print("pilihan hanya 1--8 saja!\n")
    x = float(input("\nMasukkan beratmu : "))
    y = input("Pilih opsi planet(1-8) : ")
    function(x,y)
    pilihan = input("Apakah ingin diulang (y/n) : ")
    print("_____________")






