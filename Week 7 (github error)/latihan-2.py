def hitung_frekuensi_kata(kalimat, kata):
    # Mengubah kalimat menjadi lowercase untuk menghindari perbedaan case
    kalimat = kalimat.lower()
    # Menghitung frekuensi kemunculan kata
    frekuensi = kalimat.count(kata.lower())
    return frekuensi

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dihitung: ")

frekuensi = hitung_frekuensi_kata(kalimat, kata)
print(f"{kata} ada {frekuensi} buah")