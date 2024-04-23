kalimat = input("Masukkan kalimat: ")

# Memisahkan kata-kata dalam kalimat
kata = kalimat.split()

# Menginisialisasi kata terpendek dan terpanjang dengan kata pertama dalam kalimat
kata_terpendek = kata[0]
kata_terpanjang = kata[0]

# Mencari kata terpendek dan terpanjang
for k in kata:
    if len(k) < len(kata_terpendek):
        kata_terpendek = k
    if len(k) > len(kata_terpanjang):
        kata_terpanjang = k

# Menampilkan hasil
print("Kata terpendek:", kata_terpendek)
print("Kata terpanjang:", kata_terpanjang)