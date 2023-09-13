jarak = float(input("Masukkan jarak pengiriman: "))

if jarak < 5:
    print("Biaya ongkos kirim anda gratis")
elif 5 <=  jarak <= 10:
    print("Biaya ongkos kirim anda adalah: ", 5000*jarak)
elif 10 <=  jarak <= 20:
    print("Biaya ongkos kirim anda adalah: ", 6000*jarak)
elif 20 <= jarak <= 30:
    print("Biaya Ongkos Kirim anda adalah: ", 7000* jarak)   
else:
    print("Biaya ongkos kirim anda adalah: ", 9000*jarak) 
    hf