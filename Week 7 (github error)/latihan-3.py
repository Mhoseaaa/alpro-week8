def hapus_spasi_berlebih(string):
    string = ' '.join(string.split())
    return string

# Contoh penggunaan
kalimat = input("Masukkan kalimat: ")
kalimat_terhapus_spasi = hapus_spasi_berlebih(kalimat)
print(kalimat_terhapus_spasi)