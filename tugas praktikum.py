#Himpunan

Jumlah_seluruh_bilangan_asli = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        Jumlah_seluruh_bilangan_asli = Jumlah_seluruh_bilangan_asli + i

print ("Jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 kurang dari 1000 =", Jumlah_seluruh_bilangan_asli)
